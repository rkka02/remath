#!/usr/bin/env python3
"""Exact boundary chess maps and independent numerical checks for Study 03.

Run with Python 3 and mpmath, optionally NumPy for --scan. Vertex parameters
are counterclockwise edge index plus edge fraction. s is physical ray slope.
"""
from __future__ import annotations

import argparse
import bisect
import math
import subprocess
import sys
from fractions import Fraction as Q
from functools import cached_property
from numbers import Integral
from pathlib import Path

import mpmath as mp
from mpmath.ctx_iv import MPIntervalContext, ivmpf
from mpmath.libmp import from_rational, round_nearest, to_rational

STUDY = Path(__file__).resolve().parents[1]


UNRESOLVED = 'unresolved'


class InsufficientResolution(ValueError):
    """A geometric decision needs more precise input."""


def rational(x):
    """Exact value of a supplied integer, rational or rounded binary number."""
    if isinstance(x, Q):
        return Q(int(x.numerator), int(x.denominator))
    if isinstance(x, Integral):
        return Q(int(x))
    if isinstance(x, mp.mpf):
        if not mp.isfinite(x):
            raise InsufficientResolution('unresolved: a finite enclosure is required')
        return Q(*to_rational(x._mpf_))
    return Q(x)


def mp_value(x):
    return mp.mp.make_mpf(from_rational(x.numerator, x.denominator, mp.mp.prec, round_nearest))


def _radius(input_radius, tol=None):
    """Accept the former tol argument as an explicit absolute input radius."""
    if tol is not None and input_radius is not None:
        raise ValueError('supply only one of input_radius and tol')
    radius = rational(input_radius if input_radius is not None else tol or 0)
    if radius < 0:
        raise ValueError('input_radius must be nonnegative')
    return radius


def input_ball(value, radius):
    """Exact center and radius of an integer, fraction, interval or bounded estimate."""
    if isinstance(value, ivmpf):
        lo, hi = (rational(mp.mp.make_mpf(end)) for end in value._mpi_)
        return (lo+hi)/2, (hi-lo)/2
    if isinstance(value, (Integral, Q)):
        return rational(value), Q(0)
    if not radius:
        raise InsufficientResolution('unresolved: a rounded input needs a positive input_radius '
                                     'or an outward interval')
    return rational(value), radius


def input_interval(value, ctx, input_radius=None):
    """Move a supplied enclosure into an interval context with outward rounding."""
    if isinstance(value, ivmpf):
        return ctx.mpf(value)
    x, r = input_ball(value, _radius(input_radius))
    lo, hi = x-r, x+r
    return ctx.mpf([ctx.mpf(lo.numerator)/lo.denominator, ctx.mpf(hi.numerator)/hi.denominator])


def enclosed_parameters(values, input_radius=None):
    """Use fractions for exact formulas and outward intervals for uncertain parameters."""
    values = tuple(values)
    radius = _radius(input_radius)
    balls = [input_ball(x, radius) for x in values]
    if all(r == 0 for _, r in balls):
        return [x for x, _ in balls]
    iv = MPIntervalContext()
    iv.prec = mp.mp.prec
    return [input_interval(value, iv, radius) for value in values]


def distinct(values, tol):
    """Unique exact rationals, or clustered numerical event estimates."""
    values = sorted(values)
    if all(isinstance(x, (Integral, Q)) for x in values):
        return sorted(set(values))
    result = []
    for x in values:
        if not result or x - result[-1] > tol:
            result.append(x)
    return result


