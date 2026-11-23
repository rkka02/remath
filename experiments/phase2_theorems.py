"""ReMath, Phase 2. Run with Python 3, mpmath, numpy and scipy.

No sampling noise. All transforms use positive arclength and CCW sides.
The Gamma, small-Gram and cancellation checks use arbitrary precision.
Larger trial-space, Gram and quadrature checks use double precision as labeled.
"""
import math

import mpmath as mp
import numpy as np
import scipy.linalg as la
from scipy.integrate import quad
from scipy.special import roots_legendre

mp.mp.dps = 80
I = mp.j
PI = mp.pi
T = 2 * PI * I
SQUARE = tuple(map(mp.mpc, [0, 1, 1+1j, 1j]))
TRI = (mp.mpc(0), mp.mpc(1), mp.mpc("0.5", mp.sqrt(3)/2))
SCALENE = (mp.mpc(0), mp.mpc("1.5", "0.1"), mp.mpc("0.2", "1.1"))
QUAD = (mp.mpc(0), mp.mpc("1.4", ".1"), mp.mpc("1.1", "1.2"), mp.mpc("-.2", ".8"))
TRAP = tuple(map(mp.mpc, [0, 2, 1+1j, 1j]))
PENT = tuple(mp.exp(T*j/5) for j in range(5))


def edges(v):
    return [v[(j+1) % len(v)] - x for j, x in enumerate(v)]


def h(v, s):
    return max(mp.re(s*z) for z in v)


def oriented(v, j, x):
    d = edges(v)
    s = T*x/d[j]
    return s, [mp.exp(s*(z-v[j])) for z in v]


class GammaSymbol:
    def __init__(self, v):
        self.v = v
        self.a = [d/T for d in edges(v)]
        u = mp.exp(I*mp.mpf(".347"))
        vertex = max(v, key=lambda z: mp.re(z*u))
        self.tau = vertex - sum(a*mp.log(-a*u) for a in self.a)

    def __call__(self, s):
        return mp.exp(self.tau*s)*mp.fprod(mp.rgamma(1-a*s) for a in self.a)

    def asymptotic(self, u):
        logs = [mp.log(-a*u) for a in self.a]
        return (self.tau+sum(a*z for a, z in zip(self.a, logs)),
                mp.exp(-sum(logs)/2)/(2*PI)**(len(logs)/2))


def area_transform(v, s):
    if not s:
        return sum(mp.im(mp.conj(z)*d) for z, d in zip(v, edges(v)))/2
    return -sum(mp.conj(d)/d * mp.exp(s*z)*mp.expm1(s*d)
                for z, d in zip(v, edges(v)))/(2*I*s**2)


def phi(z):
    return mp.expm1(z)/z if z else mp.mpf(1)


def unit_moment(k, z, left, right):
    """Integral t**k exp(s(w(t)-base)) dt from scaled endpoint values."""
    if abs(z) < mp.mpf("1e-25"):
        return left*mp.hyp1f1(k+1,k+2,z)/(k+1)
    value = (right-left)/z
    for j in range(1, k+1):
        value = (right-j*value)/z
    return value


