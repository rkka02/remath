## Executive referee verdict

**REVISIONS REQUIRED (2 critical, 11 moderate, 8 minor).**

Twenty of the 40 Round 1 items close. Twenty retain a finding at the severity shown below, and the bibliography has one additional minor finding. The two publication blockers are the proof of Paper 1, Theorem 3.1, and a Korean sentence that gives the opposite of the proved phase-flip result.

Paper 2’s Common Fund feasibility and limit-order repairs pass. All ten publication figures match the images embedded in the PDFs pixel-for-pixel. The Lean axiom audit also passes.

## Itemized resolution audit

Line references use **P1** for :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.tex" purpose="source"}, **P2** for :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex" purpose="source"}, **KR** for :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/expository_kr/expository_tsetlin_kr.tex" purpose="source"}, and **Fig** for :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/experiments/generate_paper_figures.py" purpose="source"}. The IDs follow :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/codex_logs/phase4_referee_r1_output.md" purpose="source"}.

### C1–C5

**C1 — Critical.** The synchronized deterministic case at P1:178 passes. The two compulsory survey-\(D\) loss windows at P1:179 also pass, including \(B_P=0\). They give the aggregate numerator base \(\max(B_P,q_Pq_T/q_S)\). Two gaps remain in the nearest-neighbor proof on PDF page 5.

1. P1:174 uses a **lower** bound on \(Q_{MC_0}\) to infer that the mixed-state escape fraction toward \(D_0\) has exponent zero. P1:180 bounds the direct edge \(Q_{D_0C_0}\), leaving the indirect numerator term uncontrolled. Insert
   \[
   Q_{MC_0}\le e^{-n\min(H_T,H_S+H_P)+o(n)}
   \]
   and the \(H_P\) rate for \(Q_{D_0M}\) when the effective increments can disagree. The indirect branch then costs at least \(\min(H_P+H_T-H_S,2H_P)\), with \(2H_P\ge J\). At perfect \(DD\) synchrony, use the scalar first passage and, for \(B\), the fixed positive probability of two accepted shallow switches. [P1:174](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.tex:174)
2. P1:184 transfers the stopped-corner prefactor to the interacting game using a reflected-walk comparison proved for linear tactics under extra domination hypotheses. One is \(S\le1-P\). At the actual critical point \((R,P,T,S)=(.80,.70,.90,.60)\), \(\kappa_R=0,\ \kappa_P=13/63\), the mixed cooperator’s up-step probability is \(.60\), while the proposed dominating coordinate’s is \(.30\). The cited coupling therefore fails inside the theorem’s domain. Use the general first-switch bound, sum over the surviving defector’s remaining distance, and transfer trace occupation to profile occupation. At independence use the separate product-kernel estimate. For \(K\), use the thinned increment law throughout. [P1:184](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.tex:184)

The restricted comparison states its hypotheses at line 5 of :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/docs/phase1_square_prefactor.md" purpose="source"}. The general repair is available at lines 132, 175–181, 194–196, and 212–254 of :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/docs/phase1_architectures.md" purpose="source"}.

**C2 — Closed.** Theorem 4.2(1) states feasibility exactly as \(R_n(c)\ge r_\theta\), strict increase of \(A_n\) over feasible depths, and eventual feasibility for \(p_*>1/2\). On the one-quarter benchmark, \(R_1(c)=21>3=r_\theta\), so every depth is feasible. The Round 1 counterexample has \(R_1(c)=1.5<3\) and is correctly excluded. [P2:283](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex:283)

**C3 — Closed.** Deep-memory quorum loss is restricted to the one-quarter benchmark with \(N\to\infty\) first. The separate fixed-\(N\) statement \(W_{4,n}(.99)\to.82\) is accurate. The fixed-four proof gives \(\Pr(k\ne1)=O(n^2(20/21)^n)\). Its citation needs the correction recorded once under M19. [P2:292](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex:292)

**C4 — Critical.** The \(8{,}994.22447\times\) factor now correctly ends at **per-excursion escape** for \((60,20),R=.80,\kappa_P=.99\). Both architectures select \(DD\) in that game. The next sentence, also printed on Korean PDF page 4, says **“\(L\)은 0% 배신”**. In the separate \(R=.78,\gamma=2,\kappa_P=.99\) game, I obtain
\[
V_B=1.1538622793<h_R=1.2656663733<V_L=1.3834878238.
\]
Replace the outcome clause with **“\(L\)의 상호 협력률은 0%로, \(B\)의 상호 협력률은 100%로 수렴한다.”** The English corollary already gives the correct signs. [KR:169](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/expository_kr/expository_tsetlin_kr.tex:169) · [P1:304](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.tex:304)