class CirclePL:
    """Monotone lift. The nominal graph uses exact coordinates, even for mpf input.

    The period is fixed. For rounded inputs, error and inverse_error bound the uniform lift errors.
    Each true subdivision mark is within knot_error of its nominal mark, in
    cyclic distance. Coincident marks may split under perturbation.
    """

    def __init__(self, knots, images, degree, input_radius=None, *, tol=None):
        bound = _radius(input_radius, tol)
        xs = [input_ball(x, bound) for x in knots]
        ys = [input_ball(y, bound) for y in images]
        radius = max(r for _, r in xs+ys)
        self.x, self.y = [x for x, _ in xs], [y for y, _ in ys]
        self.degree, self.period = degree, self.x[-1]
        assert degree in (-1, 1) and self.x[0] == 0
        assert len(self.x) == len(self.y) and all(a < b for a, b in zip(self.x, self.x[1:]))
        last = self.y[0] + degree*self.period
        assert abs(self.y[-1]-last) <= 2*radius
        self.y[-1] = last
        assert all(degree*(v-u) > 0 for u, v in zip(self.y, self.y[1:]))
        self.lookup = self.y if degree == 1 else [-v for v in self.y]
        self.tol = self.knot_error = self.error = self.inverse_error = radius
        self.support_vertices = ()
        if radius:
            # Interpolate corresponding perturbed endpoints, then move the
            # argument back by at most radius along the nominal graph.
            self.error = (1+self.lipschitz)*radius
            self.inverse_error = (1+self.inverse_lipschitz)*radius

    @cached_property
    def lipschitz(self):
        return max(abs((v-u)/(b-a)) for a,b,u,v in zip(self.x, self.x[1:], self.y, self.y[1:]))

    @cached_property
    def inverse_lipschitz(self):
        return max(abs((b-a)/(v-u)) for a,b,u,v in zip(self.x, self.x[1:], self.y, self.y[1:]))

    def _lap(self, offset, inexact):
        if inexact:
            n = int(mp.floor(mp_value(offset/self.period), prec=0))
            if 0 <= offset-n*self.period < self.period:
                return n
        return offset // self.period

    def __call__(self, x):
        inexact = not isinstance(x, (Integral, Q))
        x = rational(x)
        n = self._lap(x, inexact)
        t = x - n*self.period
        i = bisect.bisect_right(self.x, t)-1
        f = (t-self.x[i]) / (self.x[i+1]-self.x[i])
        value = self.y[i] + f*(self.y[i+1]-self.y[i]) + n*self.period*self.degree
        return mp_value(value) if inexact else value

    def inverse(self, y):
        inexact = not isinstance(y, (Integral, Q))
        y, d = rational(y), self.degree
        n = self._lap(d*(y-self.y[0]), inexact)
        t = y - n*d*self.period
        i = bisect.bisect_right(self.lookup, d*t)-1
        f = (t-self.y[i]) / (self.y[i+1]-self.y[i])
        value = self.x[i] + f*(self.x[i+1]-self.x[i]) + n*self.period
        return mp_value(value) if inexact else value

    def after(self, other):
        assert self.period == other.period
        pulled = [other.inverse(v) % self.period for v in self.x[:-1]]
        knots = sorted(set(other.x).union(pulled))
        result = CirclePL(knots, [self(other(x)) for x in knots], self.degree*other.degree)
        result.tol = max(self.tol, other.tol)
        if result.tol:
            result.error = self.error + self.lipschitz*other.error
            result.inverse_error = other.inverse_error + other.inverse_lipschitz*self.inverse_error
            # A break is inherited from the inner map or pulled back through it.
            result.knot_error = max(other.knot_error, other.inverse_error +
                                    other.inverse_lipschitz*self.knot_error)
        return result

    def power(self, q):
        if q < 1:
            raise ValueError('positive period required')
        result = self
        for _ in range(1, q):
            result = self.after(result)
        return result

    def one_lap_lift(self, reference=None):
        """Normalize at zero, or align to the closest lift of a fixed reference at zero.

        A single integer shift applies on the whole line. For independently
        normalized inputs the error includes any change of lap at the seam.
        """
        origin = 0
        if reference is not None:
            if reference.period != self.period or reference.degree != self.degree:
                raise ValueError('lift comparison requires the same period and degree')
            origin = reference.y[0] - self.period/2
        offset = self.y[0] - origin
        lap = offset // self.period
        shift = lap*self.period
        result = CirclePL(self.x, [y-shift for y in self.y], self.degree)
        result.tol, result.knot_error = self.tol, self.knot_error
        # A common supporting vertex at zero pins the normalized image there
        # for every admissible polygon, including perturbations of the other vertices.
        origin_error = 0 if 0 in self.support_vertices else self.error
        first = (offset-origin_error) // self.period
        last = (offset+origin_error) // self.period
        seam_error = max(lap-first, last-lap)*self.period
        result.error = self.error + seam_error
        result.inverse_error = self.inverse_error + seam_error
        result.support_vertices = self.support_vertices
        return result

    def displacement(self, turns):
        """Nominal knot displacements, exact for rational input geometry."""
        return [y-x-turns*self.period for x, y in zip(self.x, self.y)]

    def rotation_status(self, turns):
        """True for a crossing, False for strict exclusion, or unresolved."""
        D = self.displacement(turns)
        if not self.tol:
            return min(D) <= 0 <= max(D)
        margin = max(self.error, self.tol)
        if min(D) > margin or max(D) < -margin:
            return False
        if min(D) < -margin and max(D) > margin:
            return True
        return UNRESOLVED

    def fixed_cells(self, turns):
        """Neutral pieces, interior roots and boundary roots, or unresolved."""
        D = self.displacement(turns)
        if self.tol:
            # Bound the displacement at *every* true break, including marks
            # that coincide only in the nominal graph. Opposite certified signs
            # have disjoint position enclosures and preserve their cyclic order.
            margin = max(self.tol, self.error + (1+self.lipschitz)*self.knot_error)
            if any(abs(d) <= margin for d in D):
                return UNRESOLVED
        neutral, isolated, endpoints = [], [], []
        for i, (a, b) in enumerate(zip(self.x, self.x[1:])):
            l, r = D[i:i+2]
            if l == 0:
                endpoints.append(a)
            if l == r == 0:
                neutral.append((a, b))
            elif l*r < 0:
                multiplier = (self.y[i+1]-self.y[i]) / (b-a)
                root = a-l*(b-a)/(r-l)
                isolated.append((mp_value(root), mp_value(multiplier)) if self.tol else
                                (root, multiplier))
        return neutral, isolated, endpoints


