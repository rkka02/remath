# The fair independent corner has a logarithmic correction

Let both rewards be fair, let the feedbacks be independent, and let the deficit barriers satisfy $m/n\to\gamma\ge1$. Start at the deepest pair $o=(0,0)$. The event reaches $c=(m,n)$ before a first positive return to $o$ or an action switch. Use the hard L boundary or the independent randomized B boundary. Write $w=0$ for L and $w=1/4$ for B. This is the one-round probability of holding at a shallow boundary on a declined loss.

**Theorem.** The per-excursion probability satisfies
$$
 h_{m,n}\sim \frac{\pi I(\gamma)}{4(1-2w)^2D_w}\,\frac{1}{n^2\log n},
 \qquad I(\gamma)=2\pi\sum_{k=0}^\infty
 \frac{(-1)^k(2k+1)}{\cosh((2k+1)\pi\gamma/2)} .
$$
Here $D_0=16/\pi-4$ and $D_{1/4}=(16/5)(4\log(3)/\pi-1)$. Both constants are also given by the convergent integral
$$
 D_w=\frac1\pi\int_0^\pi
 \left|\frac{F(e^{it})}{1-w e^{it}F(e^{it})}\right|^2\,dt,
 \qquad F(z)=\frac2{1+\sqrt{1-z^2}},
$$
using the principal square root. For equal barriers the respective coefficients of $1/(n^2\log n)$ simplify to
$$
 C_L=\frac{\Gamma(1/4)^4}{128(4-\pi)}=1.57260953586626338\ldots,\qquad
 C_B=\frac{5\Gamma(1/4)^4}{128(4\log3-\pi)}=5.38744691613048646\ldots .
$$