**C5 — Minor.** The artwork passes. The legend gives unanimous defection \(\to1\), peer cooperation \(\to0\), and \(d>d_*\). The shading stops at \(d/h=1\), the arrow lands at \(0.945>8/9\) for \(N=10\), and the vertical axis names the requested ratio. The PDF caption gives the correct limits but omits which side of the curve produces each. Add “for \(d<d_*\)” after peer cooperation and “for \(d>d_*\)” after unanimous defection. [P2:154](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex:154) · [Fig:558](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/experiments/generate_paper_figures.py:558)

### M1–M12 · Paper 1 and the Korean feature

| ID | Status | Resolution or minimal repair |
|---|---|---|
| M1 | **Moderate** | **P1:215, 221, 228.** The variance, fixed window parameters, and positive-drift cap argument are present. The Neumann test at \(-1,1\) identifies the **signed** gap \(Z/n\) as uniform on \([-1,1]\). Apply \(\lvert Z\rvert/n=X/n+o_P(1)\) to get the stated law on \([0,1]\). The \(Z^2\) test bounds cap mass. Use the product test \(g(Z/n)v(Y)\) to establish independence and the unsigned Neumann test for the tilted window. The steps are at lines 93, 103, and 117 of :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/docs/phase1_weak_rewards.md" purpose="source"}. |
| M2 | **Moderate** | **P1:209, 224. KR:111, 143, 152.** The English theorem adds full support, but its negative-correlation clause uses an undefined \(E_1^K\). Define it from the effective Krylov law or omit that extension. Add full support at both symmetric profiles to the Korean general claim. On its own example \((.45,.20,.95,.10)\), setting \(\kappa_R=\kappa_P=1\) still gives \(R>F_K>F_D\), yet synchronized \(L\) has limiting \(CC\) mass \(6/7\). |
| M3 | Closed | **P1:198. KR:135–137.** I reproduced \(\pi_{80}^L(CC)=0.99999997054\) when both correlations are \(1/2\), and \(0.99999996663\) when only \(\kappa_P=1/2\). The joint-loss probability is correctly given as \(0.195\). |
| M4 | **Moderate** | **P1:198.** The Korean thresholds and equality outcomes are correct. The new English sentence says the move to \(1/2\) crosses both thresholds. In fact \(13/63<1/2<11/21\), and \(F_D(.70,.50)=.805>.80\). Say the move crosses the \(L,B\) threshold and that \(D\) joins strictly above \(11/21\). |
| M5 | **Moderate** | **P1:244–249, 266. KR:166.** The second derivative \(2C_\gamma\), supremum, and leading-order tip expansion pass. Qualify the endpoint-collapse claim by aspect ratio. In the paper’s game at \(\gamma=1.1\), both endpoints select \(CC\). Also reserve uniqueness at \(\kappa_*\) for *minimum escape cost*. At independence, \(46.927\%\) of successful \((60,20)\) linear excursions already have simultaneous first switches. |
| M6 | **Moderate** | **P1:237, 277, 285, 433.** The synchronized value, negative-\(\kappa_P\) linear formula, proved \(B\) subregions, and \(\Phi_u(1)=1\) pass. Line 277 still announces an ordinary limit across the stated domain, including the negative-\(\kappa_P\) region for \(B\) listed as open at line 433. Begin “In each of the following proved cases.” Use the already defined \(D(s,v)\) at line 285 or identify \(M=D\) there. |
| M7 | Closed | **P1:270, 287, 291.** Strict truncation is distinguished from first contact. The first-return transform includes the \(B\) holds. Its convexity and its values below one at \(h_P\) and equal to one at the active cutoff give positive longitudinal drift. |
| M8 | **Minor** | **P1:354, 358.** The negative-correlation ordering and zero-horizontal-drift support tilt are fixed. The reflection factor \(2(\ell+1)/(j+\ell+2)\) allows earlier visits to \(X=m\). Replace “strictly left of \(X=m\)” with “at or below \(X=m\).” For \(\ell=1,j=3\), the weak and strict fractions are \(2/3\) and \(1/3\). |
| M9 | Closed | **P1:299, 304. KR:130, 169.** Conditional ever-hit probabilities, expected visit counts, terminal corner entry, and simultaneous first switches now have distinct labels. The last two probabilities at \(2/3\) are \(91.97\%\) and \(36.85\%\), respectively. |
| M10 | **Minor** | **KR:202, 211.** The symbolic cancellation and limiting statement pass. Add \(M=N=4096\) to the finite value \(0.9995\). At the same \(N\) with \(M=3N\), the ratio is \(1.00025105\). P1:421 gives both correctly. |
| M11 | Closed | **P1:414.** The tensor factors are substochastic transition matrices. The displayed exit-time transform is assigned to \(L\), and the shallow-state remaining means \(2N\) and \(4N\) justify the shared diffusive limit. |
| M12 | Closed | **P1:421–422. Fig:441–445.** Both immediate-switch series are plotted. The square finite values are \(2.18790570\) and \(2.18683781\), against limit \(2.18843962\). Both aspect-three values round to \(0.1129\). |