def _chord(levels, radius):
    """Build the nominal opposite-endpoint map and enclose its perturbation."""
    n = len(levels)
    steps = [levels[(j+1) % n]-start for j, start in enumerate(levels)]
    smallest = min(map(abs, steps))
    if radius and smallest <= 2*radius:
        raise InsufficientResolution('unresolved: cannot separate an edge from a tangent chord')
    if not smallest:
        raise ValueError('edge parallel to chord; use the critical-edge trace criterion')

    graph = {}
    for i, height in enumerate(levels):
        hits = set()
        for j, start in enumerate(levels):
            stop = levels[(j+1) % n]
            if min(start, stop) <= height <= max(start, stop):
                hits.add((j+(height-start)/steps[j]) % n)
        hits.discard(i)
        target, = hits or {Q(i)}
        graph[Q(i)] = target
        graph[target] = Q(i)
    knots = sorted(graph)
    images = []
    for t in knots:
        y = graph[t]
        if images and y >= images[-1]:
            y -= n
        images.append(y)
    result = CirclePL(knots+[Q(n)], images+[images[0]-n], -1)
    result.tol = radius
    # At a fixed source the level changes by <= radius on each chain.
    # The opposite monotone chain has nominal inverse Lipschitz 1/smallest.
    # The strict edge tests above keep both extremal vertices fixed.
    result.error = result.inverse_error = result.knot_error = 2*radius/smallest
    return result


def chord(projections, input_radius=None, *, tol=None):
    """Other endpoint at equal projection on a transverse convex polygon."""
    bound = _radius(input_radius, tol)
    balls = [input_ball(value, bound) for value in projections]
    return _chord([v for v, _ in balls], max(r for _, r in balls))


def chess(points, s, input_radius=None, *, tol=None):
    """Two-chord map on a transverse convex polygon, first flight of slope +s.

    Integers and fractions are exact. Each interval supplies its own bounds.
    input_radius bounds the absolute error of every bare float or mpf.
    """
    bound = _radius(input_radius, tol)
    s, ds = input_ball(s, bound)
    minus, plus = [], []
    projection_error = Q(0)
    for x, z in points:
        x, dx = input_ball(x, bound)
        z, dz = input_ball(z, bound)
        minus.append(z-s*x)
        plus.append(z+s*x)
        projection_error = max(projection_error, dz + abs(s)*dx + ds*(abs(x)+dx))
    billiard = _chord(plus, projection_error).after(_chord(minus, projection_error))
    # Both supporting vertices of each projection survive the strict edge tests.
    billiard.support_vertices = tuple(sorted({minus.index(min(minus)), minus.index(max(minus))} &
                                              {plus.index(min(plus)), plus.index(max(plus))}))
    return billiard.one_lap_lift()


def rotated_rectangle(phi, R, ctx=mp, *, input_radius=None):
    if isinstance(ctx, MPIntervalContext):
        phi, R = (input_interval(x, ctx, input_radius) for x in (phi, R))
    C, S = ctx.cos(phi), ctx.sin(phi)
    return [(0, 0), (C, S), (C-R*S, S+R*C), (-R*S, R*C)]


def regular_polygon(n, phi, ctx=mp, *, input_radius=None):
    if isinstance(ctx, MPIntervalContext):
        phi = input_interval(phi, ctx, input_radius)
    return [(ctx.cos(phi+2*ctx.pi*i/n), ctx.sin(phi+2*ctx.pi*i/n)) for i in range(n)]


