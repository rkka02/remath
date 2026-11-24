"""Regression tests for the Phase 1 and Phase 2 referee counterexamples."""

import math
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from fractions import Fraction as Q
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import mpmath as mp
import numpy as np
from mpmath.ctx_iv import MPIntervalContext, ivmpf

from phase1_canonical import ChessMap, polygon
from phase1_coexistence import prescribed_wall
from phase1_measure import neutral_root
from phase1_multiple import (affine_edges, rational_rectangles, rectangle_on_edges,
                             sharp_polygon, show_interval)
from phase1_parity import column_height, normal_return
from phase1_pde import periodic_set, reflect, walk
from phase1_probe import (CirclePL, InsufficientResolution, SQUARE_SINGULAR,
                          UNRESOLVED, certify_rotation, chess, distinct, hexagon,
                          mp_value, rational, rational_degrees, regular_polygon, rotated_rectangle,
                          scan_geometry, square_tongue_labels)
from phase1_rectangle import boundary_map, primary_low_intervals, section_endpoint, section_tongue
from phase1_regular import grid_check, half_period_cells, has_centered_rectangle, resonance_window

SQUARE = [(0, 0), (1, 0), (1, 1), (0, 1)]
DOCS = Path(__file__).resolve().parents[1] / 'docs'


class LiftTests(unittest.TestCase):
    def test_lap_seam_at_95_digits(self):
        with mp.workdps(95):
            lift = CirclePL([0, Q(1, 2), 1], [0, Q(1, 4), 1], 1)
            delta = Q(1, 10**20)
            exact_x, exact_y = 1-delta, 1-3*delta/2
            self.assertEqual(lift(exact_x), exact_y)
            self.assertEqual(lift.inverse(exact_y), exact_x)
            x, y = 1-mp.mpf('1e-20'), 1-mp.mpf('1.5e-20')
            # The decimal x has already rounded once. Check the correct
            # branch exactly on that binary input and against the decimal.
            self.assertEqual(lift(x), mp_value(1-3*(1-rational(x))/2))
            self.assertLessEqual(abs(lift(x)-y), mp.eps)
            self.assertEqual(lift.inverse(y), x)
            self.assertEqual(lift.inverse(lift(x)), x)

    def test_negative_degree_and_large_exact_laps(self):
        lift = CirclePL([0, Q(1, 2), 1], [2, Q(7, 4), 1], -1)
        for lap in (-10**100, -1, 0, 10**100):
            delta = Q(1, 10**60)
            x, y = lap+1-delta, 1-lap+3*delta/2
            self.assertEqual(lift(x), y)
            self.assertEqual(lift.inverse(y), x)

    def test_near_identity_square_exact(self):
        delta = Q(1, 10**60)
        self.assertEqual(distinct([0, delta, 1], Q(1, 10**53)), [0, delta, 1])
        for tol in (0, Q(1, 10**53)):
            b = chess(SQUARE, 1+delta, tol)
            p, g = certify_rotation(b, 2)
            self.assertIsNone(p)
            self.assertLess(max(g.displacement(1)), 0)
            self.assertEqual(g.fixed_cells(1), ([], [], []))
            self.assertEqual(b.tol, 0)
        p, g = certify_rotation(chess(SQUARE, 1, delta), 2)
        self.assertEqual(p, 1)
        self.assertEqual(set(g.displacement(1)), {0})

    def test_near_identity_square_rounded(self):
        with mp.workdps(72):
            for s in (mp.mpf(1), 1+mp.mpf('1e-60'), mp.tan(mp.atan(1+mp.mpf('1e-60')))):
                with self.assertRaisesRegex(ValueError, 'input_radius'):
                    chess(SQUARE, s, input_radius=0)
                p, g = certify_rotation(chess(SQUARE, s, input_radius=mp.mpf('1e-53')), 2)
                self.assertEqual(p, UNRESOLVED)
                self.assertEqual(g.rotation_status(1), UNRESOLVED)
                self.assertEqual(g.fixed_cells(1), UNRESOLVED)
            # A resolved displacement of one sign still excludes the label.
            p, g = certify_rotation(chess(SQUARE, 1+mp.mpf('1e-20'), input_radius=Q(1, 10**60)), 2)
            self.assertIsNone(p)
            self.assertEqual(g.fixed_cells(1), ([], [], []))

    def test_low_precision_tangents_keep_their_original_uncertainty(self):
        with mp.workdps(15):
            square_s = mp.tan(mp.pi/4)
            twelve_s = mp.tan(mp.pi/3)
            old_vertices = regular_polygon(12, 0)
        with mp.workdps(72):
            iv = MPIntervalContext()
            iv.dps = mp.mp.dps
            twelve = regular_polygon(12, iv.mpf(0), iv)
            cases = ((SQUARE, square_s, iv.tan(iv.pi/4), 2),
                     (twelve, twelve_s, iv.tan(iv.pi/3), 3))
            for vertices, stale, enclosure, q in cases:
                with self.assertRaisesRegex(ValueError, 'input_radius'):
                    certify_rotation(chess(vertices, stale), q)
                self.assertLess(abs(enclosure-iv.mpf(stale)), iv.mpf('1e-15'))
                bounded = chess(vertices, stale, input_radius=Q(1, 10**15))
                self.assertEqual(certify_rotation(bounded, q)[0], UNRESOLVED)
                self.assertEqual(certify_rotation(chess(vertices, enclosure), q)[0], UNRESOLVED)
            with self.assertRaisesRegex(ValueError, 'input_radius'):
                chess(old_vertices, iv.tan(iv.pi/3))
            self.assertNotEqual(rational(square_s), 1)
            self.assertEqual(certify_rotation(chess(SQUARE, Q(1)), 2)[0], 1)

    def test_rational_degrees_preserves_binary64_and_interval_uncertainty(self):
        s = math.tan(math.pi/4)
        self.assertNotEqual(s, 1)
        with self.assertRaisesRegex(ValueError, 'input_radius'):
            rational_degrees(s, 0)
        with self.assertRaisesRegex(ValueError, 'input_radius'):
            rational_degrees(1, 0.0)
        self.assertEqual(certify_rotation(rational_degrees(s, 0, input_radius=Q(1, 10**15)), 2)[0],
                         UNRESOLVED)
        iv = MPIntervalContext()
        iv.dps = 72
        self.assertEqual(certify_rotation(rational_degrees(iv.tan(iv.pi/4), 0), 2)[0], UNRESOLVED)
        tilted = rational_degrees(1, iv.mpf(['0.19999', '0.20001']), R=iv.mpf(['0.9999', '1.0001']))
        for aspect in (Q(9999, 10000), Q(10001, 10000)):
            exact = rational_degrees(1, Q(20001, 100000), R=aspect)
            for x in tilted.x+exact.x:
                self.assertLessEqual(abs(tilted(x)-exact(x)), tilted.error)
        with self.assertRaisesRegex(ValueError, 'finite'):
            chess(SQUARE, iv.tan(iv.mpf([1, 2])))

    def test_polygon_constructors_and_centered_contact_keep_angle_provenance(self):
        with mp.workdps(15):
            quarter, half = mp.pi/4, mp.pi/2
        with mp.workdps(72):
            iv = MPIntervalContext()
            iv.dps = 80
            for n in (8, 16):
                with self.assertRaisesRegex(ValueError, 'input_radius'):
                    has_centered_rectangle(n, 0, quarter)
                self.assertEqual(has_centered_rectangle(n, 0, quarter, input_radius=Q(1, 10**15)),
                                 UNRESOLVED)
                self.assertEqual(has_centered_rectangle(n, 0, iv.pi/4), UNRESOLVED)
                with self.assertRaisesRegex(ValueError, 'input_radius'):
                    regular_polygon(n, quarter, iv)
            with self.assertRaisesRegex(ValueError, 'input_radius'):
                rotated_rectangle(half, 1, iv)
            with self.assertRaisesRegex(ValueError, 'input_radius'):
                rotated_rectangle(0, 1.0, iv)
            square = rotated_rectangle(half, 1, iv, input_radius=Q(1, 10**15))
            self.assertEqual(certify_rotation(chess(square, 1), 2)[0], UNRESOLVED)

    def test_scan_passes_actual_outward_vertex_and_slope_boxes(self):
        with mp.workdps(72), redirect_stdout(StringIO()):
            with patch('phase1_probe.chess', side_effect=StopIteration) as first_map:
                with self.assertRaises(StopIteration):
                    scan_geometry()
        points, slope = first_map.call_args.args
        iv = MPIntervalContext()
        iv.dps = 140
        expected = regular_polygon(3, iv.pi/36, iv)
        for box, refined in [(slope, iv.tan(iv.pi/480)),
                             *[(x, y) for p, r in zip(points, expected) for x, y in zip(p, r)]]:
            self.assertIsInstance(box, ivmpf)
            self.assertTrue(refined in box)
            self.assertTrue(box.a < box.b)

    def test_one_lap_lifts_compare_across_the_seam(self):
        eps = Q(1, 10**20)
        for degree in (-1, 1):
            family = CirclePL([0, 1], [mp.mpf(0), mp.mpf(degree)], degree, input_radius=eps)
            canonical = family.one_lap_lift()
            actual = CirclePL([0, 1], [-eps, degree-eps], degree).one_lap_lift()
            self.assertEqual((canonical(0), actual(0)), (0, 1-eps))
            aligned = actual.one_lap_lift(reference=canonical)
            tight = family.one_lap_lift(reference=canonical)
            self.assertEqual(tight.error, family.error)
            for t in (-2, 0, Q(1, 3), 1, 12):
                self.assertLessEqual(abs(canonical(t)-actual(t)), canonical.error)
                self.assertLessEqual(abs(canonical.inverse(t)-actual.inverse(t)), canonical.inverse_error)
                self.assertEqual(tight(t)-aligned(t), eps)
                self.assertLessEqual(abs(tight.inverse(t)-aligned.inverse(t)), tight.inverse_error)
        for shift in (-5, 0, 7):
            lifted = CirclePL([0, 1], [shift+Q(1, 3), shift+Q(4, 3)], 1)
            self.assertEqual(certify_rotation(lifted, 3)[0], 1)

    def test_rounded_tangent_is_unresolved(self):
        polygon = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        with mp.workdps(72):
            with self.assertRaisesRegex(InsufficientResolution, 'unresolved'):
                chess(polygon, 1+mp.mpf('1e-60'), mp.mpf('1e-53'))

    def test_propagated_bounds_cover_a_perturbed_polygon(self):
        with mp.workdps(72):
            coords = [(0, 0), (1, Q(1, 4)), (Q(3, 4), Q(5, 4)), (-Q(1, 4), 1)]
            centers = [(mp_value(Q(x)), mp_value(Q(z))) for x, z in coords]
            approx = chess(centers, mp.mpf(1), mp.mpf('1e-15')).power(3)
            delta = Q(1, 10**16)
            coords[2] = (Q(3, 4)+delta, Q(5, 4)-delta)
            actual = chess(coords, 1+delta).power(3)
            # Maximal differences of the two lifts occur on the union of
            # their breaks. Check both lifts and both cyclic knot sets.
            for t in set(actual.x+approx.x):
                self.assertLessEqual(abs(actual(t)-approx(t)), approx.error)
            for y in set(actual.y+approx.y):
                self.assertLessEqual(abs(actual.inverse(y)-approx.inverse(y)), approx.inverse_error)
            for source, target in ((actual, approx), (approx, actual)):
                for t in source.x:
                    distance = min(min(abs(t-u), source.period-abs(t-u)) for u in target.x)
                    self.assertLessEqual(distance, approx.knot_error)

    def test_strict_rotation_can_have_an_unresolved_fixed_cell(self):
        with mp.workdps(72):
            xs = [mp.mpf(j)/4 for j in range(5)]
            # Both displacement signs are robust. The mark at 1/2 can move
            # either way, so the full fixed-point census is undetermined.
            ys = [xs[0]+mp.mpf('.55'), xs[1]+mp.mpf('.45'), 1,
                  xs[3]+mp.mpf('.45'), xs[4]+mp.mpf('.55')]
            g = CirclePL(xs, ys, 1, input_radius=Q(1, 10**60))
            h = CirclePL([0, 1], [Q(1, 2), Q(3, 2)], 1).after(g)
            self.assertIs(h.rotation_status(1), True)
            self.assertEqual(h.fixed_cells(1), UNRESOLVED)