### M13–M24 · Paper 2, figures, and verification claims

| ID | Status | Resolution or minimal repair |
|---|---|---|
| M13 | Closed | **P2:134, 140.** Exact graph enumeration gives 80 recurrent states at \((40,40)\) and 6,560 at \((41,40)\). The two certificates and the entry depths needed by the block argument are correctly assigned. |
| M14 | Closed | **P2:209–211.** \(h_C\) and \(h_D\) now start on opposite sides of the interface. Substitution of \(h_D=\rho_P h_C\) gives the printed transmission identity. |
| M15 | **Moderate** | **KR:195. P2:192, 200, 215.** The English theorem has the right \(\delta_j>0,\ b_j\to b<1\) hypotheses and continuous \(b_j=0\) value. The Korean parenthesis still identifies subcriticality with \(\delta>0\). Above the fair line it requires \(a\lambda<1\). Taking \(\lambda=e^{-\delta}\), \(a=e^{2\delta}\) gives \(\delta>0\) and \(a\lambda>1\). Write \(R<R_c(P,S)\). At P2:215, the bound \(\delta G_n\lambda^n\le x e^{-(1-\max(0,b_j))x}\), \(x=\delta n\), supplies the claimed compactness at both ends. |
| M16 | **Moderate** | **P2:222. Fig:596–600.** The legend distinguishes sampled maxima and endpoints, including the red trace at \(80.3\%\). The caption still says all curves “peak between \(76\%\) and \(83\%\).” For \((S,R)=(.52,.935)\) I obtain **\(83.0366886755461\%\) at \(n=18\)**. The plotted \(n=16\) value is \(82.9896523519\%\). Write “the displayed samples reach approximately \(76\%\)–\(83\%\).” |
| M17 | Closed | **P2:239–244. KR:221–226.** The pivotal condition is a weak inequality intersected with \([0,1]\). The Korean benchmark identifies the large-population limit for quota concentration, provision, and welfare. |
| M18 | **Minor** | **P2:270.** The exponential tilt, \(O(\log N)\) return window, and drift estimate establish the claimed rate. Set the tilted mean to \(\min(\mu,N\theta-2\sqrt N)\). When \(\mu\) is already below the target, zero tilt and Chebyshev give the lower bound directly. |
| M19 | **Minor** | **P2:303.** The stationary argument now uses the mean empirical vector, and the cited notes support the depth-two and depth-three results. The same citation incorrectly assigns the fixed-four proof to those notes. Cite lines 69–78 of :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/codex_logs/phase2_verify_r2_output.md" purpose="source"} for \(W_{4,n}(.99)\to.82\). |
| M20 | **Moderate** | **P2:298.** Both radius-\(10^{-80}\) contraction certificates reproduce at \(\alpha=.70\), with norm bounds \(18/25\) and \(17/20\). The certified map is the **third iterate** on the two coordinates \((x_{t-1},x_t)\). Replace “two-step return map” with “three-step return map on two successive cooperation fractions.” The three branch updates and Jacobian products are at lines 412–422 of :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/experiments/phase2b_quorum_memory.py" purpose="source"}. |
| M21 | Closed | **P2:309.** The rational witness is described as bistability. The two-player values are identified as strict-phase cooperation thresholds. |
| M22 | **Minor** | **KR:244. Fig:164, 1048.** P2:316 gives the finite trajectory protocol correctly. Add “800 burn-in steps, then a 120-step average” to the Korean caption and replace “Long-run average” in the generator helper with “finite trajectory average.” |
| M23 | **Moderate** | **KR:253. Fig:23, 185.** The recomputed rational payoff-enclosure widths are \(3.9983\times10^{-70}\) and \(1.75749\times10^{-66}\). The Korean bound “both \(\le10^{-66}\)” fails for \((41,40)\). Give the two widths printed at P2:134 or use \(<2\times10^{-66}\). Replace the blanket working-precision range with per-dataset values. The escape grids used 150 working digits and the Stag Hunt grid reached 434. Describe the generator’s 80-digit GTH sweeps as working precision. |
| M24 | **Minor** | **KR:249, 253. P1:428. P2:323.** The verification paragraphs correctly distinguish 911 theorem constants from 1,168 declarations and identify the formalized results. The Korean heading still advertises “100% 기계 검증” for the study. Scope the heading to the proved algebraic results, for example **“핵심 대수 정리의 Lean 검증”**. |

### M25–M30 · Primary sources and bibliography