For a rectangle, let $K(k)$ denote the complete elliptic integral with modulus $k$, let $k'=\sqrt{1-k^2}$, and choose $K(k')/K(k)=\gamma$. The shape factor is $I(\gamma)=4kk'K(k)^2/\pi$. Indeed, differentiating the absolutely convergent Fourier series of $\operatorname{cn}(u,k)$ at $u=K(k)$ and using $\operatorname{cn}'(K(k),k)=-k'$ gives precisely the defining hyperbolic series. For $\gamma=1$ we have $k=k'=1/\sqrt2$ and $K(k)=\Gamma(1/4)^2/(4\sqrt\pi)$. [NIST DLMF, Jacobi Fourier series](https://dlmf.nist.gov/22.11.E2) · [Lemniscatic value of the complete integral](https://dlmf.nist.gov/23.5.E5)

## Three entries of a Green function

Let $A_L$ be the symmetric one-coordinate transition matrix on $0,\ldots,L$ for the hard walk, with probability $1/2$ of holding at 0 and killing on overflow. The soft matrix is $A_L+w e_L e_L^\top$. Independent feedback makes the square transition matrix the tensor product of the two one-dimensional matrices. Let $G$ be its Green matrix, summing over times before killing and including time zero. Its restriction to $\{o,c\}$ is the inverse of $I-Q$, where $Q$ is the transition matrix observed at successive visits to these two states before killing. Therefore
$$
 h_{m,n}=Q_{oc}=\frac{G_{oc}}{G_{oo}G_{cc}-G_{oc}^2}.
$$

For hard boundaries $G_{oo}\sim(4/\pi)\log n$. On the infinite half-line the probability of occupying 0 at time $j$ from 0 equals $p_j(0)+p_j(1)\sim\sqrt{2/(\pi j)}$, where $p_j$ is the simple symmetric walk kernel on the integers. This follows by folding at $-1/2$. Lower bounding the product sum up to $n^{2-\epsilon}$ costs an exponentially small error, by the maximal tail bound for reaching either distant barrier by then. Upper bound it by the uncapped sum through $n^2$. The remaining sum is $O_\gamma(1)$ since the one-coordinate spectral expansion below gives $A_L^j(0,0)\le C_\gamma L^{-1}\exp(-c j/L^2)$ at $j\ge n^2$ for $L=m,n$. Taking $\epsilon\downarrow0$ proves the equivalent.

Starting at $c$, the probability of reaching either deep boundary before killing is $O(1/n)$ by one-coordinate gambler's ruin. The same estimate holds for B by renewing at a declined first overflow. Every visit to $c$ has a killing probability in the next round bounded below independently of size. Thus $G_{cc}\to D_w$, the expected number of returns to the common endpoint of a pair of independent half-line walks, including time zero. In one dimension the hard endpoint has return generating function $F(z)$ by the Catalan path count. Adding a holding probability $w$ gives $F(z)/(1-wzF(z))$ by convolution. The sum of the squared return probabilities is the displayed integral by Parseval. For $w=0$, the sine spectral basis on the killed half-line gives $D_0=(4/\pi)\int_0^\pi\sin^2(t)/(1+\sin t)\,dt=16/\pi-4$.

For the B constant, the unperturbed endpoint resolvent in the spectral variable is $b(z)=2(z-\sqrt{z^2-1})$, with the square root chosen to agree with $z$ at infinity. The perturbed resolvent is $b/(1-wb)$, with no pole outside $[-1,1]$ since $|b|<2$ there. Taking imaginary parts on the cut multiplies the sine spectral density by $(1-4w\cos t+4w^2)^{-1}$. Integrate the endpoint generating function of the other coordinate at $\cos t$. For $w=1/4$ and $u=\tan(t/2)$ this gives
$$
 D_{1/4}=\frac{256}{\pi}\int_0^\infty
 \frac{u^2\,du}{(1+u^2)(1+9u^2)(1+u)(1+3u)}
 =\frac{256}{\pi}\left(\frac{\log3}{20}-\frac{\pi}{80}\right).
$$
The last integral follows by partial fractions.

## The transfer from the origin to the corner

For the hard short coordinate the eigenangles, eigenvectors, and squared norms are
$$
 \theta_k=\frac{(2k+1)\pi}{2n+3},\qquad
 f_k(x)=\cos((x+\tfrac12)\theta_k),\qquad
 \|f_k\|^2=(2n+3)/4,\quad 0\le k\le n .
$$
The eigenvalues are $\cos\theta_k$. Expand the short kernel and sum the long kernel in time. With $U_m(z)=\sum_{j\ge0}A_m^j(0,m)z^j$ this gives
$$
 G_{oc}=\sum_{k=0}^n\frac{4(-1)^k\cos(\theta_k/2)\sin\theta_k}{2n+3}
 U_m(\cos\theta_k).
$$
For $0<z\le1$ the one-coordinate overflow time has generating function $zU_m(z)/2$. Solving its scalar recursion gives
$$
 U_m(z)=\frac2z\frac{\cosh(\xi/2)}{\cosh((m+3/2)\xi)},\qquad
 \cosh\xi=1/z .
$$
For each fixed $k$, $U_m(\cos\theta_k)\to2/\cosh((2k+1)\pi\gamma/2)$. The coefficient multiplied by $n^2$ tends to $(-1)^k(2k+1)\pi$. For domination use $|U_m(z)|\le U_m(|z|)\le4e^{-m\xi}$, with $\xi\ge\min(\theta_k,\pi-\theta_k)$. Both spectral edges have a summable exponential bound times at most a linear factor in their index from the edge. At the negative edge, the additional factor $\cos(\theta_k/2)$ tends to zero for every fixed index from that edge. Thus $n^2G_{oc}\to I(\gamma)$. For $\gamma\ge1$ the terms of the alternating series decrease strictly in magnitude and its sum is positive.

To include the B boundary, add the one-coordinate holding term by its geometric resolvent series. In the time domain this convolves $A_L^j(0,L)$ with a nonnegative kernel $K_L$ of generating function
$$
 (1-wz[(I-zA_L)^{-1}]_{LL})^{-1}.
$$
The hard expected number of visits to $L$ from $L$ is exactly two. From each visit there is a one-half chance of immediate killing, and after a step down the walk returns to $L$ almost surely. Hence $K_L$ has total mass $(1-2w)^{-1}$. As $L\to\infty$ its coefficients converge at every fixed time, and the half-line limit has the same total mass since $F(1)=2$. This gives uniform tightness. For fixed shifts of the two endpoint kernels the limit of $n^2G_{oc}$ is still $I(\gamma)$. Expand the coordinate with the extra time steps. Its terms acquire a fixed power of $\cos\theta_k$, tending to one at the contributing edge. The identical argument with the coordinates interchanged handles the other order.

For domination uniformly in either shift, $\sup_j A_L^j(0,L)\le C/L^2$. Fold the walk on the integers and allow killing only at the outside edge adjacent to each of the two endpoint images. Reflection bounds their probabilities by $p_j(\ell)-p_j(\ell+2)$ at $\ell=L,L+1$. This difference equals $2(\ell+1)p_j(\ell)/(j+\ell+2)$ on the reachable parity and is at most $C/(\ell+1)^2$ by the binomial Gaussian bound. The other factor has time sum $U_L(1)=2$. Integrating against both tight kernels now gives $n^2G_{oc}\to I(\gamma)/(1-2w)^2$. Finally, the one-dimensional sum of the increases in the $00$ return probabilities under this perturbation is $w U_L(1)^2/(1-2w)$. In the product its effect on $G_{oo}$ is bounded by the sum of the two one-dimensional increases, since individual return probabilities are at most one. Substituting the three Green entries proves the theorem.

The independent spectral program uses a tridiagonal resolvent for the long coordinate and verifies small systems against exact rational state elimination. At barriers $(160,160)$ it gives $h=0.000010681412537396063320526\ldots$ for L and $0.000036102972477384315755757\ldots$ for B. At $(1024,1024)$ the respective values are $1.9955212358106589517968\times10^{-7}$ and $6.8220528875708986785359\times10^{-7}$. [75-digit numerical check](../experiments/phase1_fair_corner.py)