class PolygonTests(unittest.TestCase):
    def test_reflex_notch_intercepts_a_formal_four_edge_itinerary(self):
        vertices = [tuple(map(Q, point)) for point in
                    [(-6, 0), (0, -6), (7, 1), (1, 4), (0, 0), (-2, 4)]]
        candidate = rectangle_on_edges(affine_edges(vertices), (0, 1, 2, 5))
        self.assertEqual((candidate.left, candidate.right, candidate.lower, candidate.upper),
                         (-3, 3, -3, 3))
        self.assertTrue(all(0 < t < 1 for t in candidate.edge_fractions))
        self.assertEqual(candidate.multiplier_sw, Q(1, 2))
        hits = [u+(3-v)*(x-u)/(y-v) for (u, v), (x, y) in zip(vertices, vertices[1:]+vertices[:1])
                if min(v, y) < 3 < max(v, y)]
        self.assertEqual(max(x for x in hits if x < 3), Q(3, 4))
        with self.assertRaisesRegex(ValueError, 'convex'):
            rational_rectangles(vertices)

    def test_integer_projection_reflection_is_an_exact_involution(self):
        n = 10**20
        levels = (0, n, n-1, -1)
        other = reflect(levels, 2)
        self.assertIsInstance(other, Q)
        self.assertEqual(other, Q(n-1, n))
        self.assertEqual(reflect(levels, other), 2)

    def test_cut_diamond_has_only_fixed_periodic_points(self):
        half = Q(1, 2)
        poly = [(0, -1), (1, 0), (half, half), (-half, half), (-1, 0)]
        for s in (half, Q(99, 100), Q(101, 100), Q(2)):
            b = chess(poly, s)
            vertex = 0 if s < 1 else 1
            self.assertIn(vertex, b.support_vertices)
            self.assertEqual((b(vertex)-vertex) % 5, 0)
            dx = Q(1, 10**5)
            slopes = [(b(vertex+d)-b(vertex))/d for d in (-dx, dx)]
            self.assertLess(min(slopes), 1)
            self.assertGreater(max(slopes), 1)
            third = b.power(3)
            for turns in (1, 2):
                self.assertIs(third.rotation_status(turns), False)
        iv = MPIntervalContext()
        iv.dps = 72
        nearby = chess(poly, iv.mpf(['0.499999999999999', '0.500000000000001']))
        self.assertIn(0, nearby.support_vertices)
        self.assertLess(nearby.error, nearby.period)
        self.assertIs(nearby.power(2).rotation_status(1), False)

    def test_characteristic_hexagon_has_four_directed_cycles(self):
        half = Q(1, 2)
        vertices = sharp_polygon(2)[:-1] + [(half, half), (half, -half)]
        us, vs = zip(*vertices)
        word = [vs, us]
        _, fixed, neutral, rates = periodic_set(word*2)
        self.assertFalse(neutral)
        self.assertEqual(len(fixed), 8)
        cycles = {frozenset((t, walk(word, t))) for t in fixed}
        self.assertTrue(all(len(orbit) == 2 for orbit in cycles))
        self.assertEqual(len(cycles), 4)
        self.assertGreater(len(cycles), len(vertices)-3)
        self.assertEqual({rates[t] for t in fixed}, {Q(1, 3), 3, Q(3, 5), Q(5, 3)})
        for lo, hi, r in ((2, 89, 2), (4, 86, 4)):
            for u, v in ((lo, -r), (hi, -r), (hi, r), (lo, r)):
                # Verify the contacts on the original open, transverse edges.
                hits = [(a, b) for a, b in zip(vertices, vertices[1:]+vertices[:1])
                        if min(a[1], b[1]) < v < max(a[1], b[1]) and
                        (u-a[0])*(b[1]-a[1]) == (v-a[1])*(b[0]-a[0])]
                self.assertEqual(len(hits), 1)
                self.assertNotEqual(hits[0][0][0], hits[0][1][0])

    def test_nonregular_even_rectangle_has_no_two_cycle(self):
        g = rational_degrees(1, Q(1, 3), R=3).power(2)
        D = g.displacement(1)
        self.assertEqual((min(D), max(D)), (Q(5, 4), 2))
        self.assertEqual(g.fixed_cells(1), ([], [], []))
        for tilt in (Q(33, 100), Q(34, 100)):
            self.assertIsNone(certify_rotation(rational_degrees(1, tilt, R=3), 2)[0])

    def test_critical_diamond_removes_cyclic_interval_endpoints(self):
        levels = [tuple(map(Q, (0, 1, 1, 0))), tuple(map(Q, (0, 0, 1, 1)))]
        cuts, isolated, neutral, slopes = periodic_set(levels*2)
        self.assertEqual(cuts, list(range(5)))
        self.assertEqual(neutral, list(zip(range(4), range(1, 5))))
        self.assertEqual(isolated, [])
        self.assertEqual(slopes, {})

    def test_last_neutral_interval_owns_the_zero_vertex(self):
        vertices, _ = hexagon()
        xi, eta = zip(*(vertices[i] for i in (3, 2, 1, 0, 5, 4)))
        _, isolated, intervals, slopes = periodic_set([eta, xi]*2)
        self.assertEqual(intervals[-1][1], 6)
        self.assertGreater(intervals[0][0], 0)
        self.assertNotIn(0, isolated)
        self.assertEqual(set(isolated), set(slopes))
        self.assertEqual(len(isolated), 4)

    def test_rectangle_enumeration_in_both_windings(self):
        poly = sharp_polygon(2)
        expected = {(2, 89, -2, 2, Q(1, 3)), (4, 86, -4, 4, Q(3, 5))}
        for vertices in (poly, poly[::-1], poly[2:]+poly[:2]):
            actual = {(r.left, r.right, r.lower, r.upper, r.attracting_multiplier)
                      for r in rational_rectangles(vertices)}
            self.assertEqual(actual, expected)

    def test_rational_vertices_need_not_give_rational_angles(self):
        points = [((u-v)/2, (u+v)/2) for u, v in sharp_polygon(1)]
        slopes = [(w-z)/(y-x) if y != x else None
                  for (x, z), (y, w) in zip(points, points[1:]+points[:1])]
        self.assertIn({0, -3}, [{a, b} for a, b in zip(slopes, slopes[1:]+slopes[:1])])
        # If the angle were rational in pi, 2*cos(2*angle) would be an
        # algebraic integer. Here it is a nonintegral rational.
        self.assertEqual(2*Q(1-3**2, 1+3**2), Q(-8, 5))

    def test_chamfer_octagon_full_census(self):
        poly = [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]
        for s, q, factor in [(Q(3,5),3,Q(1,16)), (Q(7,18),4,Q(121,625)),
                             (Q(5,17),5,Q(36,121))]:
            p, g = certify_rotation(chess(poly, s), q)
            self.assertEqual(p, q-1)
            neutral, roots, vertices = g.fixed_cells(p)
            self.assertFalse(neutral or vertices)
            self.assertEqual(sorted(m for _, m in roots), [factor]*(2*q)+[1/factor]*(2*q))

    def test_vertex_only_maximum_is_visible_on_regular_ray(self):
        vertices, _ = hexagon()
        def profile(y):
            return 4*max(0, y-Q(3, 4))
        self.assertEqual({(u, v) for u, v in vertices if profile(abs(v)) == 1},
                         {(0, -1), (0, 1)})
        self.assertEqual(profile(1-abs(0))-profile(Q(1, 4)), 1)
        self.assertLess(-Q(3, 4), 0)
        self.assertGreater(Q(7, 12), 0)