| ID | Status | Resolution or minimal repair |
|---|---|---|
| M25 | **Moderate** | **P1:65. KR:217.** The historical discussion now credits Pittel, unequal-memory work, full averaging, and teams of automata. Correct the precise Tsetlin citation. Section 5, equations (17)–(20), defines the joint law, marginals, and independent-outcome construction. The explicit one-wins/one-loses model is in **§6**, p. 23 of the Russian original. In KR:217 distinguish the 1963 introduction from the 1964 placement experiments, as P2:67 already does. [Tsetlin’s survey](https://www.mathnet.ru/links/06d903a391036955593b6f9a3c688e2b/rm6373_eng.pdf) |
| M26 | **Moderate** | **P1:80–81, 451. KR:142.** The transition rule and the qualification about Volkonskii’s omitted comparison proof are repaired. The new `Krinskii1964` entry has the wrong title. Replace it with *On a construction of a sequence of automata and its behavior in games*. The volume, issue, pages, and identifier already match. [Publisher’s contents](https://www.mathnet.ru/php/archive.phtml?jrnid=dan&option_lang=eng&viewarchiveID=8&vl=156&wshow=contents) · [Original paper](https://www.mathnet.ru/links/924d02763b1538399a9c006b249049ab/dan29756.pdf) |
| M27 | Closed | **P1:463. P2:351.** `Krinskii1966` has the correct title, Russian pages 43–53, and translation pages 33–41. [Publisher record](https://www.mathnet.ru/php/archive.phtml?jrnid=ppi&option_lang=eng&paperid=1933&wshow=paper) |
| M28 | Closed | **P1:472.** `Jiao2021` correctly identifies Jiao, Zhang, and Granmo’s AND/OR preprint. [Author record](https://arxiv.org/abs/2109.09488) |
| M29 | Closed | **P1:475.** `Belaid2023` has the correct title, first-author initials, six-author order, and identifier. [Author record](https://arxiv.org/abs/2310.02005) |
| M30 | Closed | **P1:478.** `DJR2019` correctly identifies the logarithmic-asymptotics paper, *Risks* 7(3), article 83, arXiv:1906.09347. [Author record](https://arxiv.org/abs/1906.09347) |

**N1 — New minor finding.** `Gurvich1975` combines the English volume number with the Russian journal and pagination. Use *Avtomat. i Telemekh.*, **1975, no. 2, 80–94**, or give the English translation as *Automation and Remote Control* **36(2), 257–270**. The publisher’s English title is *Method for asymptotic investigation of games between automata*. [P1:466](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.tex:466) · [Publisher record](https://www.mathnet.ru/php/archive.phtml?jrnid=at&option_lang=eng&paperid=7793&wshow=paper)

### S1–S5

| ID | Status | Verification |
|---|---|---|
| S1 | Closed | **P2:53, 107, 153. Fig:533.** One additional depth per action correctly takes the machine from 80 to 82 internal states. |
| S2 | Closed | **P1:354.** The boundary denominator is correctly called a squared-Catalan-number series. |
| S3 | Closed | **KR:139.** The Korean reference agrees with the compiled numbering, Paper 1, Theorem 3.1. |
| S4 | Closed | **P2:288.** The compiled \(n_c=2\) is bold and the literal Markdown asterisks are gone. |
| S5 | Closed | **P1:298. Fig:339, 356–358, 859, 878–880.** Both plots identify the sampled range starting at \(-.30\) and attach the independence observation to \(\kappa_P=0\). |

## Final publication readiness sign-off

**Publication sign-off withheld.** Paper 1 needs the general trace and occupation argument under its stated hypotheses. The Korean feature needs the corrected \(L\) outcome. Paper 2’s Common Fund conclusions survive re-verification, including the fixed-four result and both locally attracting period-three cycles.

I inspected all **32 PDF pages** and compared all **10** figures from in-memory generator output through publication PNG to embedded PDF raster. All ten matched exactly. The page review found no visible clipping, unresolved references, or remaining literal Markdown markers. The numerical checks also reproduced all 134 aspect-ratio boundary values and all 20 finite fair-game spectra. The reviewed PDFs were :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper1_correlated_automata/paper1_correlated_automata.pdf" purpose="source"}, :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.pdf" purpose="source"}, and :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/papers/expository_kr/expository_tsetlin_kr.pdf" purpose="source"}.

Lean 4.36.0 checked the five module sources and the audit entry point using the existing compiled imports. The audit passed for **911 theorem constants among 1,168 declarations**, with zero `sorry` and only the three permitted standard axioms. Strict read-only mode was preserved throughout. Fresh Tectonic and clean Lake build logs remain unverified. :codex-file-citation{path="/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/Main.lean" purpose="source"}