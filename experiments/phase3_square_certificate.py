"""Global, outward-rounded finite-band square-shift certificate for Phase 3.

The Chebyshev interpolation encloses an entire bordered determinant and a
diagonal cofactor. Integer arithmetic verifies the small Schur determinants.
"""
import math

import mpmath as mp
import numpy as np
from mpmath.libmp import mpf_shift, to_int, round_floor, round_ceiling

iv = mp.iv
BITS = 600
SCALE = 1 << BITS
DIRECTIONS = (1,1j,-1,-1j)


def fixed(x):
    lo,hi = x._mpi_
    a = to_int(mpf_shift(lo,BITS),round_floor)
    b = to_int(mpf_shift(hi,BITS),round_ceiling)
    assert b-a <= 2, 'insufficient working precision for fixed-point enclosure'
    return a


def bareiss(a):
    """Exact integer determinant with pivoting and exact divisions."""
    v = a.copy().tolist()
    sign, prev = 1,1
    for i in range(len(v)-1):
        if not v[i][i]:
            j = next((j for j in range(i+1,len(v)) if v[j][i]),None)
            if j is None:
                return 0
            v[i],v[j] = v[j],v[i]
            sign = -sign
        pivot = v[i][i]
        for j in range(i+1,len(v)):
            for k in range(i+1,len(v)):
                v[j][k] = (v[j][k]*pivot-v[j][i]*v[i][k])//prev
        prev = pivot
    return sign*v[-1][-1]


def det_ball(a, error):
    n = len(a)
    height = (max(abs(z) for z in a.flat)+error+SCALE-1)//SCALE
    radius = iv.mpf(n*math.factorial(n)*height**(n-1)*error)/SCALE
    center = iv.mpf(bareiss(a))/SCALE**n
    return center+iv.mpf([-1,1])*radius


class SquareDeterminants:
    def __init__(self,n):
        self.n = n
        self.twopi = 2*iv.pi
        self.expint = [iv.exp(-self.twopi*j) for j in range(n+1)]
        self.integer = []
        for j in range(4):
            for m in range(1,n+1):
                dec = self.expint[m]
                phases = [iv.mpc(1 if (k-j)%4<2 else dec) for k in range(4)]
                self.integer.append((m/DIRECTIONS[j],0j,phases))
        self.recip = {}
        nb = 8*n
        C = iv.matrix(nb+3)
        x = iv.mpf(0)
        for j,r in enumerate(self.integer):
            for k in range(3):
                C[2*j,nb+k]=C[nb+k,2*j]=r[2][k].real
                C[2*j+1,nb+k]=C[nb+k,2*j+1]=r[2][k].imag
            for l in range(j+1):
                block = self.block(r,self.integer[l],x,{})
                for a in (0,1):
                    for b in (0,1):
                        C[2*j+a,2*l+b]=C[2*l+b,2*j+a]=block[a][b]
        assert iv.det(C) < -iv.mpf('1e-8')
        inv = C**-1
        self.inverse = np.array([[fixed(inv[i,j]) for j in range(nb+3)]
                                                for i in range(nb+3)],dtype=object)
        self.invbound = max(abs(v) for v in self.inverse.flat)//SCALE+2

    def block(self,r,t,x,local):
        a,b,v = r
        c,e,w = t
        plain,herm = iv.mpc(0),iv.mpc(0)
        for j,d in enumerate(DIRECTIONS):
            k = (j+1)%4
            u,h = (a+c)*d,(b+e)*d
            p,q = a*d-(c*d).conjugate(),b*d-(e*d).conjugate()
            def integral(k0,k1,start,end):
                if k0==0 and k1==0:
                    return start
                cache = local if k1 else self.recip
                key = (k0,k1)
                if key not in cache:
                    div = iv.mpc(k0.real,k0.imag)+iv.mpc(k1.real,k1.imag)*x
                    cache[key] = 1/(iv.j*self.twopi*div)
                return (end-start)*cache[key]
            plain += integral(u,h,v[j]*w[j],v[k]*w[k])
            herm += integral(p,q,v[j]*iv.mpc(w[j].real,-w[j].imag),v[k]*iv.mpc(w[k].real,-w[k].imag))
        return [[(herm+plain).real/2,(plain-herm).imag/2],
                [(plain+herm).imag/2,(herm-plain).real/2]]

    def __call__(self,x):
        n = self.n
        local = {}
        osc = iv.exp(iv.j*self.twopi*x)
        decay = iv.exp(-self.twopi*x)
        shifted = [(m+0j,1+0j,[iv.mpc(1),osc,osc*decay*self.expint[m],
                                  iv.mpc(decay*self.expint[m])]) for m in range(n)]
        nb, ns = 8*n,2*n
        X = np.zeros((nb+3,ns+2),dtype=object)
        X[nb,ns+1] = SCALE
        Y = np.zeros((ns+2,ns+2),dtype=object)
        for i,r in enumerate(self.integer):
            X[2*i,ns],X[2*i+1,ns] = fixed(r[2][3].real),fixed(r[2][3].imag)
        for j,r in enumerate(shifted):
            for i,t in enumerate(self.integer):
                block = self.block(t,r,x,local)
                for a in (0,1):
                    for b in (0,1):
                        X[2*i+a,2*j+b] = fixed(block[a][b])
            for i in range(3):
                X[nb+i,2*j],X[nb+i,2*j+1] = fixed(r[2][i].real),fixed(r[2][i].imag)
            Y[2*j,ns]=Y[ns,2*j]=fixed(r[2][3].real)
            Y[2*j+1,ns]=Y[ns,2*j+1]=fixed(r[2][3].imag)
            for l in range(j+1):
                block = self.block(r,shifted[l],x,local)
                for a in (0,1):
                    for b in (0,1):
                        Y[2*j+a,2*l+b]=Y[2*l+b,2*j+a]=fixed(block[a][b])
        schur = Y-(X.T@self.inverse@X)//(SCALE*SCALE)
        xb = max(abs(v) for v in X.flat)//SCALE+2
        # Each matrix input differs from its dyadic representative by at most 2 ulps.
        err = 3+2*(nb+3)**2*(2*xb*self.invbound+xb*xb)
        norm = x**(4*n-2)*(1-x)**(4*n)
        return (det_ball(schur[:ns,:ns],err)/norm,
                -det_ball(schur[:ns+1,:ns+1],err)/norm, -det_ball(schur,err)/norm)