class ParameterTests(unittest.TestCase):
    def test_odd_boundary_period_and_full_section_rotation(self):
        # At s=1/2, W=H=1 the right trapezoid's full section has zero
        # translation after the break involution, so F²(t)=t+1.
        s = Q(1, 2)
        delta = s-Q(1, 2)
        self.assertEqual(delta, 0)
        section = CirclePL([0, Q(7, 16), 1], [Q(7, 16), 1, Q(23, 16)], 1)
        self.assertEqual(set(section.power(2).displacement(1)), {0})
        tank = polygon(0, 0, Q(9, 8), Q(7, 8))
        self.assertEqual(ChessMap(tank, s).periodic_data(1, 3), (True, {}))

    def test_dirichlet_counterexamples_to_rational_local_slopes(self):
        p, g = certify_rotation(rational_degrees(1, Q(1, 2)), 2)
        neutral, roots, vertices = g.fixed_cells(p)
        self.assertFalse(neutral or vertices)
        self.assertEqual(sorted(m for _, m in roots), [Q(1, 81)]*2+[81]*2)
        # In Q(sqrt(2)), the coefficient pairs for a and b sum to (1,0).
        # This is exactly the k=1 global family tested above on rational data.
        a_coeffs, b_coeffs = (-1, 1), (2, -1)
        self.assertEqual(tuple(a+b for a, b in zip(a_coeffs, b_coeffs)), (1, 0))
        with mp.workdps(72):
            iv = MPIntervalContext()
            iv.dps = mp.mp.dps
            r = iv.sqrt(2)
            a, b = r-1, 2-r
            circle = boundary_map(b/a, a*b/(a+b))
            numerator, g = certify_rotation(circle, 3)
            self.assertEqual(numerator, UNRESOLVED)
            self.assertLess(max(map(abs, g.displacement(2))), Q(1, 10**60))

    def test_exact_integer_stretch(self):
        p, g = certify_rotation(boundary_map(2, 1), 3)
        self.assertEqual(p, 1)
        self.assertEqual(set(g.displacement(p)), {0})
        self.assertEqual(g.tol, 0)
        ends = section_tongue(1, 1, 2)
        self.assertEqual(ends, (Q(1, 3), Q(2, 3)))
        self.assertTrue(all(isinstance(x, Q) for x in ends))
        self.assertIsInstance(section_endpoint(Q(1), 2), Q)
        self.assertEqual(ends, section_tongue(1, 1, Q(2)))

    def test_high_period_kopecz_family(self):
        for k in (1, 2, 5, 9):
            a, b = Q(1, 3*k), Q(2, 3*k)
            self.assertEqual(k*(a+b), 1)
            circle = boundary_map(b/a, a*b/(a+b))
            p, g = certify_rotation(circle, 2*k+1)
            self.assertEqual(p, 2*k)
            self.assertEqual(set(g.displacement(p)), {0})

    def test_a_rational_label_persists_across_an_open_tongue(self):
        with mp.workdps(72):
            iv = MPIntervalContext()
            iv.dps = mp.mp.dps
            square = rotated_rectangle(iv.pi/12, 1, iv)
            for theta in (31, 40, 45, 58, 59):
                p, g = certify_rotation(chess(square, iv.tan(theta*iv.pi/180)), 2)
                self.assertEqual(p, 1)
                self.assertIs(g.rotation_status(p), True)

    def test_odd_boundary_label_isolated_and_self_reversing_section_orbit(self):
        lo, hi = section_tongue(2, 1, 2)
        self.assertEqual((lo, hi), (Q(2, 9), Q(2, 9)))
        for delta in (-Q(1, 10**30), 0, Q(1, 10**30)):
            label, _ = certify_rotation(boundary_map(2, lo+delta), 3)
            self.assertEqual(label, None if delta else 2)
        orbit = [Q(1, 3), Q(5, 3), Q(7, 6), Q(5, 6)]
        self.assertEqual([(column_height(y, Q(1, 3), Q(2, 3))-1) % 2 for y in orbit],
                         orbit[1:]+orbit[:1])
        self.assertEqual({-y % 2 for y in orbit}, set(orbit))
        self.assertEqual(sum(0 < y < 1 for y in orbit), 2)

    def test_checkerboard_floor_preserves_the_last_branch(self):
        with mp.workdps(95):
            d = mp.mpf('1e-20')
            for a, b in ((1, 2), (mp.mpf(1), mp.mpf(2))):
                self.assertEqual(normal_return(1-d, a, b), 1-d/2)
                self.assertLessEqual(abs(normal_return(-d, a, b)+d/2), mp.eps)
        d = Q(1, 10**100)
        self.assertEqual(normal_return(1-d, 1, 2), 1-d/2)

    def test_primary_interval_at_integer_aspect_and_tiny_tilt(self):
        with mp.workdps(95):
            phi = mp.mpf('1e-25')
            lo, hi = next(primary_low_intervals(phi, 1))
            center = mp.atan(mp.mpf(1)/3)
            self.assertLess(lo, center)
            self.assertLess(center, hi)
            a, b = mp.tan(lo-phi), mp.tan(lo+phi)
            self.assertLess(abs(a+2*b-1), 10*mp.eps)
            a, b = mp.tan(hi-phi), mp.tan(hi+phi)
            self.assertLess(abs(2*a+b-1), 10*mp.eps)

    def test_periodic_square_is_approached_by_irrational_rotations(self):
        self.assertEqual(set(chess(SQUARE, 1).power(2).displacement(1)), {0})
        # For s=1+sqrt(2)/d, rationalize rho=1/(1+s) as a+b*sqrt(2).
        for d in (10, 10**20, 10**60):
            a, b = Q(2*d*d, 4*d*d-2), Q(-d, 4*d*d-2)
            self.assertEqual((2*a+2*b/d, 2*b+a/d), (1, 0))
            self.assertNotEqual(b, 0)

    def test_normalized_inverse_design(self):
        a = Q(3, 4)
        for heights in ([0], [a], [Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 4)]):
            with self.assertRaises(AssertionError):
                prescribed_wall(heights, [Q(1, 2)]*len(heights), a)

    def test_axis_exchange_and_critical_tilt(self):
        with mp.workdps(72):
            phi = mp.pi/3
            reduced = mp.pi/2-phi
            self.assertLess(mp.cos(phi)-mp.sin(phi), 0)
            self.assertGreater(mp.cos(reduced)-mp.sin(reduced), 0)
            self.assertEqual(mp.pi/2-mp.pi/4, mp.pi/4)
        # At 45 degrees both characteristic coordinate projections are
        # constant on opposite whole walls. Every wall trace is constrained.
        xi, eta = (0, 2, 2, 0), (0, 0, 1, 1)
        self.assertTrue(all(xi[i] == xi[i-1] or eta[i] == eta[i-1] for i in range(4)))
        self.assertEqual(len(periodic_set([tuple(map(Q, xi)), tuple(map(Q, eta))]*2)[2]), 4)

    def test_l_triomino_separated_modes_have_zero_interior_trace(self):
        for m, n in ((1, 1), (2, 3), (17, 14)):
            for z in (Q(1, 4), Q(1, 2), Q(3, 4)):
                self.assertEqual(mp.sinpi(m)*mp.sinpi(n*mp_value(z)), 0)
        # A smooth bump around (1,1/2) with radius 1/4 lies strictly in
        # the lower 2-by-1 part of the L and equals exp(-1) at its center.
        x, z, r = Q(1), Q(1, 2), Q(1, 4)
        self.assertTrue(0 < x-r < x+r < 2 and 0 < z-r < z+r < 1)
        self.assertGreater(math.exp(-1), 0)

    def test_interval_rounding_straddles_last_displayed_digit(self):
        old = mp.iv.dps
        try:
            mp.iv.dps = 85
            mid = mp.iv.mpf('1.2345')
            narrow = mid+mp.iv.mpf(['-1e-75', '1e-75'])
            self.assertLess(narrow.delta, 1e-65)
            with self.assertRaisesRegex(ValueError, 'round differently'):
                show_interval(narrow, 4)
            self.assertEqual(show_interval(mp.iv.mpf(['1.2329', '1.2331']), 4), '1.233')
        finally:
            mp.iv.dps = old

    def test_reentry_requires_existence_and_interior_resolution(self):
        with mp.workdps(95):
            for r in (mp.mpf('.9'), mp.mpf(1)):
                with self.assertRaisesRegex(ValueError, 'R > tan'):
                    neutral_root(mp.pi/8, r, 1)
            phi = mp.radians(5)
            for n in (-1, 0):
                with self.assertRaisesRegex(ValueError, 'N >= 1'):
                    neutral_root(phi, 1, n)
            with self.assertRaisesRegex(ValueError, 'insufficient resolution'):
                neutral_root(phi, 1, 2000)
            distance = mp.pi/4-phi-neutral_root(phi, 1, 64)
            self.assertLess(abs(distance-mp.mpf('1.863394272244326344e-11')), mp.mpf('1e-29'))
            tiny_tilt = neutral_root(mp.mpf('1e-130'), 1, 2)
            self.assertLess(abs(tiny_tilt-mp.atan(mp.mpf(2)/3)), mp.mpf('1e-90'))

    def test_resonance_cli_distinguishes_candidate_and_tiny_tilt(self):
        program = Path(__file__).with_name('phase1_regular.py')
        def resonance(*args):
            return subprocess.run([sys.executable, '-B', str(program), '--resonance', *args],
                                  capture_output=True, text=True, check=True).stdout
        candidate = resonance('5', '1', '5', '--tongues')
        self.assertTrue(candidate.startswith('candidate period 5 '))
        self.assertIn('(0, 0, 0)', candidate)
        self.assertNotIn('grid cycle', candidate)
        square = resonance('4', '2', '1e-8')
        self.assertTrue(square.startswith('period 2 '))
        self.assertIn('(0, 4, 0)', square)
        rates = [Q(line.split()[-1]) for line in square.splitlines() if line.startswith('grid cycle')]
        self.assertEqual(len(rates), 2)
        self.assertLess(min(rates), Q(1, 10**39))
        self.assertLess(abs(rates[0]*rates[1]-1), Q(1, 10**52))
        tiny = resonance('8', '4', '1e-40', '--tongues')
        self.assertTrue(tiny.startswith('period 2 '))
        self.assertIn('(0, 12, 0)', tiny)
        self.assertEqual(tiny.count('grid cycle'), 6)
        endpoint_line = next(line for line in tiny.splitlines() if line.startswith('tongue within'))
        left, right = map(Q, endpoint_line.split()[-2:])
        self.assertEqual((45-left, right-45), (Q(1, 10**40),)*2)
        self.assertEqual(Q(tiny.splitlines()[-1].split()[-1]), Q(2, 10**40))

    def test_bisection_resolves_each_tiny_endpoint_at_120_digits(self):
        with mp.workdps(120):
            phi = mp.radians(mp.mpf('1e-40'))
            left, right = resonance_window(8, 4, phi)
            for end, expected in ((left, mp.pi/4-phi), (right, mp.pi/4+phi)):
                self.assertLess(abs(end-expected), phi*mp.mpf('1e-18'))

    def test_grid_midpoint_multipliers_and_uncertain_phase(self):
        with mp.workdps(72):
            iv = MPIntervalContext()
            iv.dps = 72
            q, rates, census = grid_check(6, 3, iv.mpf(['-1e-15', '1e-15']), True)
            self.assertEqual(q, 2)
            self.assertEqual(census, (0, 8, 0))
            self.assertEqual(sum(m < 1 for m in rates.values()), 2)
            with self.assertRaises(InsufficientResolution):
                resonance_window(4, 2, iv.pi*iv.mpf([1, 4])/180)
            cells_sq, isolated, uncertain = half_period_cells(4, iv.pi/36)
            self.assertEqual(len(cells_sq), 1)
            self.assertEqual(isolated, [])
            self.assertEqual(len(uncertain), 2)
            for u in uncertain:
                self.assertTrue(hasattr(u, "_mpi_") and u.delta < iv.mpf('1e-68'))

    def test_square_plot_all_critical_lines_and_primary_endpoints(self):
        tilt, angle = np.arange(1, 900, 2), np.arange(1, 1800, 2)
        phi, theta = np.meshgrid(tilt, angle)
        labels = square_tongue_labels(tilt, angle)
        critical = (theta == phi) | (theta+phi == 1800)
        interior = (theta > phi) & (theta+phi < 1800)
        primary_edges = interior & ((theta+phi == 900) | (theta-phi == 900))
        self.assertEqual(np.count_nonzero(critical), 900)
        self.assertEqual(np.count_nonzero(primary_edges), 450)
        np.testing.assert_array_equal(labels == SQUARE_SINGULAR, critical | primary_edges)
        np.testing.assert_array_equal(labels == 2, interior & (theta-phi < 900) & (theta+phi > 900))
        row, col = 231, 218  # (phi,theta) = (21.85,23.15) degrees
        self.assertEqual(labels[row, col], SQUARE_SINGULAR)
        self.assertEqual(labels[row+1, col], 2)