def rational_degrees(s, tan_phi, R=1, *, input_radius=None):
    """Ray map with common dilation suppressed, exact for rational parameters."""
    f, R = enclosed_parameters((tan_phi, R), input_radius)
    return chess([(0, 0), (1, f), (1-R*f, f+R), (-R*f, R)], s, input_radius)


def certify_rotation(b, q):
    """Return the reduced numerator, None for exclusion, or 'unresolved'.

    The map carries the enclosures supplied at construction through every iterate.
    """
    if b.y[0]-b.error < 0 or b.y[0]+b.error >= b.period:
        b = b.one_lap_lift()
    g = b.power(q)
    if b.support_vertices:
        vertex = b.support_vertices[0]
        if q == 1 and vertex != 0 and b.error >= b.period:
            # A common support guarantees a fixed point modulo the period.
            # Independent normalization may still change its integer winding.
            return UNRESOLVED, g
        return ((b(vertex)-vertex)//b.period if q == 1 else None), g
    result = None
    for p in range(q+1):
        if math.gcd(p, q) == 1:
            status = g.rotation_status(p)
            if status is True:
                return p, g
            if status == UNRESOLVED:
                result = UNRESOLVED
    return result, g


def verify_basics():
    b = chess([(0, 0), (1, 0), (1, 1), (0, 1)], Q(1))
    p, g = certify_rotation(b, 2)
    assert p == 1 and all(z == 0 for z in g.displacement(1))
    # gamma-minus first, CCW edge coordinate. At s=1/2, rho=2/3.
    p, g = certify_rotation(chess([(0, 0),(1, 0),(1, 1),(0, 1)], Q(1,2)), 3)
    assert p == 2 and all(z == 0 for z in g.displacement(p))
    # At tan(phi)=1/5 tilt and s=1, multiplier mu^-2=(2/3)^4.
    p, g = certify_rotation(rational_degrees(1, Q(1,5)), 2)
    neutral, cycles, _ = g.fixed_cells(p)
    assert not neutral and {m for _, m in cycles} == {Q(16,81), Q(81,16)}
    print('Exact square checks: rho(s=1/2)=2/3 CCW; tan(phi)=1/5, s=1 has multiplier 16/81.')
    tol = mp.mpf('1e-62')
    iv = MPIntervalContext()
    iv.dps = mp.mp.dps + 8
    sq = rotated_rectangle(iv.pi/12, 1, iv)
    p, g = certify_rotation(chess(sq, 1), 2)
    _, roots, _ = g.fixed_cells(p)
    M = min(m for _, m in roots)
    assert abs(M-1/mp.mpf(9)) < tol
    print('15 degree square, per step log multiplier:', mp.nstr(mp.log(M)/2, 55))
    # A mirror direction on regular N=4q has order q globally.
    for p, q in ((1,2), (1,3), (2,5), (3,7)):
        t = iv.pi*p/(2*q)
        b = chess(regular_polygon(4*q, iv.mpf(0), iv), iv.tan(t))
        r, g = certify_rotation(b, q)
        # Reflection symmetry gives the exact winding. The rounded return
        # only checks its residual and cannot certify equality.
        assert r == UNRESOLVED
        assert max(map(abs, g.displacement(q-p))) < rational(tol)
    print('Mirror theorem, numerical residual checks: (N,q)=(8,2),(12,3),(20,5),(28,7).')


def check_small_periods():
    phi = mp.pi/12
    box = rotated_rectangle(phi, 1)
    def speeds(t):
        return mp.tan(t-phi), mp.tan(t+phi)
    def root(condition):
        return mp.findroot(lambda t: condition(*speeds(t)), (phi+mp.mpf('.005'), mp.pi/6))
    tests = [
        ('1/4 upper edge', root(lambda a,b: a*2+b-1), Q(1,4), False),
        ('1/3 standing mode', root(lambda a,b: a+b-1), Q(1,3), True),
        ('2/5 standing mode', root(lambda a,b: a*a+a*b+b*b-a-b), Q(2,5), True),
        ('1/2 lower edge', mp.pi/6, Q(1,2), False),
    ]
    print('Tilt 15 degrees, R=1; clockwise label, angle in degrees, physical frequency.')
    for name, t, clockwise, identity in tests:
        b = chess(box, mp.tan(t), mp.mpf('1e-58'))
        q = clockwise.denominator
        p, g = certify_rotation(b, q)
        # The checkerboard formulas above specify the parameter and winding.
        # At either a neutral angle or an endpoint one extremum touches zero.
        expected = q - clockwise.numerator
        assert p == UNRESOLVED
        D = g.displacement(expected)
        assert min(map(abs, D)) <= b.tol
        assert (max(map(abs, D)) <= b.tol) == identity
        print(name, mp.nstr(mp.degrees(t),34), mp.nstr(mp.cos(t),53))
    # 2/5 in the CCW convention occurs at the complementary angle for the square.
    # The 1/4 plateau runs from the lower critical angle up to the computed endpoint.
    t=(phi+tests[0][1])/2
    p,g=certify_rotation(chess(box,mp.tan(t),mp.mpf('1e-58')),4)
    a,b=speeds(t)
    _,roots,_=g.fixed_cells(p)
    assert p==3 and abs(min(m for _,m in roots)-(a/b)**2) < mp.mpf('1e-55')


def hexagon():
    # (xi,eta)=(z+x,z-x). The counterclockwise orientation is preserved.
    vertices = [(0,-1),(Q(1,2),-Q(1,2)),(Q(25,36),Q(1,12)),
                (Q(1,4),Q(3,4)),(0,1),(-1,0)]
    xy = [((Q(v)-w)/2,(Q(v)+w)/2) for v,w in vertices]
    return vertices, xy


def verify_hexagon():
    vertices, xy = hexagon()
    b = chess(xy, Q(1))
    p, g = certify_rotation(b, 2)
    intervals, roots, _ = g.fixed_cells(p)
    assert p==1 and intervals and sorted(m for _,m in roots)==[Q(1,2)]*2+[Q(2)]*2
    print('Hexagon vertices (xi,eta):', ' '.join(f'({v},{w})' for v,w in vertices))
    print('Period-two rectangle: xi in [-3/4,7/12], eta in [-1/4,1/4].')
    print('Interior roots and b^2 multipliers in CCW edge coordinates:',
          ', '.join(f'{t}: {m}' for t,m in roots))
    # A sign-changing H1 profile with max +/-1, attaining the sharp 1/2 observation bound.
    knots=[Q(3,4),Q(13,16),Q(7,8),Q(15,16),Q(1)]
    values=[0,1,0,-1,0]
    def h(z):
        if z <= knots[0] or z >= knots[-1]:
            return 0
        i=bisect.bisect_right(knots,z)-1
        return values[i]+(values[i+1]-values[i])*(z-knots[i])/(knots[i+1]-knots[i])
    def field(v,w):
        return h(1-abs(v))-h(abs(w))
    assert field(Q(1,16),Q(13,16))==-2
    assert field(Q(3,16),Q(1,4))==1 and field(Q(1,16),Q(1,4))==-1
    energy=4*sum(Q((q-p)**2)/(b-a) for a,b,p,q in zip(knots,knots[1:],values,values[1:]))
    assert energy==256
    print('Sharp observation example: field norm 2, attractor trace norm 1, Dirichlet energy 256.')
    # Preserve the right wall and use its antipodal copy as the left wall.
    right=vertices[:5]
    central=right+[(-v,-w) for v,w in right[1:-1]]
    central_xy=[((Q(v)-w)/2,(Q(v)+w)/2) for v,w in central]
    central_map=chess(central_xy,Q(1)).power(2)
    neutral, roots, _=central_map.fixed_cells(1)
    assert neutral and sorted(m for _,m in roots)==[Q(1,4)]*2+[Q(4)]*2
    print('Antipodally symmetric octagon: neutral intervals and full-circuit factors 1/4 and 4.')


def verify_rigidity_example():
    # The square with all four corners cut identically has all axial support faces.
    polygon=[(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]
    for slope, q, target in ((Q(3,5),3,Q(1,16)), (Q(7,18),4,Q(121,625)),
                             (Q(5,17),5,Q(36,121))):
        b=chess(polygon,slope)
        p,g=certify_rotation(b,q)
        assert p == q-1
        neutral, roots, endpoints = g.fixed_cells(p)
        assert not neutral and not endpoints
        assert sorted(m for _, m in roots) == [target]*(2*q) + [1/target]*(2*q)
        print(f'Four-corner chamfer: s={slope}, CCW {p}/{q}, two attracting and two repelling cycles, multipliers {target} and {1/target}.')


def verify_central_count():
    from phase1_coexistence import prescribed_wall

    threshold = Q(3, 4)
    for count in (2, 3, 6):
        heights = [threshold * j / (count + 1) for j in range(1, count + 1)]
        half_rates = [Q(2*j-1, 2*j+1) for j in range(1, count + 1)]
        wall = prescribed_wall(heights, half_rates, threshold)
        vertices = [*wall, *((-v, -w) for v, w in wall[1:-1])]
        physical = [((v-w)/2, (v+w)/2) for v, w in vertices]
        assert len(physical) == 2*count+6
        neutral, roots, _ = chess(physical, Q(1)).power(2).fixed_cells(1)
        factors = sorted(rate for _, rate in roots if rate < 1)
        assert neutral and factors == sorted([rate**2 for rate in half_rates]*2)
    print('Central polygons with 10, 12 and 18 sides attain the mixed period-two bound '
          'with 2, 3 and 6 independently set attracting rates.')


def verify_critical_triangles():
    from phase1_pde import periodic_set

    for xi, eta, q in (((-1,1,0),(0,0,1),2), ((0,1,0),(0,0,1),3)):
        _, _, intervals, _ = periodic_set([tuple(map(Q,eta)),tuple(map(Q,xi))]*q)
        assert sum(b-a for a,b in intervals) == 3
    print('Characteristic triangles: midpoint maps have global periods 2 and 3; both PDE kernels are zero.')


def draw_hexagon():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Polygon
    import numpy as np
    vertices, _ = hexagon()
    fig, (ax, bx) = plt.subplots(1,2,figsize=(9,4.35),constrained_layout=True,
                                gridspec_kw={'width_ratios':[1.15,1]})
    def transform(v,w):
        return ((v-w)/2,(v+w)/2)
    limit = Polygon([transform(float(v),float(w)) for v,w in vertices],closed=True,
                    edgecolor='#28313a',facecolor='none',lw=1.8,zorder=5)
    ax.add_patch(limit)
    def band(v0,v1,w0,w1):
        patch=Polygon([transform(v,w) for v,w in ((v0,w0),(v1,w0),(v1,w1),(v0,w1))],
                      closed=True,lw=0,facecolor='#b7d8e5')
        patch.set_clip_path(limit)
        ax.add_patch(patch)
    band(-.25,.25,-1,1)
    for y in (.79,.86,.93):
        s=1-y
        points=[transform(v,w) for v,w in ((-s,-y),(s,-y),(s,y),(-s,y),(-s,-y))]
        ax.plot(*zip(*points),color='#33768b',lw=.75,alpha=.85)
    loop=[transform(v,w) for v,w in ((-.75,-.25),(7/12,-.25),(7/12,.25),(-.75,.25),(-.75,-.25))]
    ax.plot(*zip(*loop),color='#ad452e',lw=2.1)
    ax.scatter(*zip(*loop[:-1]),s=17,color='#ad452e',zorder=6)
    ax.set(xlim=(-.57,.57),ylim=(-.57,.57),aspect='equal',xlabel='x',ylabel='z',
           title='Standing waves and focusing rays')
    ax.legend(handles=[Line2D([0],[0],color='#33768b',lw=1,label='Neutral rays'),
                       Line2D([0],[0],color='#ad452e',lw=2,label='Attracting circuit')],
              loc='upper center',bbox_to_anchor=(.5,-.13),ncol=2,frameon=False,fontsize=9)
    xx=np.linspace(-.75,7/12,900)
    def f(y):
        return np.interp(y,[0,.75,13/16,7/8,15/16,1],[0,0,1,0,-1,0])
    bx.axhline(0,color='#63717a',lw=.7)
    bx.plot(xx,f(1-np.abs(xx)),color='#ad452e',lw=2)
    bx.set(title='A standing mode on one attractor leg',
           xlabel=r'$\xi=z+x$ along $\eta=z-x=1/4$',ylabel='Stream function',
           ylim=(-1.18,1.18),yticks=[-1,0,1],box_aspect=1)
    for a in (ax,bx):
        a.spines[['top','right']].set_visible(False)
    path=STUDY/'figures'/'phase1_coexistence.png'
    fig.savefig(path,dpi=170,bbox_inches='tight')
    plt.close(fig)
    print('Wrote',path.relative_to(STUDY))


SQUARE_PERIODS = (2, 4, 6, 8, 10, 12)
SQUARE_SINGULAR = len(SQUARE_PERIODS) + 2


def square_tongue_labels(tilt_ticks, angle_ticks):
    """Classify midpoint samples in integer twentieths of a degree."""
    import numpy as np
    from phase1_rectangle import section_endpoint

    phi, theta = np.meshgrid(tilt_ticks, angle_ticks)
    if not all(np.issubdtype(axis.dtype, np.integer) for axis in (phi, theta)):
        raise ValueError("the angle grid requires integer twentieths of a degree")
    if np.any(phi < 0) or np.any(phi > 900) or np.any(theta < 0) or np.any(theta > 1800):
        raise ValueError("tick coordinates must lie in [0, 900] for tilt and [0, 1800] for ray angle")
    phi = phi.astype(np.int64, copy=False)
    theta = theta.astype(np.int64, copy=False)
    lower, upper = theta-phi, theta+phi
    critical = (lower == 0) | (upper == 1800)
    interior = (lower > 0) & (upper < 1800)
    # The primary endpoints inside the supercritical window have a=1 or b=1.
    singular = critical | (interior & ((lower == 900) | (upper == 900)))
    regular = interior & ~singular
    a = np.tan(np.deg2rad(np.where(regular, lower/20, 30.)))
    b = np.tan(np.deg2rad(np.where(regular, upper/20, 60.)))
    ratio, translation = b/a, a*b/(a+b)
    labels = np.where(interior, 0, 1)
    labels[singular] = SQUARE_SINGULAR
    primary = regular & (lower < 900) & (upper > 900)
    labels[primary] = 2
    # For the remaining tongues binary64 only nominates pixels. Certify both
    # strict endpoint inequalities from the integer angles before coloring.
    iv = MPIntervalContext()
    iv.dps = 40
    ticks = np.union1d(lower[regular], upper[regular])
    tangent = {t: iv.tan(int(t)*iv.pi/3600) for t in ticks}
    for index, q in enumerate(SQUARE_PERIODS[1:], 3):
        for n in range(1, q):
            m = q-n
            if math.gcd(n, m) != 1:
                continue
            winding = Q(q, 2*m)
            end1 = section_endpoint(winding, ratio)
            end2 = section_endpoint(winding, 1/ratio)
            active = (regular & ~primary & (translation > np.minimum(end1, end2))
                      & (translation < np.maximum(end1, end2)))
            for row, col in zip(*np.nonzero(active)):
                low, high = tangent[lower[row, col]], tangent[upper[row, col]]
                stretch = high/low
                shift = low*high/(low+high)
                left = section_endpoint(winding, stretch)
                right = section_endpoint(winding, 1/stretch)
                if left < shift < right or right < shift < left:
                    labels[row, col] = index
    return labels


def draw_square_tongues():
    """Draw the closed-form tongue tests on a midpoint grid of the two angles."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    import numpy as np

    tilt_ticks, angle_ticks = np.arange(1, 900, 2), np.arange(1, 1800, 2)
    labels = square_tongue_labels(tilt_ticks, angle_ticks)
    tilt_deg, angle_deg = tilt_ticks/20, angle_ticks/20
    phi, theta = np.meshgrid(tilt_ticks, angle_ticks)
    interior = (theta > phi) & (theta+phi < 1800)
    a = np.tan(np.deg2rad(np.where(interior, (theta-phi)/20, 30.)))
    b = np.tan(np.deg2rad(np.where(interior, (theta+phi)/20, 60.)))
    colors=['#ffffff','#d7d9db','#316e85','#d78956','#8fb7cc','#9a84ac','#70a899','#e4c477','#59475d']
    fig, ax = plt.subplots(figsize=(8,4.4),layout='constrained')
    ax.imshow(labels,extent=(0,45,0,90),origin='lower',interpolation='nearest',aspect='auto',
              cmap=ListedColormap(colors),vmin=-.5,vmax=len(colors)-.5)
    # Keep the one-sample-wide singular sets visible when the raster is reduced.
    for tilts, angles in [((0, 45), (0, 45)), ((0, 45), (90, 45)),
                          ((0, 22.5), (45, 22.5)), ((0, 22.5), (45, 67.5))]:
        ax.plot(tilts, angles, color=colors[SQUARE_SINGULAR], linewidth=.65)
    for residual in (a+b-1,1/a+1/b-1):
        ax.contour(tilt_deg,angle_deg,np.ma.array(residual,mask=~interior),
                   levels=[0],colors='#28333a',linestyles='dashed',linewidths=.9)
    handles=[Patch(facecolor=colors[i],label=f'Period {q}') for i,q in enumerate(SQUARE_PERIODS,2)]
    handles.extend([Patch(facecolor=colors[1],label='Corner capture'),
                    Patch(facecolor=colors[SQUARE_SINGULAR],label='Critical or primary endpoint'),
                    Patch(facecolor='white',edgecolor='#b0b0b0',label='Other frequencies'),
                    Line2D([0],[0],color='#28333a',ls='--',label='Period 3, regular rays close')])
    ax.legend(handles=handles,loc='center left',bbox_to_anchor=(1.015,.5),frameon=False,fontsize=9)
    ax.set(xlabel='Square tilt φ (degrees)',ylabel='Ray inclination θ (degrees)',
           title='Attracting periods in a tilted square',xticks=[0,7.5,15,22.5,30,37.5,45],
           yticks=[0,15,30,45,60,75,90])
    path=STUDY/'figures'/'phase1_square_tongues.png'
    fig.savefig(path,dpi=160,bbox_inches='tight')
    plt.close(fig)
    print('Wrote',path.relative_to(STUDY))


def scan_geometry():
    """A deterministic diagnostic of low-period crossings.

    Binary64 orbits nominate p/q. Outward trigonometry on rational multiples
    of pi supplies the vertex and slope enclosures used by the rational lift.
    """
    import numpy as np
    iv = MPIntervalContext()
    iv.dps = mp.mp.dps + 8
    print('Grid: 120 midpoint angles, degrees (j+1/2)*90/120, candidate q<=12')
    print('N,corner,isolated_low_period,all_periodic_low_period,mixed_or_endpoint,unresolved,critical')
    for n in (3, 4, 5, 6, 7, 8, 10, 12, 20):
        poly = regular_polygon(n, iv.pi/36, iv)
        # Edge bearings in units of pi, taken modulo an unoriented half-turn.
        walls = {(Q(1, 36) + Q(2*i+1, n) + Q(1, 2)) % 1 for i in range(n)}
        counts = [0]*6
        for j in range(120):
            direction = Q(2*j+1, 480)
            if direction in walls or (-direction) % 1 in walls:
                counts[5] += 1
                continue
            s = iv.tan(iv.pi*direction.numerator/direction.denominator)
            try:
                b = chess(poly, s)
            except InsufficientResolution:
                counts[4] += 1
                continue
            if b.support_vertices:
                counts[0] += 1
                continue
            knots = np.array(b.x, dtype=float)
            ys = np.array(b.y, dtype=float)
            # Track entire lift using a kept turn count; avoid cancellation in phase.
            u, turns = 0.378, 0
            for _ in range(256):
                v = np.interp(u, knots, ys)
                turns += math.floor(v/n)
                u = v % n
            approx = (turns+(u-0.378)/n)/256
            choices = sorted({Q(p, q) for q in range(1, 13) for p in range(q+1)},
                             key=lambda x: abs(float(x)-approx))
            r = choices[0]
            g = b.power(r.denominator)
            if g.rotation_status(r.numerator) is not True:
                counts[4] += 1
                continue
            cells = g.fixed_cells(r.numerator)
            if cells == UNRESOLVED:
                counts[4] += 1
            else:
                intervals, roots, endpoints = cells
                assert roots and not intervals and not endpoints
                counts[1] += 1
        print(','.join(map(str, [n, *counts])))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scan', action='store_true', help='also run the regular-polygon finite grid')
    parser.add_argument('--figure', action='store_true', help='draw the hexagon and tilted-square tongue diagram')
    parser.add_argument('--core-only', action='store_true', help='skip the chapter-specific verification programs')
    args = parser.parse_args()
    mp.mp.dps = 72
    verify_basics()
    check_small_periods()
    verify_hexagon()
    verify_central_count()
    verify_rigidity_example()
    verify_critical_triangles()
    if not args.core_only:
        for chapter in ('pde','rectangle','parity','measure','canonical','coexistence','multiple','regular'):
            program=STUDY/'experiments'/f'phase1_{chapter}.py'
            print(f'\n{program.name}',flush=True)
            options=['--tongues'] if chapter=='regular' and args.scan else []
            subprocess.run([sys.executable,'-B',str(program),*options],check=True)
        if args.scan:
            for resonance in ((16,4,5),(9,3,5),(15,6,5),(24,4,3)):
                print(f'\nRegular polygon resonance {resonance}',flush=True)
                subprocess.run([sys.executable,'-B',str(STUDY/'experiments'/'phase1_regular.py'),
                                '--resonance',*map(str,resonance),'--tongues'],check=True)
    if args.scan:
        tests = STUDY/'experiments'/'test_phase1_repairs.py'
        subprocess.run([sys.executable, '-B', str(tests)], check=True, stderr=subprocess.STDOUT)
        print('Audit regression suite passed.', flush=True)
        scan_geometry()
    if args.figure:
        draw_hexagon()
        draw_square_tongues()


if __name__ == '__main__':
    main()