def polyadd(a,b,sign=1):
    n = max(len(a),len(b))
    return [(a[j] if j<len(a) else 0)+sign*(b[j] if j<len(b) else 0) for j in range(n)]


def polymul(a,b):
    p = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            p[i+j] += x*y
    return p


def derivative(a):
    return [j*a[j] for j in range(1,len(a))]


def cheb_to_power(c):
    # T_j(2 theta - 1), with integer coefficients.
    t,prev = [1],[-1,2]
    v = [0]
    for z in c:
        v = polyadd(v,[z*x for x in t])
        t,prev = polyadd(polymul([-2,4],t),prev,-1),t
    return v


CBITS = 215
CSCALE = 1 << CBITS


def interpolate(n):
    # On the Bernstein ellipse rho=8 the distances to both endpoints exceed 1,
    # |theta| < 2.54, and each analytic shifted row has modulus < exp(23).
    # Factor exp(23) out of its row and column, then apply Hadamard's bound.
    degree = {1:150,2:220,4:352}[n]
    length = 10*n+5
    ceiling = math.isqrt(length)+1
    maximum = 10**8*(4*ceiling)**length*2**(134*n)
    cosine = [iv.cos(iv.pi*k/(2*degree)) for k in range(4*degree)]
    determinants = SquareDeterminants(n)
    values = [determinants((1+cosine[2*j+1])/2) for j in range(degree)]
    series = []
    for data in zip(*values):
        c = [iv.fsum(val*cosine[(k*(2*j+1))%(4*degree)] for j,val in enumerate(data))
             *((1 if k==0 else 2)/iv.mpf(degree)) for k in range(degree)]
        kept = 95
        dyadics = [to_int(mpf_shift(a._mpi_[0],CBITS),round_floor) for a in c[:kept]]
        errors,sizes = [],[]
        for q in range(3):
            # The interpolation alias of any T_k is zero or +/- a lower T_j.
            # Markov on [0,1] bounds its qth derivative by (2*k*k)^q.
            remainder = iv.mpf(8*maximum*(2*degree**2)**q)/8**degree
            errors.append(remainder+iv.fsum((2*k*k)**q*abs(
                 a-(iv.mpf(dyadics[k])/CSCALE if k<kept else 0)) for k,a in enumerate(c)))
            sizes.append(iv.fsum((2*k*k)**q*abs(z) for k,z in enumerate(dyadics))/CSCALE)
        series.append((cheb_to_power(dyadics),errors,sizes))
    return series