def classification():
    print("A. Gamma symbol, sector constants, reflected rays, area and complex kernel")
    for label, v in [("equilateral", TRI), ("scalene", SCALENE), ("quadrilateral", QUAD),
                     ("trapezoid", TRAP), ("pentagon", PENT), ("square", SQUARE)]:
        L = GammaSymbol(v)
        p = len(v)
        leading = []
        for j, vertex in enumerate(v):
            e = edges(v)
            u = I/(e[j]/abs(e[j])) + I/(e[j-1]/abs(e[j-1]))
            u /= abs(u)
            vstar, amplitude = L.asymptotic(u)
            assert abs(vstar-vertex) < mp.mpf("1e-74")
            s = 4000*u
            ratio = 4000**(mp.mpf(p)/2)*L(s)*mp.exp(-s*vertex)/amplitude
            assert abs(ratio-1) < mp.mpf(".004")
            leading.append(amplitude*u**(p//2))
        if p % 2 == 0:
            assert max(abs(leading[j]/leading[0]-(-1)**j) for j in range(p)) < mp.mpf("1e-72")
        ray = 1/L.a[0]
        for x in [mp.mpf("300.25"), mp.mpc("300.25", ".3"), mp.mpc("300.001", "-.2")]:
            s = x*ray
            u0 = ray/abs(ray)
            u = u0*mp.exp(mp.mpf(".0001")*I)
            vertex, amplitude = L.asymptotic(u)
            # CCW rotation in the s-plane selects the start of the oriented edge.
            assert abs(vertex-v[0]) < mp.mpf("1e-70")
            pred = amplitude*(s/u)**(-mp.mpf(p)/2)*mp.exp(s*v[0])*(-mp.expm1(s*edges(v)[0]))
            assert abs(L(s)/pred-1) < mp.mpf(".004")
        nodes = [m/a for a in L.a for m in (1, 2, 6)]
        assert max(abs(L(s))*mp.exp(-h(v,s)) for s in nodes) < mp.mpf("1e-70")
        reflected = max(abs(L(-1/a))*mp.exp(-h(v,-1/a)) for a in L.a)
        assert (reflected < mp.mpf("1e-70")) == (label == "square")
        dims = (2*(p//2)-1, p if p % 2 else p-1, p)
        print(f"  {label:14} predicted real dimensions {dims}, reflected defect {mp.nstr(reflected,6)}")
    for v in [TRI, SCALENE]:
        for j in range(3):
            s, phases = oriented(v, j, 1)
            assert abs(area_transform(v,s)*mp.exp(-s*v[j])) > mp.mpf(".001")
            # A Duffy parametrization, reduced analytically in one coordinate.
            a, b = v[(j+1)%3]-v[j], v[(j+2)%3]-v[j]
            integ = abs(mp.im(mp.conj(a)*b))*mp.quad(
                lambda t: mp.exp(s*a*t)*(1-t)*phi(s*b*(1-t)), [0, 1])
            assert abs(integ-area_transform(v,s)*mp.exp(-s*v[j])) < mp.mpf("1e-72")
    s = T
    H = mp.sqrt(3)/2
    torsion = 0
    for z, d in zip(TRI, edges(TRI)):
        # On a side the two other distances are H*t and H*(1-t).
        torsion += abs(d)*mp.quad(lambda t: H*t*(1-t)*mp.exp(s*(z+d*t)), [0,1])
    exact = mp.sqrt(3)*(1+mp.exp(-PI*mp.sqrt(3)))/(2*s*s)
    assert abs(torsion-exact) < mp.mpf("1e-74")
    print("  equilateral torsion at 2 pi i:", mp.nstr(exact, 18))
    for v in [TRI, QUAD]:
        for s in [mp.mpc(".6", "-.3"), T/edges(v)[1]]:
            integral = sum(d*mp.quad(lambda t: (z+d*t)**3*mp.exp(s*(z+d*t)), [0,1])
                           for z,d in zip(v,edges(v)))
            assert abs(integral) < mp.mpf("1e-67")


def moments_and_atoms():
    """Check moment completion on every real multiplier direction and test pure atoms."""
    for v in (TRI,SCALENE,QUAD,TRAP,PENT,SQUARE):
        L = GammaSymbol(v)
        p,k = len(v),len(v)//2
        jet = mp.taylor(L,0,k)
        u = mp.exp(mp.mpf(".347")*I)
        _,amplitude = L.asymptotic(u)
        top = 1/(amplitude*u**k) if p%2==0 else 1
        polynomials = [(0,1)]+[(j,c) for j in range(1,k) for c in (1,I)]
        polynomials.extend([(k,top)] if p%2==0 else [(k,1),(k,I)])
        columns = []
        for degree,c in polynomials:
            coeff = [mp.factorial(j)*c*jet[j-degree] if j>=degree else 0
                     for j in range(k+1)]
            col = [float(mp.re(coeff[0]))]
            for j in range(1,k):
                col.extend([float(mp.re(coeff[j])),float(mp.im(coeff[j]))])
            col.append(float(mp.re(coeff[k]/top)))
            if p%2:
                col.append(float(mp.im(coeff[k]/top)))
            columns.append(col)
        M = np.array(columns).T
        assert np.linalg.matrix_rank(M)==p
        assert np.linalg.matrix_rank(M[:2*k-1,:2*k-1])==2*k-1
    for v,invisible in [(SQUARE,True),(QUAD,False),(TRAP,False)]:
        pure = lambda j,m: sum((-1)**k*z for k,z in enumerate(oriented(v,j,m)[1]))
        defect = max(abs(pure(j,m)) for j in range(4) for m in range(1,5))
        assert (defect<mp.mpf("1e-64"))==invisible


def mp_design(v, n, theta=None):
    rows = [(j, mp.mpf(m)) for j in range(len(v)) for m in range(1, n+1)]
    if theta is not None:
        rows += [(0, m+mp.mpf(theta)) for m in range(n)]
    spec = [oriented(v,j,x) for j,x in rows]
    return rows, spec


def gram_mp(v, n, theta):
    rows, spec = mp_design(v, n, theta)
    nr = len(rows)
    G = mp.matrix(2*nr)
    A = mp.matrix(2*nr,len(v))
    for r,(s,ps) in enumerate(spec):
        for j,z in enumerate(ps):
            A[2*r,j], A[2*r+1,j] = z.real,z.imag
        for l in range(r+1):
            t,pt = spec[l]
            plain = mp.mpc(0)
            herm = mp.mpc(0)
            for j,d in enumerate(edges(v)):
                k = (j+1)%len(v)
                x,y = s*d,t*d
                plain += abs(d)*unit_moment(0,x+y,ps[j]*pt[j],ps[k]*pt[k])
                herm += abs(d)*unit_moment(0,x+mp.conj(y),ps[j]*mp.conj(pt[j]),ps[k]*mp.conj(pt[k]))
            block = [[mp.re(herm+plain)/2,mp.im(plain-herm)/2],
                     [mp.im(plain+herm)/2,mp.re(herm-plain)/2]]
            for u in range(2):
                for w in range(2):
                    G[2*r+u,2*l+w] = G[2*l+w,2*r+u] = block[u][w]
    return G,A


def mp_recovery(v, n, theta):
    G,A = gram_mp(v,n,theta)
    H = (A.T*(G**-1)*A)**-1
    W = H*A.T*(G**-1)
    error = max(abs(x) for x in W*A-mp.eye(len(v)))
    assert error < mp.mpf("1e-55")
    assert max(abs(x) for x in W*G*W.T-H) < mp.mpf("1e-54")
    # Matched zero-data ambiguity, of unit background norm, for coordinate 0.
    e = mp.eye(len(v))[:,0]
    a = H*e/mp.sqrt(H[0,0])
    coeff = -(G**-1)*A*a
    assert abs((coeff.T*G*coeff)[0]-1) < mp.mpf("1e-55")
    assert max(abs(x) for x in A*a+G*coeff) < mp.mpf("1e-55")
    return [mp.sqrt(H[j,j]) for j in range(len(v))]


def quad_design(v, n, theta=None, order=None):
    v = np.asarray(v,dtype=complex)
    d = np.roll(v,-1)-v
    q,wt = roots_legendre(order or max(96,5*n+40))
    t,wt = (q+1)/2,wt/2
    z = (v[:,None]+d[:,None]*t).ravel()
    weights = (np.abs(d[:,None])*wt).ravel()
    groups = [(j,np.arange(1,n+1)) for j in range(len(v))]
    if theta is not None:
        groups.append((0,np.arange(n)+theta))
    normals = np.concatenate([2j*np.pi*m/d[j] for j,m in groups])
    starts = np.concatenate([np.full(n,v[j]) for j,_ in groups])
    traces = np.exp(normals[:,None]*(z-starts[:,None]))
    traces *= np.sqrt(weights)
    vertices = np.exp(normals[:,None]*(v-starts[:,None]))
    return (np.vstack((traces.real,traces.imag)),np.vstack((vertices.real,vertices.imag)),
            normals,starts,z,weights,t)


def calibrated_averages(A, n, p, even=False):
    groups = p+int(even)
    avg = np.kron(np.eye(groups),np.ones((1,n))/n)
    avg = np.hstack((avg,np.zeros_like(avg)))
    return la.pinv(avg@A)@avg


def opt_quad(v,n,theta=None):
    D,A,*_ = quad_design(v,n,theta)
    # Work with the singular values of the rectangular sampling matrix,
    # not their squares. Used only for well resolved integer designs.
    U,sv,_ = la.svd(D, full_matrices=False)
    assert sv[-1] > 1e-10*sv[0]
    whitened = (U.T@A)/sv[:,None]
    risk = la.norm(la.pinv(whitened),axis=1)
    W = calibrated_averages(A,n,len(v),theta is not None)
    assert la.norm(W@A-np.eye(len(v))) < 3e-13
    return risk,la.norm(W@D,axis=1)


def ces_limit(v,k):
    v = np.asarray(v,dtype=complex)
    p = len(v)
    d = np.roll(v,-1)-v
    b = 2j*np.pi/d
    S = np.eye(p)+np.roll(np.eye(p),1,axis=1)
    c = la.inv(S)[k]
    value = 0
    # Remove the oscillatory sinc-squared tail analytically. Remaining
    # cross terms use a sine-weighted quadrature on [1,infinity).
    for j in range(p):
        for own,other,unit in [(j,(j-1)%p,d[j]/abs(d[j])),
                               ((j-1)%p,j,-d[j-1]/abs(d[j-1]))]:
            kap = abs(b[own])
            z = b[other]*unit
            def damp(x):
                return (np.expm1(z*x)/(z*x)).real if x else 1.0
            value += c[own]**2*np.pi/(2*kap)
            value += c[other]**2*quad(lambda x:damp(x)**2,0,np.inf,epsabs=3e-12)[0]
            cross = quad(lambda x: np.sinc(kap*x/np.pi)*damp(x),0,1)[0]
            cross += quad(lambda x:damp(x)/(kap*x),1,np.inf,weight="sin",wvar=kap,
                          epsabs=3e-12)[0]
            value += 2*c[own]*c[other]*cross
    return math.sqrt(value)


def minimax():
    print("B. Exact finite optimal-recovery risks (M=1)")
    for v in [SQUARE, QUAD]:
        for n in (1,2):
            for theta in (".25",".5",".75"):
                risk = mp_recovery(v,n,theta)
                print(" ", "square" if v == SQUARE else "quad", n, theta,
                      "vertex 0 / maximum", *(mp.nstr(x,10) for x in (risk[0],max(risk))))
    print("  scalene: N, sqrt(N) optimal, sqrt(N) calibrated Cesaro, ratio [vertex 0]")
    limit = ces_limit(SCALENE,0)
    for n in (4,12,32,64):
        opt,avg = opt_quad(SCALENE,n)
        assert (avg>=opt-1e-11).all()
        print(f"  {n:3} {opt[0]*np.sqrt(n):.9f} {avg[0]*np.sqrt(n):.9f} {avg[0]/opt[0]:.8f}")
    print(f"  independent tangent-ray Cesaro limit {limit:.9f}")
    assert abs(avg[0]*np.sqrt(n)-limit) < .015
    assert avg[0]/opt[0] > 1.01


def integrated_product(z,w,left,right):
    """Exact integral of a product of band integrals on a tangent half-line."""
    def xlogx(a):
        result = np.zeros_like(a)
        nz = abs(a)>0
        result[nz] = a[nz]*np.log(a[nz])
        return result

    def term(a,b):
        return xlogx(-a[:,None]*z-b[None,:]*w)
    return (term(right,right)-term(left,right)-term(right,left)+term(left,left))/(z*w)


def tangent_risk(v, bins):
    v = np.asarray(v,dtype=complex)
    p = len(v)
    d = np.roll(v,-1)-v
    freq = 2j*np.pi/d
    left = np.arange(bins)/bins
    right = left+1/bins
    count = p*bins
    H = np.zeros((count,count),complex)
    J = H.copy()
    for j in range(p):
        incident = (j,(j-1)%p)
        for u in (d[j]/abs(d[j]),-d[j-1]/abs(d[j-1])):
            for i in incident:
                for k in incident:
                    z,w = freq[i]*u,freq[k]*u
                    # The own-edge exponent is imaginary exactly.
                    if abs(z.real) < 1e-13: z = 1j*z.imag
                    if abs(w.real) < 1e-13: w = 1j*w.imag
                    rows = slice(i*bins,(i+1)*bins)
                    cols = slice(k*bins,(k+1)*bins)
                    H[rows,cols] += integrated_product(z,w.conjugate(),left,right)
                    J[rows,cols] += integrated_product(z,w,left,right)
    G = np.block([[(H+J).real,(J-H).imag],[(H+J).imag,(H-J).real]])/2
    S = np.eye(p)+np.roll(np.eye(p),1,axis=1)
    A = np.vstack((np.repeat(S,bins,axis=0)/bins,np.zeros((count,p))))
    Hinv = A.T@la.solve(G,A,assume_a="pos")
    return np.sqrt(np.diag(la.inv(Hinv)))


def check_tangent():
    last = math.inf
    for b in (1,2,4,8,16,32,64):
        c = tangent_risk(SCALENE,b)[0]
        print(f"  continuum dyadic upper bound, {b:2} bins: {c:.9f}")
        assert 0 < c < last
        last = c
    assert .50 < last < ces_limit(SCALENE,0)


def smooth_window(x, r):
    """Stable for fixed r as N grows. Solve the discrete moment equations."""
    N = len(x)
    # This C^infinity bump has compact support inside the high band.
    bump = []
    for z in x:
        t = z/N
        bump.append(mp.exp(-1/(16*(t-mp.mpf(".35"))*(mp.mpf(".95")-t)))
                    if mp.mpf(".35") < t < mp.mpf(".95") else mp.mpf(0))
    H = mp.matrix([[sum(b*(N/z)**(k+l) for b,z in zip(bump,x)) for k in range(r+1)]
                   for l in range(r+1)])
    coef = mp.lu_solve(H,mp.eye(r+1)[:,0])
    w = [b*sum(coef[k]*(N/z)**k for k in range(r+1)) for b,z in zip(bump,x)]
    assert max(abs(sum(v*(N/z)**l for v,z in zip(w,x))-(l==0))
               for l in range(r+1)) < mp.mpf("1e-57")
    return w


def extrapolation_window(x,r):
    n = len(x)
    gap = (n-1-n//2)//r
    if gap < 1:
        raise ValueError("the degree must fit the high band")
    index = [n//2+i*gap for i in range(r+1)]
    w = [mp.mpf(0)]*n
    for i,k in enumerate(index):
        w[k] = (-1)**(r-i)*x[k]**r/(gap**r*mp.factorial(i)*mp.factorial(r-i))
    assert abs(sum(w)-1) < mp.mpf("1e-62")
    return w


def weighted_recovery(v,n,charges,kind,r=3):
    groups = [(j,mp.mpf(1)) for j in range(len(v))]
    if len(v)%2 == 0:
        groups.append((0,mp.mpf(".5")))
    A = mp.matrix(len(groups),len(v))
    rhs = mp.matrix(len(groups),1)
    maxnorm = 0
    for row,(j,offset) in enumerate(groups):
        x = [m+offset for m in range(n)]
        if kind=="uniform":
            weights = [mp.mpf(1)/n]*n
        elif kind=="smooth":
            weights = smooth_window(x,r)
        else:
            weights = extrapolation_window(x,r)
        maxnorm = max(maxnorm,mp.sqrt(sum(w*w for w in weights)))
        for m,weight in zip(x,weights):
            if not weight:
                continue
            s,P = oriented(v,j,m)
            diffuse = mp.mpc(0)
            for l,d in enumerate(edges(v)):
                # A real analytic, edge-dependent density in fractional arclength.
                b = mp.mpf(l+1)/5
                diffuse += abs(d)*(1+mp.mpf(l)/4)*unit_moment(
                    0,s*d+b,P[l],mp.exp(b)*P[(l+1)%len(v)])
                A[row,l] += weight*P[l].real
            rhs[row] += weight*(diffuse+sum(z*a for z,a in zip(P,charges))).real
    result,_ = mp.qr_solve(A,rhs)
    return max(abs(result[i]-charges[i]) for i in range(len(v))),maxnorm


def windows():
    print("B. Smooth edge densities: max vertex error; largest row weight norm")
    for v,a in [(SCALENE,[2,-1,3]),(SQUARE,[2,-1,3,-2])]:
        for n in (32,64,128):
            err,norm = weighted_recovery(v,n,a,"uniform")
            high,_ = weighted_recovery(v,n,a,"smooth",3)
            rich,cond = weighted_recovery(v,n,a,"richardson",min(8,n//8))
            print(" ",len(v),n,*(mp.nstr(z,8) for z in (err,high,rich,cond)))
        assert high < mp.mpf("1e-9") and rich < mp.mpf("1e-15") and err > mp.mpf(".001")
    grid = list(map(mp.mpf,range(1,65)))
    w = extrapolation_window(grid,8)
    support = [z for z,v in zip(grid,w) if v]
    lower = abs(mp.chebyt(8,(max(support)+min(support))/(max(support)-min(support))))
    assert sum(abs(v) for v in w) >= lower


def smooth_bump_scaling():
    """N-dependent C^2 and H^2 witnesses near vertex zero, using the calibrated row."""
    v = np.asarray(SCALENE,complex)
    d = np.roll(v,-1)-v
    q,gw = roots_legendre(24)
    y,gw = (q+1)/2,gw/2
    delta = .004
    shape = y**3*(1-y)**3
    for n in (32,64,128):
        x = np.arange(1,n+1)
        weights = np.array(smooth_window(list(map(mp.mpf,x.tolist())),2),float)
        A,probe = [],[]
        for j,side in enumerate(d):
            s = 2j*np.pi*x[:,None]/side
            A.append(weights@np.exp(s*(v-v[j])).real)
            probe.append(weights@np.exp(s*(v[0]-v[j]+d[0]*delta*y/n)).real)
        kernel = la.solve(np.asarray(A),np.asarray(probe))[0]
        scaled = delta*abs(d[0])*np.dot(gw,shape*kernel)
        expected = delta*abs(d[0])/140
        assert .94 < scaled/expected < 1.06
        print(f"  C^2 bump error times N^3 (also H^2 times N^(5/2)): {scaled:.8g}")


def polynomial_transfer():
    """Truncated residue interpolation on the closed square, vertices included."""
    L = GammaSymbol(SQUARE)
    t = mp.mpc(".7","-.24")
    locations = list(SQUARE)+[mp.mpc(".37"),mp.mpc(".31",".7")]
    previous = math.inf
    for n in (12,24,48,96):
        extra = [T*(m+mp.mpf(".5")) for m in range(n//4)]
        def poly(s):
            return mp.fprod(s-z for z in extra)
        terms = [(q,L(q)*mp.fprod(q-z for z in extra if z!=q)) for q in extra]
        for j,c in enumerate(L.a):
            for m in range(1,n+1):
                s = m/c
                derivative = (mp.exp(L.tau*s)*(-1)**m*c*mp.factorial(m-1)
                              *mp.fprod(mp.rgamma(1-z*s) for l,z in enumerate(L.a) if l!=j))
                terms.append((s,derivative*poly(s)))
        factor = L(t)*poly(t)
        error = max(abs(factor*mp.fsum(mp.exp(s*w)/((t-s)*der) for s,der in terms)
                        -mp.exp(t*w)) for w in locations)
        print("  closed-square exponential transfer:",n,mp.nstr(error,7))
        assert error < previous
        previous = error
    assert error < mp.mpf("1e-10")


def pde_trial(v,n=5):
    verts = np.array(v,complex)
    d = np.roll(verts,-1)-verts
    p = len(d)
    _,_,nodes,start,z,wt,t = quad_design(v,n)
    gauss = np.exp(nodes[:,None]*(z-start[:,None]))*wt
    # Independent affine edge traces, plus the normalized exact physical mode.
    basis = np.zeros((len(z),2*p))
    for j in range(p):
        sl = slice(j*len(t),(j+1)*len(t))
        basis[sl,2*j] = 1
        basis[sl,2*j+1] = 2*t-1
    plane = gauss@basis
    exact = GammaSymbol(v)
    # Use the exact transform for the one non-polynomial enriched column.
    spectral = np.array([complex(exact(s)*mp.exp(-s*base))
                         for s,base in zip(nodes,start)])
    coll = np.column_stack((plane,spectral))
    op = np.vstack((coll.real,coll.imag))
    nmom = 2 if p==4 else 1
    moments = []
    for k in range(nmom):
        row = np.r_[(wt*z**k)@basis,complex(mp.diff(exact,0,k))]
        moments.append(row.real)
        if k:
            moments.append(row.imag)
    mom = np.array(moments)
    completed = np.vstack((op,mom))
    Vnull = la.null_space(op,rcond=1e-12)
    nrm = -1j*d/abs(d)
    nullvecs = [np.r_[np.zeros(2*p),1]]
    if p==4:
        for comp in [nrm.real,nrm.imag]:
            vec = np.zeros(2*p+1)
            vec[:-1:2] = comp
            nullvecs.append(vec)
    known = la.orth(np.column_stack(nullvecs))
    assert la.norm(Vnull@Vnull.T-known@known.T) < 2e-11
    assert Vnull.shape[1] == (3 if p==4 else 1)
    # q = Re(w^2 + (0.3+0.2i)w). Build RHS from independently evaluated q_t.
    derivative = 2*z+(.3+.2j)
    tangent = np.repeat(d/abs(d),len(t))
    qt = (tangent*derivative).real
    qn = (-1j*tangent*derivative).real
    projected = 1j*(gauss@qt)
    rhs = [*projected.real,*projected.imag]
    for k in range(nmom):
        value = 1j*np.dot(wt*z**k,qt)
        rhs.append(value.real)
        if k:
            rhs.append(value.imag)
    coeff = la.lstsq(completed,rhs)[0]
    error = max(np.max(abs(basis@coeff[:-1]-qn)),abs(coeff[-1]))
    if p==4:
        odd = np.arange(1,600,2)*np.pi
        enriched = np.tile(np.sin(t[:,None]*odd)@(4*np.tanh(odd/2)/odd**2),p)
    else:
        D,_,_,_,_,_,_ = quad_design(v,12,order=len(t))
        X = np.vstack((np.sqrt(wt),D))
        values = np.zeros(X.shape[0])
        values[0] = 1
        enriched = la.lstsq(X,values)[0]/np.sqrt(wt)
    recovered_flux = basis@coeff[:-1]+coeff[-1]*enriched
    boundary_data = (z*z+(.3+.2j)*z).real
    normals = np.repeat(nrm,len(t))
    field_error = 0
    for corner in verts:
        interior = .8*np.mean(verts)+.2*corner
        offset = z-interior
        field = np.dot(wt,boundary_data*(normals/offset).real
                       -np.log(abs(offset))*recovered_flux)/(2*np.pi)
        field_error = max(field_error,abs(field-(interior**2+(.3+.2j)*interior).real))
    print(" ",p,"affine-only nullity",2*p-np.linalg.matrix_rank(op[:,:-1],tol=1e-12),
          "enriched nullity",Vnull.shape[1],"completed cond / flux error / field error",
          f"{np.linalg.cond(completed):.6g}",f"{error:.3g}",f"{field_error:.3g}")
    assert error < 2e-12 and field_error < 5e-13


def field_flux_tests():
    print("C. Fokas discretization on the square and equilateral triangle")
    pde_trial(SQUARE)
    pde_trial(TRI)
    # Independent square torsion edge sine series for the unit square.
    s = mp.mpc(".7","-.2")
    L = GammaSymbol(SQUARE)
    approx = 0
    for z,d in zip(SQUARE,edges(SQUARE)):
        b = s*d
        approx += mp.exp(s*z)*sum(4*mp.tanh(n*PI/2)*(1+mp.exp(b))/
                                  (n*PI*((n*PI)**2+b*b)) for n in range(1,1200,2))
    print("  square torsion sine-series error:",mp.nstr(abs(approx-L(s)),7))
    assert abs(approx-L(s)) < mp.mpf(".000001")


def jumps():
    print("C. Jump flux: paired cutoff of an explicit harmonic angle field")
    for v,temps in [(TRI,[1,4,-2]),(SQUARE,[1,4,-2,5])]:
        a = [temps[j]-temps[j-1] for j in range(len(v))]
        s,P = oriented(v,0,1)
        atom = sum(z*q for z,q in zip(P,a))
        assert sum(a)==0
        if len(a)==3:
            S = [a[j]+a[(j+1)%3] for j in range(3)]
            assert (S[0]-S[1]+S[2])/2 == a[0]
        else:
            alt = [1,-1,1,-1]
            assert abs(sum(z*q for z,q in zip(P,alt))) < mp.mpf("1e-72")
            _,shifted = oriented(v,0,mp.mpf("4.5"))
            assert abs(sum(z*q for z,q in zip(shifted,alt))) > 1
        print(" ",len(v),"wall jumps",a,"real,imag of normalized normal transform",
              mp.nstr(I*atom,8))
    # q=arg(w) at the origin on each polygon. The other edge data vary
    # smoothly. On every open side q_t + i q_n = -i d/(|d| w).
    s = mp.mpc(".8","-.3")
    for v in (TRI,SQUARE):
        omega = mp.arg(v[-1])
        for eps in map(mp.mpf,["1e-3","1e-6","1e-9"]):
            ordinary = 0
            for j,(z,d) in enumerate(zip(v,edges(v))):
                lo = eps/abs(d) if j==0 else 0
                hi = 1-eps/abs(d) if j==len(v)-1 else 1
                ordinary += mp.quad(lambda t: -I*d*mp.exp(s*(z+d*t))/(z+d*t),[lo,hi])
            assert abs(ordinary-omega) < 4*eps
        print(" ",len(v),"cutoff residual after inclusion of tangent atom",mp.nstr(abs(ordinary-omega),6))


def certified_shift():
    """Outward-rounded interval certificate for the strict N=1 counterexample."""
    iv = mp.iv
    iv.dps = 45
    ti = 2*iv.pi*iv.mpc(0,1)
    vertices = [iv.mpc(0),iv.mpc(1),iv.mpc(1,1),iv.mpc(0,1)]
    for offset,lower,upper in [(2,".6612",".6613"),(3,".6198",".6200")]:
        # All exponents are (2*pi*i/4) times Gaussian integers. Keep those
        # integers exactly to handle the removable zeros in edge integrals.
        vi = [0,1,1+1j,1j]
        di = edges(vi)
        spec = [4/x for x in di]+[offset+0j]
        nr = len(spec)
        G,A = iv.matrix(2*nr),iv.matrix(2*nr,4)
        phases = [[iv.exp(ti/4*iv.mpc(s.real,s.imag)*(z-vertices[r%4]))
                   for z in vertices] for r,s in enumerate(spec)]
        def exponential_integral(z,P,Q):
            return (Q-P)/(ti/4*iv.mpc(z.real,z.imag)) if z else P
        for r,s in enumerate(spec):
            for j,x in enumerate(phases[r]):
                A[2*r,j],A[2*r+1,j] = x.real,x.imag
            for l,t in enumerate(spec):
                J,H = iv.mpc(0),iv.mpc(0)
                for j,dj in enumerate(di):
                    k = (j+1)%4
                    a,b = phases[r][j],phases[r][k]
                    c,e = phases[l][j],phases[l][k]
                    J += exponential_integral((s+t)*dj,a*c,b*e)
                    H += exponential_integral(s*dj-(t*dj).conjugate(),
                                              a*iv.mpc(c.real,-c.imag),b*iv.mpc(e.real,-e.imag))
                G[2*r,2*l],G[2*r,2*l+1] = (H+J).real/2,(J-H).imag/2
                G[2*r+1,2*l],G[2*r+1,2*l+1] = (J+H).imag/2,(H-J).real/2
        cov = (A.T*(G**-1)*A)**-1
        risk = [iv.sqrt(cov[j,j]) for j in range(4)]
        assert any(r > iv.mpf(lower) for r in risk) and all(r < iv.mpf(upper) for r in risk)
        print(f"  interval certificate theta={offset}/4: {lower} < maximum < {upper}")


def physical_step():
    """Conformal Poisson solution for regular polygons, independent of the GR."""
    from scipy.special import betainc
    q,w = roots_legendre(90)
    x,wt = (q+1)/2,w/2
    for p,temps in [(3,[1,4,-2]),(4,[1,4,-2,5])]:
        a = np.array(temps)-np.roll(temps,1)
        v = np.exp(2j*np.pi*np.arange(p)/p)
        angle = 2*np.pi*np.arange(p)/p
        # Fractional side length from a prevertex, from Schwarz-Christoffel.
        dt = (np.pi/p)*x**p
        frac = betainc((1-2/p)/2,.5,np.sin(p*dt/2)**2)/2
        jac = np.pi*x**(p-1)
        defect = 0
        for s in (2j*np.pi/(v[1]-v[0]),3j*np.pi/(v[1]-v[0]),.43-.2j):
            P = np.exp(s*(v-v[0]))
            normal = 0j
            for j in range(p):
                for sign in (-1,1):
                    dz = (v[(j+sign)%p]-v[j])*frac
                    near = P[j]*np.expm1(s*dz)
                    for k in range(p):
                        arg = (angle[j]-angle[k]+sign*dt)/2
                        # Subtracting P[k] on the whole circle implements PV.
                        shift = near if k==j else P[j]-P[k]+near
                        normal += a[k]*np.dot(wt,jac*shift/np.tan(arg))/(2*np.pi)
            defect = max(defect,abs(normal-1j*(a@P)))
        print(f"  regular {p}-gon, Poisson heat flux vs jump measure: {defect:.3g}")
        assert defect < 2e-12


def physical_triangle():
    """Least-norm density for mass one and finitely many zero integer samples."""
    L = GammaSymbol(TRI)
    s = .91-.52j
    target = complex(L(s))
    previous = 1
    for n in (4,16,48):
        D,_,_,_,z,wt,_ = quad_design(TRI,n)
        X = np.vstack((np.sqrt(wt),D))
        y = np.zeros(X.shape[0]); y[0] = 1
        density_weighted = la.lstsq(X,y)[0]
        value = np.dot(np.sqrt(wt)*np.exp(s*z),density_weighted)
        err = abs(value-target)
        print(f"  triangle mass-one reconstructed flux: N={n}, off-grid error {err:.5g}")
        assert err < previous
        previous = err
    assert err < 1e-5


def single_shift_and_cardinals():
    L = GammaSymbol(SQUARE)
    v = SQUARE
    for n in (16,64,256):
        # E is the next omitted integer cardinal. It is invisible on the
        # measured grid, and responds by order one at the last half-step.
        node = T*(n+1)
        derivative = mp.diff(L,node)
        def cardinal(s):
            return (s/node)**2*L(s)/((s-node)*derivative)
        last = T*(n-mp.mpf(".5"))
        fixed = T/2
        fixed_null = lambda s: I*s*(s-fixed)*L(s)
        assert abs(fixed_null(fixed)) < mp.mpf("1e-70")
        assert abs(cardinal(T*n)) < mp.mpf("1e-70")
        last_response = abs(cardinal(last))
        assert mp.mpf(".2") < last_response < mp.mpf(".23")
        m,band = n//2,n//4
        theta = mp.mpf(".5")
        def coeff(l):
            return mp.expm1(T*theta)/(T*(theta-l))
        total = sum(coeff(l) for l in range(-band,band+1))
        endpoint_response = -1-total
        own_norm = mp.sqrt(1-sum(abs(coeff(l))**2 for l in range(-band,band+1)))
        assert abs(endpoint_response)>.9 and own_norm*mp.sqrt(n)<1.1
        print("  single shift N, last-cardinal response, middle projected norm:",
              n,mp.nstr(last_response,6),mp.nstr(own_norm,6))
    # A one-node interpolant on the odd grid has bounded cost along each ray.
    L = GammaSymbol(SCALENE)
    for m in (4,16):
        v = SCALENE; b = T/edges(v)[0]; q = b*m
        derivative = mp.diff(L,q)
        E = lambda s: (s/q)*L(s)*mp.exp(q*v[0])/((s-q)*derivative)
        assert abs(E(q+mp.mpf("1e-35"))*mp.exp(-q*v[0])-1) < mp.mpf("1e-32")
        assert abs(E(0))+abs(E(T/edges(v)[1])) < mp.mpf("1e-65")


def enriched_rates():
    print("B. Square with a half-shift: N^(3/4) times exact finite risks")
    for n in (2,4,8,12):
        risk = mp_recovery(SQUARE,n,".5")
        scaled = [n**mp.mpf(".75")*r for r in risk]
        print(" ",n,*(mp.nstr(v,9) for v in (scaled[0],max(scaled))))
        assert all(mp.mpf(".4") < r < mp.mpf(".9") for r in scaled)


if __name__ == "__main__":
    print("mpmath",mp.__version__,"digits",mp.mp.dps,"numpy",np.__version__)
    classification()
    moments_and_atoms()
    minimax()
    certified_shift()
    check_tangent()
    single_shift_and_cardinals()
    enriched_rates()
    polynomial_transfer()
    windows()
    smooth_bump_scaling()
    field_flux_tests()
    physical_triangle()
    jumps()
    physical_step()
    print("All checks passed.")
