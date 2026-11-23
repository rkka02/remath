"""ReMath Phase 3. Run with Python 3, numpy, scipy and mpmath from any directory."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as la
from scipy import special

from phase2_theorems import GammaSymbol, edges, unit_moment
from phase3_square_certificate import square_certificate

ROOT = Path(__file__).resolve().parent
BANDS = (2, 4, 6, 8, 12, 16, 20)


def arclength_gram(vertices, n, theta):
    """Integrate both complex products on each edge, using the current precision for pi."""
    directions = edges(vertices)
    specs = [(j,m) for j in range(len(vertices)) for m in range(1,n+1)]
    specs.extend((0,m+mp.mpf(theta)) for m in range(n))
    rows = []
    for j,m in specs:
        s = 2*mp.pi*mp.j*m/directions[j]
        phases = [mp.exp(s*(z-vertices[j])) for z in vertices]
        rows.append((s,phases))
    G,A = mp.matrix(2*len(rows)),mp.matrix(2*len(rows),len(vertices))
    for i,(s,f) in enumerate(rows):
        for j,v in enumerate(f):
            A[2*i,j],A[2*i+1,j] = v.real,v.imag
        for l,(t,h) in enumerate(rows[:i+1]):
            plain,herm = 0,0
            for j,d in enumerate(directions):
                k = (j+1)%len(vertices)
                plain += abs(d)*unit_moment(0,(s+t)*d,f[j]*h[j],f[k]*h[k])
                herm += abs(d)*unit_moment(0,s*d+mp.conj(t*d),f[j]*mp.conj(h[j]),f[k]*mp.conj(h[k]))
            block = (((herm+plain).real/2,(plain-herm).imag/2),
                     ((plain+herm).imag/2,(herm-plain).real/2))
            for a in (0,1):
                for b in (0,1):
                    G[2*i+a,2*l+b] = G[2*l+b,2*i+a] = block[a][b]
    return G,A


def vertex_risks(G, A):
    """Whiten the four columns by triangular solves. The large inverse is unnecessary."""
    L = mp.cholesky(G)
    n = L.rows
    B = mp.matrix(n, A.cols)
    for k in range(A.cols):
        for i in range(n):
            B[i,k] = (A[i,k] - mp.fdot((L[i,j], B[j,k]) for j in range(i))) / L[i,i]
    info = B.T * B
    K = info**-1
    tolerance = mp.eps**mp.mpf('.4')
    assert max(abs(z) for z in L*B-A) < tolerance
    assert max(abs(z) for z in info*K-mp.eye(A.cols)) < tolerance
    for k in range(A.cols):
        a = K[:,k]/mp.sqrt(K[k,k])
        whitened = -B*a
        assert abs(mp.fdot(whitened,whitened)-1) < tolerance
        assert max(abs(z) for z in A*a+L*whitened) < tolerance
    return [mp.sqrt(K[j,j]) for j in range(A.cols)]


def rhombus(precision):
    with mp.workdps(precision):
        u = mp.mpc(mp.mpf(1)/2, mp.sqrt(3)/2)
        v = (0, 1, 1+u, u)
        G, A = arclength_gram(v, max(BANDS), '.5')
        results = []
        for n in BANDS:
            ids = [2*(block*max(BANDS)+m)+part for block in range(5)
                   for m in range(n) for part in (0,1)]
            g = mp.matrix([[G[i,j] for j in ids] for i in ids])
            a = mp.matrix([[A[i,j] for j in range(4)] for i in ids])
            risks = vertex_risks(g, a)
            print('rhombus', precision, n, *(mp.nstr(x, 11) for x in risks), flush=True)
            results.append([mp.nstr(x, 45) for x in risks])
        return results


def square_design(n, theta):
    """Rectangular quadrature with divided differences extending to both endpoints."""
    q, wt = special.roots_legendre(64)
    v = np.array([0,1,1+1j,1j])
    d = np.roll(v,-1)-v
    z = np.r_[(v[:,None]+d[:,None]*(q+1)/2).ravel(), v]
    rows = []
    for j in range(4):
        f = 2j*np.pi*(z-v[j])/d[j]
        rows.extend(np.exp(m*f) for m in range(1,n+1))
    f = 2j*np.pi*z
    for m in range(n):
        near = m + int(theta >= .5)
        delta = m+theta-near
        diff = np.expm1(delta*f)/delta if delta else f
        row = np.exp(near*f)*diff
        if near == 0:
            row = np.exp(theta*f).real + 1j*diff.imag
        rows.append(row)
    H = np.concatenate((np.real(rows), np.imag(rows)))
    D = H[:,:-4]*np.tile(np.sqrt(wt/2),4)
    _, T = la.qr(D.T, mode='economic')
    B = la.solve_triangular(T.T,H[:,-4:],lower=True)
    if n==1 and theta==0:
        return np.full(4,np.inf)
    return la.norm(la.pinv(B),axis=1)


def square_curve():
    grid = np.arange(1, 41)/41
    values, optima = [], []
    for n in (1,2,4):
        def risks(t):
            return square_design(n, t)
        certificate = square_certificate(n)
        raw = []
        max_check = 0.0
        with mp.workdps(60):
            v = tuple(map(mp.mpc,[0,1,1+1j,1j]))
            for j,t in enumerate(grid):
                row = vertex_risks(*arclength_gram(v,n,mp.mpf(j+1)/41))
                max_check = max(max_check, max(abs(float(z)-b) for z,b in zip(row,risks(t))))
                raw.append([mp.nstr(z,38) for z in row])
        values.append(raw)
        with mp.workdps(60):
            half=vertex_risks(*arclength_gram(v,n,mp.mpf('.5')))
        assert max_check < 2e-9
        certificate['grid_quadrature_max_error'] = float(max_check)
        certificate['half_step_risks']=[mp.nstr(z,38) for z in half]
        certificate['limits_at_0_and_1_double']=[
             'infinite' if n==1 else float(max(risks(0))),float(max(risks(1)))]
        assert float(certificate['risk_bracket'][1]) < float(max(half))
        optima.append(certificate)
    return {'N':[1,2,4],'theta':grid.tolist(),'theta_exact':'j/41, 1 <= j <= 40',
            'risks':values,'optima':optima}


def tilt_curve():
    eps = sorted(set(np.r_[0.,np.geomspace(1e-7,.01,13),np.linspace(.01,.2,39)]))
    sigmas = []
    with mp.workdps(75):
        for e in eps:
            v = (0,1,(1+mp.j)*mp.exp(mp.j*float(e)),mp.j)
            symbol = GammaSymbol(v)
            d = edges(v)
            u = (-1+mp.j)/mp.sqrt(2)  # Re(u*z) exposes vertex zero.
            vert, amp = symbol.asymptotic(u)
            assert abs(vert)<mp.mpf('1e-65')
            q2 = 1/(amp*u**2)
            rows, differentiated = [],[]
            directions_prime = (0,-1+mp.j,1-mp.j,0)
            for j,dj in enumerate(d):
                for m in range(1,7):
                    s = -2*mp.pi*mp.j*m/dj
                    base = max(v,key=lambda w:mp.re(s*w))
                    val = mp.exp(-s*base)*symbol(s)
                    row = [val,s*val,mp.j*s*val,q2*s*s*val]
                    rows.extend([[float(z.real) for z in row],[float(z.imag) for z in row]])
                    if e==0:
                        other = (j+2)%4
                        mismatch = 2*mp.pi*mp.j*m*(directions_prime[j]/dj**2+
                                                 directions_prime[other]/d[other]**2)
                        slope = mp.exp(-s*base)*mp.diff(symbol,s)*mismatch
                        dr = [slope,s*slope,mp.j*s*slope,q2*s*s*slope]
                        differentiated.extend([[float(z.real) for z in dr],[float(z.imag) for z in dr]])
            sv = la.svdvals(rows)
            if e == 0:
                assert sv[0] < 1e-60
                sv[:] = 0
                slopes = la.svdvals(differentiated)
            else:
                assert sv[-1] > 0
            sigmas.append(sv.tolist())
    assert np.max(np.abs(np.array(sigmas[1])/eps[1]/slopes-1))<3e-6
    return {'epsilon':eps,'singular_values':sigmas,'harmonics':6,
            'first_order_slopes':slopes.tolist(),
            'moving_vertex':'(1+i)*exp(i*epsilon)', 'one_sided_basis':['L','sL','isL','q2*s^2*L'],
            'basis_norm':'Euclidean on real coefficients; q2 gives unit atom at vertex 0'}



def skeleton_coefficients(order):
    """Taylor coefficients of h(r)/sqrt(r) on a median, from the Binet kernel."""
    logcoef = {j: (-1)**((j-3)//6)*3/mp.pi*mp.factorial(j-1)*mp.zeta(j+1)
               for j in range(3,order+1,6)}
    expansion = [mp.mpf(0)]*(order+1)
    expansion[0] = 1
    for n in range(3,order+1,3):
        expansion[n] = mp.fsum(k*b*expansion[n-k] for k,b in logcoef.items() if k<=n)/n
    return [expansion[n]/mp.gamma(n+mp.mpf('1.5')) for n in range(0,order+1,3)]


def inverse_beta(a, b, p):
    """Use the nearer endpoint and refine the inverse regularized beta at working precision."""
    if p == 0 or p == 1:
        return p
    if p > mp.mpf('.5'):
        return 1-inverse_beta(b,a,1-p)
    x = mp.mpf(special.betaincinv(float(a),float(b),float(p)))
    beta = mp.beta(a,b)
    for _ in range(4):
        step = (mp.betainc(a,b,0,x,regularized=True)-p)*beta*x**(1-a)*(1-x)**(1-b)
        x -= step
        if abs(step) < mp.eps*x*8:
            break
    return x


def median_quadrature(order, series_order, levels):
    # u=sqrt(r/R) removes the inverse square root in the two derivative modes.
    # dyadic panels keep the Poisson peak at r comparable to x resolved.
    R = 1/mp.sqrt(3)
    coeff = skeleton_coefficients(series_order)
    derivative = [(3*j+mp.mpf('.5'))*a for j,a in enumerate(coeff)]
    nodes, weights = mp.gauss_quadrature(order,'legendre')
    third = mp.mpf(1)/3
    bounds = [0]+[mp.mpf(2)**(-j) for j in range(levels,-1,-1)]
    sample = []
    for left,right in zip(bounds,bounds[1:]):
        for g,w in zip(nodes,weights):
            u = (left+right+(right-left)*g)/2
            r = R*u*u
            dr = R*u*(right-left)*w
            h = mp.sqrt(r)*mp.polyval(coeff[::-1],r**3)
            dh = mp.polyval(derivative[::-1],r**3)/mp.sqrt(r)
            t = u*u
            if t <= mp.mpf('.5'):
                s = inverse_beta(third,third,t)
                delta = -mp.expm1(mp.log1p(-s)/3)
                q = 1-delta
            else:
                q = mp.cbrt(inverse_beta(third,third,1-t))
                delta = 1-q
            sample.append((delta,q,dr*h,dr*dh))
    return sample


def side_disk(x):
    """Angular offset from the nearer prevertex and dt/d(arclength)."""
    a,b = mp.mpf(1)/6,mp.mpf(1)/2
    if x == b:
        return mp.pi/3,2*mp.beta(a,b)/3
    y = inverse_beta(a,b,2*min(x,1-x))
    return (2*mp.asin(mp.sqrt(y))/3, 2*mp.beta(a,b)*mp.cbrt(y)/3)


def boundary_modes(x, sample):
    """Balayage of (5), followed by the disk realification (6), on all three edges."""
    t, speed = side_disk(x)
    near,sgn = (0,1) if x<=mp.mpf('.5') else (1,-1)
    base = mp.mpf(0)
    deriv = mp.mpc(0)
    for j in range(3):
        angle = (near-j)*2*mp.pi/3+sgn*t
        sinhalf2, sint = 4*mp.sin(angle/2)**2, mp.sin(angle)
        real = mp.mpf(0)
        imag = mp.mpc(0)
        for delta,q,h,dh in sample:
            denominator = delta*delta+q*sinhalf2
            p = delta*(1+q)/denominator
            conjugate = -2*q*sint/denominator
            real += h*p
            imag += dh*mp.mpc(p,conjugate)
        base += real
        deriv -= imag*mp.exp(-mp.j*(mp.pi/6+2*j*mp.pi/3))
    factor = speed/(2*mp.pi)
    # For the two derivative modes use Re(D) and Re(iD) after rotating the edge.
    deriv *= factor
    rot = [deriv*mp.exp(-mp.j*2*j*mp.pi/3) for j in range(3)]
    return [base*factor]+[z.real for z in rot]+[-z.imag for z in rot]


def triangle_rows(n, x):
    # Reduction by the three exact rotations preserves the minimum norm.
    # Both sine and cosine rows are present. No reflection constraint is imposed.
    apex = .5+np.sqrt(3)*.5j
    v = np.array([0,1,apex])
    m = (2j*np.pi*np.arange(1,n+1))[:,None]
    trace = sum(np.exp(m*(z+d*x)) for z,d in zip(v, np.roll(v,-1)-v))
    return np.vstack((np.full(len(x),3.),trace.real,trace.imag))


def projection(n, x, reference):
    q,w = special.roots_legendre(5*n+60)
    nodes,weights = (q+1)/2,w/2
    D = triangle_rows(n,nodes)
    dw = D*np.sqrt(weights)
    b = np.zeros(len(D)); b[0]=1
    coeff = la.solve(dw@dw.T,b,assume_a='pos')
    projected = coeff@triangle_rows(n,x)
    gq = coeff@D
    defect = np.max(np.abs(D@(weights*gq)-b))
    assert defect < 3e-12
    err = np.abs(projected-reference)
    inside = (x>=.05)&(x<=.95)
    # Estimate the L² boundary discrepancy by integrating on a uniform sqrt(x) mesh.
    l2 = np.sqrt(3*np.trapezoid(err*err,x))
    return projected, {'N':n,'gauss_order':len(q),'constraint_residual':float(defect),
           'max_all_listed_points':float(max(err)), 'max_on_005_095':float(max(err[inside])),
           'boundary_L2_trapezoid':float(l2),'midpoint':float(projected[len(x)//2])}


def direct_cauchy_check(gamma, vertices, coeff):
    """Evaluate the original, undeformed Laplace integral (5) outside the base."""
    z = mp.mpc('.37','-1.25')
    T = mp.mpf(100)
    R = 1/mp.sqrt(3)
    ctr = sum(vertices)/3
    # The tail is bounded by a polynomial times exp(-1.25*T) on this ray.
    def original(t):
        return mp.j*gamma(mp.j*t)*mp.exp(-mp.j*t*z)
    residual = []
    for n in (0,1):
        direct = mp.quad(lambda t: (mp.j*t)**n*original(t),[0,6,16,36,65,T])
        transformed = mp.mpc(0)
        for v in vertices:
            u = (ctr-v)/R
            transformed += mp.quad(lambda y: 2*y*y*mp.polyval(coeff[::-1],y**6)/
                                   (z-v-u*y*y)**(n+1),[0,mp.sqrt(R)])
        residual.append(abs(direct-transformed))
    assert max(residual)<mp.mpf('1e-40')
    return mp.nstr(max(residual),9)


def boundary_transform_check(sample, vertices, gamma):
    """Integrate the real reconstructed boundary profiles, after x=u²/2 desingularization."""
    r,q,wh,wdh = np.asarray(sample,dtype=float).T
    nodes,weights = special.roots_legendre(80)
    u = (1+nodes)/2
    x = u*u/2
    wt = weights*u/2
    y = special.betaincinv(1/6,.5,2*x)
    t = 2*np.arcsin(np.sqrt(y))/3
    speed = 2*special.beta(1/6,.5)*np.cbrt(y)/3
    v = np.asarray(vertices,dtype=complex)
    streams,zs,ws = [],[],[]
    for side in range(3):
        for near,sign in ((0,1),(1,-1)):
            base = np.zeros(len(x)); deriv = np.zeros(len(x),complex)
            for j in range(3):
                angle = (near-j)*2*np.pi/3+sign*t[:,None]
                den = r*r+4*q*np.sin(angle/2)**2
                poisson = r*(1+q)/den
                base += poisson@wh
                deriv -= np.exp(-1j*(np.pi/6+2*np.pi*(j+side)/3))*(
                      (poisson-2j*q*np.sin(angle)/den)@wdh)
            streams.append(np.array([base,deriv.real,-deriv.imag])*speed/(2*np.pi))
            zs.extend(v[side]+(v[(side+1)%3]-v[side])*(x if near==0 else 1-x))
            ws.extend(wt)
    values = np.hstack(streams)
    maximum = 0
    for s in [0,.91-.52j,-4+1.5j]+[2*np.pi*1j*m/d for d in edges(v) for m in (1,3,8)]:
        anchor = max(v,key=lambda z:(s*z).real)
        predicted = complex(gamma(complex(s)))*np.exp(-s*anchor)*np.array([1,s,1j*s])
        observed = values@(np.asarray(ws)*np.exp(s*(np.asarray(zs)-anchor)))
        maximum=max(maximum,float(max(abs(observed-predicted))))
    assert maximum<3e-12
    return maximum


def triangle_probe():
    with mp.workdps(55):
        # Grid specified in decimal arithmetic with both endpoints excluded.
        half = {mp.mpf(j)/400 for j in range(1,201)}
        half.update(mp.mpf(10)**(-mp.mpf(j)/10) for j in range(4,81))
        left = sorted(half)
        xmp = left+[1-t for t in reversed(left) if t<mp.mpf('.5')]
        sample = median_quadrature(50,195,19)
        R = 1/mp.sqrt(3)
        coeff = skeleton_coefficients(180)
        centroid_mass = 3*mp.fsum(a*R**(3*j+mp.mpf('1.5'))/(3*j+mp.mpf('1.5'))
                                    for j,a in enumerate(coeff))
        assert abs(centroid_mass-1) < mp.mpf('1e-42')
        # Compute both halves separately. Rotation is used only to obtain the other edges.
        profiles = []
        for j,t in enumerate(xmp):
            profiles.append(boundary_modes(t,sample))
        digits = 27
        dec = np.array([[mp.nstr(z,digits) for z in row] for row in profiles])
        x = np.array([float(t) for t in xmp]); modes = dec.astype(float)
        mirror = max(abs(a[0]-b[0]) for a,b in zip(profiles,reversed(profiles)))
        assert mirror < mp.mpf('1e-36')
        check_nodes = [mp.mpf(s) for s in ('1e-8','.0003','.057','.25','.5','.873')]
        refined = median_quadrature(66,228,21)
        relative = max(abs(a-b)/max(abs(b),mp.mpf('.001')) for t in check_nodes
                       for a,b in zip(boundary_modes(t,sample),boundary_modes(t,refined)))
        print('triangle quadrature refinement',mp.nstr(relative,8),flush=True)
        assert relative < mp.mpf('1e-24')
        # The full Gamma transform independently checks the three complex median jumps.
        v = (mp.mpc(0),mp.mpc(1),mp.mpc('.5',mp.sqrt(3)/2))
        ctr = sum(v)/3
        gamma = GammaSymbol(v)
        residuals = []
        for s in (mp.mpc('.91','-.52'),2*mp.pi*mp.j,mp.mpc('-4','1.5')):
            sums = [mp.mpc(0)]*3
            for z in v:
                u = (ctr-z)/R
                def radial(r):
                    return mp.exp(s*(z+u*r*r))
                for ix,mult in enumerate((1,-1/u,-mp.j/u)):
                    polynomial = coeff if ix==0 else [(3*j+mp.mpf('.5'))*c for j,c in enumerate(coeff)]
                    value = mp.quad(lambda y: 2*(y*y if ix==0 else 1)*radial(y)*
                                    mp.polyval(polynomial[::-1],y**6),[0,mp.sqrt(R)])
                    sums[ix] += mult*value
            residuals.extend(abs(a-b*gamma(s)) for a,b in zip(sums,(1,s,mp.j*s)))
        assert max(residuals) < mp.mpf('1e-40')
        cauchy_error = direct_cauchy_check(gamma,v,coeff)
        boundary_error = boundary_transform_check(sample,v,gamma)
        ref = modes[:,0]
        proj, checks = [],[]
        for n in (48,192,768):
            vals, stats = projection(n,x,ref)
            proj.append(vals); checks.append(stats)
            print('triangle projection',stats,flush=True)
        assert checks[-1]['boundary_L2_trapezoid'] < checks[0]['boundary_L2_trapezoid']/8
        assert min(ref)>0 and abs(ref[0]/np.sqrt(x[0])-np.sqrt(2/np.pi)) < 1e-8
        corner = []
        for q in (mp.mpf(1),mp.j):
            corner.append([[float(-2/mp.sqrt(mp.pi)*mp.re(q*mp.exp(-mp.j*(mp.pi/6+
                           2*j*mp.pi/3+sgn*5*mp.pi/12)))) for sgn in (1,-1)] for j in range(3)])
        for band in range(2):
            for vertex in range(3):
                out = modes[0,1+3*band+vertex]*np.sqrt(x[0])
                inc = modes[-1,1+3*band+(vertex-1)%3]*np.sqrt(x[0])
                assert max(abs(out-corner[band][vertex][0]),abs(inc-corner[band][vertex][1])) < 1e-8
        directory = ROOT/'data'
        directory.mkdir(exist_ok=True)
        np.savez_compressed(directory/'phase3_triangle.npz',x=x, x_decimal=np.array([mp.nstr(t,digits) for t in xmp]),
             g_L2=ref, g_s=modes[:,1:4].T, g_is=modes[:,4:7].T,
             profiles_decimal=dec, projection=np.array(proj), projection_N=[48,192,768],
             vertices=np.array(v,dtype=complex), corner_coefficients=np.array(corner))
        summary = {'boundary_file':'data/phase3_triangle.npz','points_per_edge':len(x),
                 'decimal_columns':['g_L2','g_s_0','g_s_1','g_s_2','g_is_0','g_is_1','g_is_2'],
                 'quadrature_check_relative':mp.nstr(relative,8), 'gamma_transform_max_error':mp.nstr(max(residuals),8),
                 'median_mass_error':mp.nstr(abs(centroid_mass-1),8),'mirror_max_error':mp.nstr(mirror,8),
                 'projection':checks,'leading_sibling_out_in':corner,'values':{}}
        for key in ('1e-8','1e-6','.0001','.01','.1','.25','.5'):
            t = mp.mpf(key); j = min(range(len(xmp)), key=lambda j:abs(xmp[j]-t))
            summary['values'][key] = [mp.nstr(z,22) for z in profiles[j]]
        sel = x<=1.e-4
        numerical_exponents = [float(np.polyfit(np.log(x[sel]),np.log(np.abs(col[sel])),1)[0])
                               for col in modes.T]
        assert max(abs(np.array(numerical_exponents)-np.array([.5]+[-.5]*6)))<1e-5
        summary.update({'boundary_transform_max_error':boundary_error,
                        'direct_cauchy_max_error':cauchy_error,
                        'corner_fitted_exponents':numerical_exponents,
                        'x_decimal':[mp.nstr(t,digits) for t in xmp],
                        'profiles_decimal':dec.tolist(),'projection_profiles':np.array(proj).tolist()})
        return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', choices=['all','rhombus','square','tilt','triangle'], nargs='?', default='all')
    parser.add_argument('--dps', type=int, default=100)
    parser.add_argument('--section-output', type=Path)
    args = parser.parse_args()
    results = {}
    for name in ('rhombus','square','tilt','triangle'):
        if args.part not in ('all',name):
            continue
        if name == 'rhombus':
            low = rhombus(args.dps)
            high = rhombus(args.dps+32)
            assert low==high, 'Revisit the 45-digit output rounding or increase precision'
            risks = np.asarray(high,float)
            n = np.asarray(BANDS)
            scaled = risks*n[:,None]**[5/6,2/3,5/6,2/3]
            slope = -np.polyfit(np.log(n),np.log(risks),1)[0]
            results[name] = {'N':BANDS,'risks':high,'digits_crosschecked':[args.dps,args.dps+32],
                  'vertices':['0','1','1+exp(i*pi/3)','exp(i*pi/3)'],
                  'scaled':scaled.tolist(),'fitted_exponents':slope.tolist()}
        elif name == 'square':
            results[name] = square_curve()
        elif name == 'tilt':
            results[name] = tilt_curve()
        else:
            results[name] = triangle_probe()
    if args.part!='all' and args.section_output is None:
        print(json.dumps(results,indent=2,allow_nan=False))
    else:
        path = args.section_output or ROOT/'phase3_data.json'
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile(mode='w',dir=path.parent,delete=False) as output:
            json.dump(results,output,indent=2,allow_nan=False)
            output.write('\n')
        Path(output.name).replace(path)
        print('Saved',path)