class Bernstein:
    def __init__(self,p,scale):
        n = len(p)-1
        factorials = [math.factorial(j) for j in range(n+1)]
        s = [a*factorials[j]*factorials[n-j] for j,a in enumerate(p)]
        self.b = [sum(s[j]*math.comb(i,j) for j in range(i+1)) for i in range(n+1)]
        self.den = factorials[n]*scale

    @staticmethod
    def split(b,den):
        # Subdivide exactly at the midpoint by de Casteljau's recurrence.
        left,right = [],[]
        n = len(b)-1
        for j in range(n,-1,-1):
            left.append(b[0]<<j); right.append(b[-1]<<j)
            b = [x+y for x,y in zip(b,b[1:])]
        return (left,den<<n),(right[::-1],den<<n)

    def signed(self, lo, hi, sign, error):
        """Certify a sign on a dyadic subinterval, including endpoints."""
        from fractions import Fraction
        lo,hi = Fraction(lo),Fraction(hi)
        def visit(b,den,left,right,depth):
            if right<=lo or left>=hi:
                return 0
            if min(sign*x for x in b)*error.denominator > den*error.numerator:
                return 1
            assert depth<35, ('sign certificate unresolved',float(left),float(right),sign)
            a,c = self.split(b,den)
            mid = (left+right)/2
            return visit(*a,left,mid,depth+1)+visit(*c,mid,right,depth+1)
        return visit(self.b,self.den,Fraction(0),Fraction(1),0)


def square_certificate(n):
    from fractions import Fraction
    iv.dps = 230
    (p,ep,sp),(d,ed,sd),(bottom,eb,_) = interpolate(n)
    def product_error(k,l):
        return ep[k]*(sd[l]+ed[l])+sp[k]*ed[l]
    h = polyadd(polymul(derivative(p),d),polymul(p,derivative(d)),-1)
    h1 = derivative(h)
    error = Fraction(1,10**36)
    bound = iv.mpf(error.numerator)/error.denominator
    assert product_error(1,0)+product_error(0,1)<bound
    assert product_error(2,0)+product_error(0,2)<bound
    assert ep[0]+eb[0]<bound
    assert ed[0]<bound
    hb = Bernstein(h,CSCALE**2)
    hprime = Bernstein(h1,CSCALE**2)
    gap = Bernstein(polyadd(p,bottom,-1),CSCALE)
    counts = []
    if n==1:
        # D has at least a double zero at 0 by the alternating atom column.
        # Thus H(0)=0. H'<0 in the first interval gives H<0 on its interior.
        cut = Fraction(1,64)
        counts += [hprime.signed(0,cut,-1,error), hb.signed(cut,1,-1,error),
                   gap.signed(Fraction(1,2),1,1,error)]
        lo=hi=Fraction(1)
    elif n==2:
        counts += [hb.signed(0,1,1,error),gap.signed(0,Fraction(1,8),1,error)]
        lo=hi=Fraction(0)
    else:
        lo,hi=Fraction(7,64),Fraction(1,8)
        counts += [hb.signed(0,lo,-1,error),hprime.signed(lo,hi,1,error),
                   hb.signed(hi,1,1,error),gap.signed(lo,hi,1,error)]
        def sign_at(t):
            z = Fraction(0)
            for a in reversed(h):
                z = z*t+a
            z /= CSCALE**2
            assert abs(z)>error
            return 1 if z>0 else -1
        assert sign_at(lo)<0<sign_at(hi)
        while hi-lo>Fraction(1,10**19):
            mid = (lo+hi)/2
            if sign_at(mid)<0:
                lo=mid
            else:
                hi=mid
    def value_at(poly, t):
        val = Fraction(0)
        for z in reversed(poly):
            val=val*t+z
        val /= CSCALE
        return iv.mpf(val.numerator)/val.denominator
    # Bound P and D over the root bracket from the midpoint, using a uniform
    # first derivative bound. All interval endpoints are rounded outwards.
    mid=(lo+hi)/2
    width=iv.mpf((hi-lo).numerator)/(hi-lo).denominator/2
    pv = value_at(p,mid)+iv.mpf([-1,1])*(ep[0]+width*(sp[1]+ep[1]))
    dv = value_at(d,mid)+iv.mpf([-1,1])*(ed[0]+width*(sd[1]+ed[1]))
    risk=iv.sqrt(pv/dv)
    def enclosure(ball,digits):
        scale=10**digits
        lo=to_int((ball*scale)._mpi_[0],round_floor)
        hi=to_int((ball*scale)._mpi_[1],round_ceiling)
        return [f'{k//scale}.{k%scale:0{digits}d}' for k in (lo,hi)]
    interval=iv.mpf(lo.numerator)/lo.denominator+iv.mpf([0,1])*2*width
    result = {'N':n, 'shift_bracket':enclosure(interval,20),
              'risk_bracket':enclosure(risk,17),'attained':n==4,
              'signed_bernstein_boxes':counts,
              'uniform_error_H_and_derivative':'1e-36'}
    print('square certificate',result,flush=True)
    return result


if __name__=='__main__':
    import argparse
    import json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n',type=int,choices=(1,2,4))
    parser.add_argument('--output')
    args=parser.parse_args()
    result=square_certificate(args.n)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