class ManuscriptTests(unittest.TestCase):
    def test_itinerary_visibility_and_boundary_parity_are_stated(self):
        overview = (DOCS/'phase1_scouting.md').read_text()
        self.assertIn(r'Exact finite-\(q\) test for any convex polygon', overview)
        self.assertRegex(overview, r'nonconvex polygon[^.]*every proposed chord[^.]*first-hit')
        self.assertRegex(overview, r'interior rational label with even denominator[^.]*open tongue')
        self.assertRegex(overview, r'odd-denominator label[^.]*single angle')
        self.assertRegex(overview, r'orbit and its reversal are distinct[^.]*interlace')
        self.assertRegex(overview, r'equal its own reversal\.[^.]*pairs[^.]*each semicircle')

    def test_reduced_tilt_precedes_both_canonical_formulas(self):
        paragraphs = (DOCS/'phase1_canonical.md').read_text().split('\n\n')
        for formula in (r'\cot(2\phi)\le R\le\tan(2\phi)', r'\cos\phi-\sin\phi'):
            paragraph, = (p for p in paragraphs if formula in p)
            self.assertIn(r'0<\phi<\pi/4', paragraph.split(formula)[0])

    def test_examples_specify_rational_vertices(self):
        for path in DOCS.glob('phase1_*.md'):
            with self.subTest(chapter=path.name):
                self.assertNotRegex(path.read_text().lower(), r'\brational (?:hexagon|octagon|polygon)s?\b')
        for name, shape in (('coexistence', 'hexagon'), ('central_bounds', 'octagon'),
                            ('rigidity', 'octagon')):
            self.assertIn(f'{shape} with rational vertices', (DOCS/f'phase1_{name}.md').read_text())

    def test_prior_work_specifies_the_square_and_both_unbounded_families(self):
        overview = (DOCS/'phase1_scouting.md').read_text()
        self.assertRegex(overview, r'For the square, [^.]*Theorem 13[^.]*open dense subset')
        parity = (DOCS/'phase1_parity.md').read_text()
        self.assertRegex(parity, r'Bajars, Frank and Maas[^.]*unbounded winding families[^.]*'
                                 r'\(2k,1\)[^.]*\(1,2k\)[^.]*§2\.4')

    def test_final_audit_regressions(self):
        from phase1_measure import strip_coordinate
        from phase1_parity import section_coordinate
        from phase1_regular import degree_interval
        with self.assertRaises(TypeError):
            ChessMap(polygon(0, 0, 1, 1), math.nextafter(1.0, 0.0))
        cm = ChessMap(polygon(0, 0, 1, 1), Q.from_float(math.nextafter(1.0, 0.0)))
        self.assertEqual(cm.periodic_data(1, 2), (False, {}))
        with self.assertRaises(TypeError):
            cm.forward(0.1)
        with self.assertRaises(TypeError):
            reflect([0.0, 1.0, 2.0, 1.0], 0.5)
        self.assertEqual(reflect(np.array([0, 1, 2, 1], dtype=np.int64), Q(1, 3)), Q(11, 3))
        big = 10**20
        verts = [(0, 0), (4*big+2, -4*big-2), (8*big+5, 1), (4*big+1, 4*big+1)]
        rec = rectangle_on_edges(affine_edges(verts), (0, 1, 2, 3))
        self.assertIsNotNone(rec)
        self.assertEqual(rec.attracting_multiplier, Q(big, big+1))
        big10 = np.int64(10**10)
        verts_np = [(np.int64(0), np.int64(0)), (4*big10+2, -4*big10-2),
                    (8*big10+5, np.int64(1)), (4*big10+1, 4*big10+1)]
        rec_np = rectangle_on_edges(affine_edges(verts_np), (0, 1, 2, 3))
        self.assertIsNotNone(rec_np)
        self.assertEqual(rec_np.attracting_multiplier, Q(10**10, 10**10 + 1))
        with self.assertRaises(TypeError):
            rational_rectangles([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)])
        self.assertEqual(column_height(big, 2, 3), big + Q(7, 3))
        self.assertEqual(section_coordinate(big+1, 2, 3), Q(big, 2) + Q(2, 5))
        with mp.workdps(95):
            sc = strip_coordinate(-big-1, mp.mpf(2), mp.mpf(3))
            self.assertLess(abs(sc - (-mp.mpf(big)/2 - mp.mpf(2)/5)), mp.mpf('1e-70'))
            sc_huge = strip_coordinate(-2**319 - 1, mp.mpf(2), mp.mpf(3))
            with mp.workdps(120):
                exact_huge = -mp.mpf(2**318) - mp.mpf(2)/5
            self.assertEqual(sc_huge, +exact_huge)
        with mp.workdps(75):
            iv = MPIntervalContext()
            iv.dps = 83
            with self.assertRaises(InsufficientResolution):
                half_period_cells(4, iv.mpf([4.99, 5.01]) * iv.pi / 180)
            with self.assertRaises(InsufficientResolution):
                d = iv.mpf('1e-68') * iv.pi / 180
                base = iv.mpf(5) * iv.pi / 180
                half_period_cells(4, iv.mpf([base.a - d.b, base.b + d.b]))
            cells, iso, unres = half_period_cells(4, degree_interval(Q(1, 10**40)))
            self.assertEqual((len(cells), len(iso)), (1, 0))
            self.assertEqual(len(unres), 2)
            for u in unres:
                self.assertTrue(hasattr(u, "_mpi_") and u.delta < mp.mpf('1e-68'))
            width_deg = (cells[0][1] - cells[0][0]) * 180 / mp.pi
            self.assertLess(abs(width_deg - mp.mpf('2e-40')), mp.mpf('1e-55'))

    def test_referee_r1_b30_b31_regressions(self):
        from phase1_measure import strip_coordinate
        from phase1_regular import degree_interval
        from phase1_probe import chess
        # B30a: Fraction wrapping np.int64 at public entry points
        big10 = np.int64(10**10)
        verts_frac_np = [(Q(np.int64(0)), Q(np.int64(0))), (Q(4*big10+2), Q(-4*big10-2)),
                         (Q(8*big10+5), Q(np.int64(1))), (Q(4*big10+1), Q(4*big10+1))]
        recs = rational_rectangles(verts_frac_np)
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0].attracting_multiplier, Q(10**10, 10**10 + 1))
        sq_np = [(Q(np.int64(x)), Q(np.int64(z))) for x, z in ((0, 0), (1, 0), (1, 1), (0, 1))]
        self.assertEqual(chess(sq_np, Q(np.int64(1))).power(2).rotation_status(1), True)
        with mp.workdps(75):
            di = degree_interval(Q(np.int64(5), np.int64(1)))
            self.assertGreater(di, 0)
        # B30b: Unsigned tick dtypes must not wrap on theta - phi
        for dt in (np.uint16, np.uint64):
            lbl = square_tongue_labels(np.array([301], dtype=dt), np.array([101], dtype=dt))
            self.assertEqual(int(lbl[0, 0]), 1)
        # B31a: Tiny negative mpf & huge int vs Fraction consistency in strip_coordinate
        with mp.workdps(95):
            tiny = strip_coordinate(-mp.mpf('1e-160'), 2, 3)
            self.assertLess(abs(tiny - (-mp.mpf('4e-161'))), mp.mpf('1e-250'))
            huge_y = (1 << 501) + (1 << 182) + 1
            self.assertEqual(strip_coordinate(huge_y, 2, 3), strip_coordinate(Q(huge_y, 1), 2, 3))
            # Exact value 2^500 + 2^181 + 3/5 rounds to 2^500 + 2^182 at 95 dps (319 bits)
            expected_huge = mp.mpf((1 << 500) + (1 << 182))
            self.assertEqual(strip_coordinate(huge_y, 2, 3), expected_huge)
        # B31b: Narrow 5° ± 10^{-73}° enclosure at 75 dps must raise InsufficientResolution
        with mp.workdps(75):
            iv = MPIntervalContext()
            iv.dps = 75
            base = iv.mpf(5) * iv.pi / 180
            d = iv.mpf('1e-73') * iv.pi / 180
            with self.assertRaises(InsufficientResolution):
                half_period_cells(4, iv.mpf([base.a - d.b, base.b + d.b]))
        overview = (DOCS/'phase1_scouting.md').read_text()
        self.assertIn('preserves the exact disk eigenfrequency', overview)
        self.assertIn('rational boundary rotation', overview)
        primary = (DOCS.parent/'sources'/'PRIMARY_SOURCES.md').read_text()
        self.assertIn('Aleksandryan', primary)
        self.assertIn(r'|\log\alpha_\kappa(\lambda)| < \sqrt{3}\pi', primary)

    def test_referee_r2_regressions(self):
        from phase1_measure import strip_coordinate, strip_position
        from phase1_parity import column_height, section_coordinate
        from phase1_regular import degree_interval, wall_correction
        from phase1_rectangle import section_endpoint
        # 1. strip_coordinate float/str exact consistency at 95 dps
        with mp.workdps(95):
            b = (1 << 320) - 2
            ref = strip_coordinate(1, 1, b)
            self.assertEqual(strip_coordinate(1.0, 1, b), ref)
            self.assertEqual(strip_coordinate("1", 1, b), ref)
            self.assertLess(ref, mp.mpf(1))
            # 2. strip_position exact huge row without low-bit loss
            pos = strip_position(1 << 321, 48, 96)
            self.assertEqual(pos, mp.mpf((1 << 321) + 64))
        # 3. half_period_cells rejects coarse 10-digit interval at 75 working digits
        with mp.workdps(75):
            iv10 = MPIntervalContext()
            iv10.dps = 10
            lo = Q(1, 16)
            hi = Q(1, 16) + Q(1, 1 << 40)
            with self.assertRaises(InsufficientResolution):
                half_period_cells(4, iv10.mpf([float(lo), float(hi)]))
            # 4a. Even near-coincident events: 22.5° + 10^-68° must not falsely claim 22.5° inside cell
            phi_sq = degree_interval(Q(45, 2) + Q(1, 10**68))
            cells, iso, unres = half_period_cells(4, phi_sq)
            self.assertEqual(len(cells), 1)
            self.assertGreater(cells[0][0] * 180 / mp.pi, mp.mpf('22.5'))
            self.assertGreaterEqual(len(unres), 1)
            # 4b. Odd near-coincident events: pentagon 9° + 10^-40° cannot falsely vanish at 75 dps,
            #     and resolves its exact open cell at 150 dps; 9° + 10^-72° reports an outward cluster interval.
            phi_p5 = degree_interval(Q(9) + Q(1, 10**40))
            with self.assertRaises(InsufficientResolution):
                half_period_cells(5, phi_p5)
            phi_p5_tiny = degree_interval(Q(9) + Q(1, 10**72))
            cells5_t, iso5_t, unres5_t = half_period_cells(5, phi_p5_tiny)
            self.assertTrue(any(hasattr(u, "delta") and u.delta > 0 for u in unres5_t))
            # 5. wall_correction stable at N = 10^50 + 2 at 75 digits
            n_big = 10**50 + 2
            rel_e, _ = wall_correction(n_big)
            scaled = mp.mpf(n_big)**3 * rel_e
            target = mp.mpf(4)/15 * mp.pi**4 + mp.mpf(2)/3 * mp.pi**2
            self.assertLess(abs(scaled - target), mp.mpf('1e-40'))
        with mp.workdps(150):
            phi_p5_150 = degree_interval(Q(9) + Q(1, 10**40))
            cells5, iso5, unres5 = half_period_cells(5, phi_p5_150)
            self.assertEqual(len(cells5), 1)
            lo5_deg = cells5[0][0] * 180 / mp.pi
            hi5_deg = cells5[0][1] * 180 / mp.pi
            self.assertLess(abs(lo5_deg - (45 - mp.mpf('1e-40'))), mp.mpf('1e-55'))
            self.assertLess(abs(hi5_deg - (45 + mp.mpf('1.60357456590997e-41'))), mp.mpf('1e-52'))
        # 6. NumPy-backed Fraction inputs in column_height, section_coordinate, section_endpoint
        y_np = Q(np.int64((1 << 62) + 1), np.int64(1))
        a_np = Q(np.int64(2), np.int64(1))
        b_np = Q(np.int64(3), np.int64(1))
        self.assertEqual(column_height(y_np, a_np, b_np), Q(9223372036854775815, 2))
        self.assertEqual(section_coordinate(y_np, a_np, b_np), Q(11529215046068469762, 5))
        self.assertEqual(
            section_endpoint(Q(2, 3), Q(np.int64(10**10))),
            Q(10**10, 200000000030000000001),
        )

    def test_referee_r3_regressions(self):
        from phase1_measure import strip_coordinate, strip_position
        from phase1_regular import degree_interval, wall_correction
        from phase1_rectangle import section_tongue
        # 1. Cloned-context mpf and singleton ivmpf in strip_coordinate / strip_position
        with mp.workdps(95):
            one_clone = mp.mp.clone().mpf(1)
            one_iv = mp.iv.mpf(1)
            b_big = (1 << 320) - 2
            ref_c = strip_coordinate(1, 1, b_big)
            self.assertEqual(strip_coordinate(one_clone, 1, b_big), ref_c)
            self.assertEqual(strip_coordinate(one_iv, 1, b_big), ref_c)
            a_tiny = Q(1, 1 << 319) + Q(1, 1 << 700)
            expected_pos = mp.mpf(1) + mp.mpf(2) ** (-318)
            self.assertEqual(strip_position(one_clone, a_tiny, a_tiny), expected_pos)
            self.assertEqual(strip_position(one_iv, a_tiny, a_tiny), expected_pos)
        # 2. half_period_cells huge exact phase, narrow 100-dps interval, and 10^-69 / 10^-74 cases
        with mp.workdps(75):
            # 2a. Exact square phase 2**253 + 1 radians must match (31.59402542°, 58.40597458°)
            cells_big, iso_big, unres_big = half_period_cells(4, (1 << 253) + 1)
            self.assertEqual(len(cells_big), 1)
            lo_deg = cells_big[0][0] * 180 / mp.pi
            hi_deg = cells_big[0][1] * 180 / mp.pi
            self.assertLess(abs(lo_deg - mp.mpf('31.59402542')), mp.mpf('1e-7'))
            self.assertLess(abs(hi_deg - mp.mpf('58.40597458')), mp.mpf('1e-7'))
            self.assertLess(hi_deg, mp.mpf(60))
            # 2b. Narrow 100-digit interval [3/8, 3/8 + 2^-251] must raise InsufficientResolution
            iv100 = MPIntervalContext()
            iv100.dps = 100
            lo100 = iv100.mpf(3) / 8
            hi100 = lo100 + iv100.mpf(2) ** (-251)
            with self.assertRaises(InsufficientResolution):
                half_period_cells(4, iv100.mpf([lo100.a, hi100.b]))
            # 2c. Square 22.5° + 10^-69° must NOT include 22.5° + 0.9999995e-69° inside cell
            phi_sq69 = degree_interval(Q(45, 2) + Q(1, 10**69))
            cells69, _, unres69 = half_period_cells(4, phi_sq69)
            self.assertEqual(len(cells69), 1)
            with mp.workdps(120):
                probe69 = (mp.mpf('22.5') + mp.mpf('0.9999995e-69')) * mp.pi / 180
                self.assertGreater(mp.mpf(cells69[0][0]), probe69)
                self.assertTrue(any(mp.mpf(u._mpi_[0]) <= probe69 <= mp.mpf(u._mpi_[1]) for u in unres69 if hasattr(u, "_mpi_")))
            # 2d. Pentagon 9° + 10^-74° must cover 45° - 0.96e-74° in unresolved outward band
            phi_p74 = degree_interval(Q(9) + Q(1, 10**74))
            cells74, _, unres74 = half_period_cells(5, phi_p74)
            with mp.workdps(120):
                probe74 = (mp.mpf('45') - mp.mpf('0.96e-74')) * mp.pi / 180
                in_cells = any(mp.mpf(a) < probe74 < mp.mpf(b) for a, b in cells74)
                in_unres = any(mp.mpf(u._mpi_[0]) <= probe74 <= mp.mpf(u._mpi_[1]) for u in unres74 if hasattr(u, "_mpi_"))
                self.assertTrue(in_cells or in_unres)
            # 3. wall_correction accepts np.int64 and section_tongue rejects non-integer Fraction winding
            rel_np, bound_np = wall_correction(np.int64(1002))
            rel_py, bound_py = wall_correction(1002)
            self.assertEqual(rel_np, rel_py)
            self.assertEqual(bound_np, bound_py)
        with self.assertRaises(TypeError):
            section_tongue(Q(3, 2), 1, Q(2))

    def test_referee_r4_regressions(self):
        from phase1_measure import strip_coordinate, strip_position
        from phase1_regular import degree_interval
        # 1a. 75-digit interval [3/8, 3/8 + 2^-251] must raise InsufficientResolution
        with mp.workdps(75):
            iv75 = MPIntervalContext()
            iv75.dps = 75
            lo75 = iv75.mpf(3) / 8
            hi75 = lo75 + iv75.mpf(2) ** (-251)
            with self.assertRaises(InsufficientResolution):
                half_period_cells(4, iv75.mpf([lo75.a, hi75.b]))
            # 1b. Exact square Fraction(1, 10**90) and 10**-200 must enclose pi/4 + phi/2 in unresolved
            for exp_n in (90, 200):
                phi_tiny = Q(1, 10**exp_n)
                cells_t, _, unres_t = half_period_cells(4, phi_tiny)
                with mp.workdps(250):
                    probe = mp.pi / 4 + mp.mpf(1) / (2 * mp.mpf(10)**exp_n)
                    in_c = any(mp.mpf(a) < probe < mp.mpf(b) for a, b in cells_t)
                    in_u = any(mp.mpf(u._mpi_[0]) <= probe <= mp.mpf(u._mpi_[1]) for u in unres_t if hasattr(u, "_mpi_"))
                    self.assertTrue(in_c or in_u)
            # 1c. Pentagon 9° + 10^-82° must enclose 45° - 0.5e-82° in unresolved
            phi_p82 = degree_interval(Q(9) + Q(1, 10**82))
            cells82, _, unres82 = half_period_cells(5, phi_p82)
            with mp.workdps(150):
                probe82 = (mp.mpf(45) - mp.mpf('0.5e-82')) * mp.pi / 180
                in_c = any(mp.mpf(a) < probe82 < mp.mpf(b) for a, b in cells82)
                in_u = any(mp.mpf(u._mpi_[0]) <= probe82 <= mp.mpf(u._mpi_[1]) for u in unres82 if hasattr(u, "_mpi_"))
                self.assertTrue(in_c or in_u)
        # 2. Lazy mpmath constant mp.pi in strip_position and strip_coordinate at 95 digits
        with mp.workdps(95):
            q_pi = mp.mpf(mp.pi)
            res_pos = strip_position(-q_pi, mp.pi, mp.pi)
            res_coord = strip_coordinate(1, mp.pi, 3)
            with mp.workdps(260):
                true_pos = mp.pi - mp.mpf(q_pi)
                true_coord = mp.mpf(3) / (mp.pi + 3)
            self.assertEqual(res_pos, +true_pos)
            self.assertEqual(res_coord, +true_coord)
            self.assertLess(res_pos, 0)

    def test_referee_r5_regressions(self):
        from phase1_measure import strip_coordinate, strip_position
        # 1a. Exact square phase phi = 1/2 at 75 dps: trimmed boundary 1/2 + 2^-252 must lie in unresolved
        with mp.workdps(75):
            cells_h, iso_h, unres_h = half_period_cells(4, Q(1, 2))
            self.assertEqual((len(cells_h), len(iso_h)), (1, 0))
            with mp.workdps(150):
                for probe_h in (mp.mpf('0.5'), mp.mpf('0.5') + mp.mpf(2)**(-253), mp.mpf('0.5') + mp.mpf(2)**(-252)):
                    in_c = any(mp.mpf(a) < probe_h < mp.mpf(b) for a, b in cells_h)
                    in_u = any(mp.mpf(u._mpi_[0]) <= probe_h <= mp.mpf(u._mpi_[1]) for u in unres_h if hasattr(u, "_mpi_"))
                    self.assertTrue(in_c or in_u, f"probe {probe_h} omitted at phi=1/2")
            # 1b. Accepted 75-dps interval [3/8, 3/8 + 2^-252]: pi/4 - 3/8 - 2^-253 must lie in unresolved
            iv75 = MPIntervalContext()
            iv75.dps = 75
            lo_iv = iv75.mpf(3) / 8
            hi_iv = lo_iv + iv75.mpf(2)**(-252)
            cells_i, iso_i, unres_i = half_period_cells(4, iv75.mpf([lo_iv.a, hi_iv.b]))
            self.assertEqual((len(cells_i), len(iso_i)), (1, 0))
            with mp.workdps(150):
                probe_i = mp.pi / 4 - mp.mpf(3) / 8 - mp.mpf(2)**(-253)
                in_c = any(mp.mpf(a) < probe_i < mp.mpf(b) for a, b in cells_i)
                in_u = any(mp.mpf(u._mpi_[0]) <= probe_i <= mp.mpf(u._mpi_[1]) for u in unres_i if hasattr(u, "_mpi_"))
                self.assertFalse(in_c)
                self.assertTrue(in_u)
        # 2a. Equal-slope exact halfway tie in strip_coordinate (ties-to-even)
        with mp.workdps(95):
            y_tie = Q(1, 2) + Q(15, 1 << 320)
            expected_tie = mp.mpf(1)/4 + mp.mpf(8) * mp.mpf(2)**(-320)
            self.assertEqual(strip_coordinate(y_tie, mp.pi, mp.pi), expected_tie)
            c15 = mp.mp.clone()
            c15.dps = 15
            self.assertEqual(strip_coordinate(y_tie, mp.pi, c15.pi), expected_tie)
            # 2b. Exact-zero exit in strip_position
            self.assertEqual(strip_position(-Q(1, 3), mp.pi, Q(1, 3)), mp.mpf(0))
            # 3. Cloned 15-digit context lazy constants (e, phi, euler, pi, ln2, catalan)
            for cname in ("e", "phi", "euler", "pi", "ln2", "catalan"):
                const_c = getattr(c15, cname)
                const_m = getattr(mp, cname)
                got = strip_coordinate(1, const_c, 3)
                with mp.workdps(260):
                    true_val = mp.mpf(3) / (mp.mpmathify(const_m) + 3)
                self.assertEqual(got, +true_val, f"cloned context {cname} lost precision")
            # 4. Non-singleton interval input with unambiguous rounded output (and wide interval rejection)
            iv150 = MPIntervalContext()
            iv150.dps = 150
            y_lo = iv150.mpf(1) / 4
            y_hi = y_lo + iv150.mpf(2)**(-400)
            y_box = iv150.mpf([y_lo.a, y_hi.b])
            self.assertEqual(strip_coordinate(y_box, 1, 1), mp.mpf('0.125'))
            self.assertEqual(strip_position(y_box, 1, 1), mp.mpf('1.25'))
            # Interval straddling integer boundary 1 with unambiguous output
            y_straddle = iv150.mpf([(iv150.mpf(1) - iv150.mpf(2)**(-400)).a, (iv150.mpf(1) + iv150.mpf(2)**(-400)).b])
            self.assertEqual(strip_coordinate(y_straddle, 1, 3), mp.mpf('0.75'))
            # Wide non-singleton interval must raise ValueError rather than misrounding
            with self.assertRaises(ValueError):
                strip_coordinate(iv150.mpf(['0.1', '0.9']), 1, 1)
            with self.assertRaises(ValueError):
                strip_position(iv150.mpf(['0.1', '0.9']), 1, 1)

    def test_referee_r6_regressions(self):
        from mpmath.rational import mpq
        from phase1_measure import strip_coordinate, strip_position
        # 1. half_period_cells(4, mp.e) must not freeze mp.e at 75 digits
        with mp.workdps(75):
            cells_e, iso_e, unres_e = half_period_cells(4, mp.e)
            self.assertEqual((len(cells_e), len(iso_e)), (1, 0))
            with mp.workdps(200):
                theta_floor = mp.floor(mp.mpf(2)**253 * (mp.pi - mp.e)) * mp.mpf(2)**(-253)
                # Exact lower edge is pi - e > theta_floor, so theta_floor must NOT lie inside open cell.
                self.assertGreater(mp.mpf(cells_e[0][0]), mp.pi - mp.e)
                self.assertFalse(any(mp.mpf(a) < theta_floor < mp.mpf(b) for a, b in cells_e))
                self.assertTrue(any(mp.mpf(u._mpi_[0]) <= theta_floor <= mp.mpf(u._mpi_[1]) for u in unres_e))
            # Cloned 15-digit context c.e also resolves at full precision
            c15 = mp.mp.clone()
            c15.dps = 15
            cells_ce, _, unres_ce = half_period_cells(4, c15.e)
            self.assertEqual(cells_ce, cells_e)
            # mpq phase accepted exactly
            cells_q, _, _ = half_period_cells(4, mpq(1, 2))
            cells_f, _, _ = half_period_cells(4, Q(1, 2))
            self.assertEqual(cells_q, cells_f)
        # 2-5. Strip helpers at 95 digits
        with mp.workdps(95):
            # 2. mp.eps and cloned c.eps keep their exact context epsilon values
            self.assertEqual(strip_position(mp.eps, 1, 1), mp.mpf(1) + mp.mpf(2)**(-318))
            c15 = mp.mp.clone()
            c15.dps = 15
            self.assertEqual(strip_position(-Q(1, 1 << 52), c15.eps, c15.eps), mp.mpf(0))
            # 3. mpmath.rational.mpq is treated as an exact rational (exact zero exit)
            s_third = Q(1, 3)
            self.assertEqual(strip_position(mpq(-1, 3), s_third, s_third), mp.mpf(0))
            self.assertEqual(strip_coordinate(mpq(1, 3), mpq(1, 3), mpq(1, 3)), mp.mpf(1) / 6)
            # 4. Arbitrary callables are rejected instead of using an uncertified error heuristic
            with self.assertRaises(TypeError):
                strip_position(lambda: (mp.mpf(2)**1000 + 1) - mp.mpf(2)**1000, 1, 1)
            with self.assertRaises(TypeError):
                strip_coordinate(lambda: mp.mpf(1), 1, 1)
            # 5. Refinable lazy constant near a high-precision tie must refine instead of exiting early
            with mp.workdps(300):
                q_ln2 = Q(int(mp.floor(mp.mpf(2)**800 * mp.ln2)), 1 << 800)
            s_tie = 1 + Q(1, 1 << 319) - q_ln2
            t_tie = Q(1, 2) + Q(1, 1 << 320)
            self.assertEqual(strip_position(mp.ln2, s_tie, s_tie), mp.mpf(1) + mp.mpf(2)**(-318))
            self.assertEqual(strip_coordinate(mp.ln2, q_ln2 - t_tie, t_tie), mp.mpf(1)/2 + mp.mpf(2)**(-319))

    def test_referee_r7_regressions(self):
        import subprocess
        import sys
        from decimal import Decimal
        from phase1_measure import (circle_distance, involution, parameters,
                                    strip_coordinate, strip_position)
        from phase1_regular import corner_widths, quadratic_roots
        # 1. High-bit (170,000-bit) ln2 near-tie resolves cleanly in both strip helpers
        with mp.workdps(95):
            with mp.workprec(170600):
                q_hi = Q(int(mp.floor(mp.mpf(2)**170000 * mp.ln2)), 1 << 170000)
            s_hi = 1 + Q(1, 1 << 319) - q_hi
            t_hi = Q(1, 2) + Q(1, 1 << 320)
            self.assertEqual(strip_position(mp.ln2, s_hi, s_hi), mp.mpf(1) + mp.mpf(2)**(-318))
            self.assertEqual(strip_coordinate(mp.ln2, q_hi - t_hi, t_hi), mp.mpf(1)/2 + mp.mpf(2)**(-319))
            # 2. Exact rational slope ratio mp.degree / mp.pi = 1/180 resolves exact ties-to-even
            y_deg = Q(181, 180) * t_hi
            self.assertEqual(strip_coordinate(y_deg, mp.degree, mp.pi), mp.mpf('0.5'))
            # 3. Near-pole parameters(theta, phi, aspect) keeps positive tangent and real square roots
            m_half_pi = mp.pi / 2
            th = mp.mpf(3) / 2
            ph = m_half_pi - th - mp.mpf(2)**(-320)
            a_p, b_p, r_p, x_p = parameters(th, ph, 1)
            self.assertGreater(a_p, 0)
            self.assertGreater(b_p, mp.mpf('2e96'))
            self.assertIsInstance(r_p, mp.mpf)
            self.assertIsInstance(x_p, mp.mpf)
            self.assertGreater(r_p, 0)
            self.assertGreater(x_p, 0)
            # 4. Exact involution near breakpoint m and circle_distance on huge mpf
            t_inv = mp.mpf(1) - mp.mpf(2)**(-319)
            r_inv = mp.mpf(3) * mp.mpf(2)**(-161)
            got_inv = involution(t_inv, r_inv)
            self.assertLess(abs(got_inv - (mp.mpf(1) + mp.mpf(1)/9)), mp.mpf('1e-90'))
            self.assertEqual(circle_distance(mp.mpf(2**400), mp.mpf(1)/4), mp.mpf('0.25'))
            # 5. Unsupported NumPy complex raises TypeError (not ValueError)
            for fn in (strip_position, strip_coordinate):
                with self.assertRaises(TypeError):
                    fn(np.complex128(1 + 2j), 1, 1)
            # Portable NumPy float exactness check (np.float64 and np.longdouble)
            for dt in (np.float64, np.longdouble):
                v_np = dt(1.0) + dt(2.0)**(-50)
                self.assertEqual(strip_position(v_np, 1, 1), mp.mpf(2) + mp.mpf(2)**(-50))
        # 6. corner_widths(4, 2**253 + 1) matches 420-digit outward reduction modulo pi/2
        with mp.workdps(75):
            cw_v, cw_h = corner_widths(4, (1 << 253) + 1)
            with mp.workdps(420):
                h4 = mp.pi / 4
                per = mp.pi / 2
                rem = ((1 << 253) + 1 + per / 2) % per - per / 2
                expected_cw = h4 - abs(rem)
            self.assertEqual(cw_v, +expected_cw)
            self.assertEqual(cw_h, +expected_cw)
            # 7. quadratic_roots at discriminant == -tolerance stays strictly real
            roots_bd = quadratic_roots(mp.mpf(1), mp.mpf(0), mp.mpf(1)/16, mp.mpf(1)/4)
            self.assertEqual(roots_bd, [mp.mpf(0)])
            # 8. half_period_cells rejects negative input_radius
            with self.assertRaises(ValueError):
                half_period_cells(4, 0, input_radius=-1)
        # 9. CLI --tongues prints outward-rounded brackets enclosing the pentagon's true transition
        out = subprocess.check_output(
            [sys.executable, str(Path(__file__).resolve().parent / 'phase1_regular.py'), '--tongues'],
            text=True,
        )
        p5_line = next(line for line in out.splitlines() if line.startswith('5 hull '))
        first_bracket = p5_line.split("unresolved event degrees ['[", 1)[1].split("]'", 1)[0]
        lo_str, hi_str = [s.strip() for s in first_bracket.split(',')]
        self.assertLessEqual(Decimal(lo_str), Decimal('44.49603432757450'))
        self.assertGreaterEqual(Decimal(hi_str), Decimal('44.49603432757452'))


if __name__ == '__main__':
    unittest.main()
