// Sparse subtraction-free GTH reduction. phase2b_stationary.py supplies the
// single closed class, its elimination order and the exact rational kernel.
#include <gmpxx.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

using Real = mpf_class;
using Integer = mpz_class;
using Edge = std::pair<int, int>;  // destination and index of an exact weight

struct Column {
    std::vector<int> later;
    std::vector<Real> outgoing;  // k -> j, normalized after eliminating k
    std::vector<Real> incoming;  // j -> k at the time of elimination
    Real rate;
};

static void add_product(Real& result, const Real& a, const Real& b, Real& scratch) {
    if (mpf_sgn(a.get_mpf_t()) && mpf_sgn(b.get_mpf_t())) {
        mpf_mul(scratch.get_mpf_t(), a.get_mpf_t(), b.get_mpf_t());
        mpf_add(result.get_mpf_t(), result.get_mpf_t(), scratch.get_mpf_t());
    }
}

// A structural zero in either direction is allowed. The symbolic Cholesky
// pattern of the undirected support contains every possible directed fill.
static std::vector<Column> symbolic(const std::vector<std::vector<Edge>>& rows) {
    const int n = rows.size();
    std::vector<std::vector<int>> below(n);
    for (int i = 0; i < n; ++i)
        for (auto [j, index] : rows[i])
            below[std::max(i, j)].push_back(std::min(i, j));

    std::vector<Column> columns(n);
    std::vector<int> parent(n, n), seen(n, -1);
    for (int j = 0; j < n; ++j) {
        for (int k : below[j]) {
            while (k < j && seen[k] != j) {
                seen[k] = j;
                columns[k].later.push_back(j);
                if (parent[k] == n) parent[k] = j;
                k = parent[k];
            }
        }
    }
    for (auto& c : columns) {
        c.outgoing.resize(c.later.size());
        c.incoming.resize(c.later.size());
    }
    return columns;
}

static void eliminate(std::vector<Column>& columns) {
    Real scratch;
    for (size_t k = 0; k + 1 < columns.size(); ++k) {
        auto& c = columns[k];
        for (const auto& value : c.outgoing) c.rate += value;
        if (c.rate <= 0) throw std::logic_error("zero exit rate in closed-class reduction");
        for (auto& value : c.outgoing) value /= c.rate;
        for (size_t p = 0; p + 1 < c.later.size(); ++p) {
            auto& dest = columns[c.later[p]];
            auto pos = std::lower_bound(dest.later.begin(), dest.later.end(), c.later[p+1]);
            for (size_t q = p+1; q < c.later.size(); ++q) {
                while (pos != dest.later.end() && *pos < c.later[q]) ++pos;
                if (pos == dest.later.end() || *pos != c.later[q])
                    throw std::logic_error("missing symbolic fill");
                auto t = pos - dest.later.begin();
                add_product(dest.outgoing[t], c.incoming[p], c.outgoing[q], scratch);
                add_product(dest.incoming[t], c.incoming[q], c.outgoing[p], scratch);
                ++pos;
            }
        }
    }
}

static std::vector<Real> stationary(const std::vector<Column>& cols) {
    std::vector<Real> pi(cols.size());
    pi.back() = 1;
    Real scratch, total = 1;
    for (int k = int(cols.size())-2; k >= 0; --k) {
        const auto& c = cols[k];
        for (size_t j = 0; j < c.later.size(); ++j)
            add_product(pi[k], c.incoming[j], pi[c.later[j]], scratch);
        pi[k] /= c.rate;
        total += pi[k];
    }
    for (auto& v : pi) v /= total;
    return pi;
}

// Solve (I-P)g = reward - centre at every vertex except the final reference
// vertex, with g(reference)=0. Only the subsequent exact residual is used
// to certify the answer, irrespective of the accuracy of this bias solve.
static std::vector<Real> bias(const std::vector<Column>& cols,
                              const std::vector<int>& profile, int mark,
                              const Real& centre) {
    std::vector<Real> g(cols.size());
    Real scratch;
    for (size_t i = 0; i < g.size(); ++i) g[i] = int(profile[i] == mark) - centre;
    for (size_t k = 0; k + 1 < cols.size(); ++k) {
        const auto& c = cols[k];
        g[k] /= c.rate;
        for (size_t j = 0; j < c.later.size(); ++j)
            add_product(g[c.later[j]], c.incoming[j], g[k], scratch);
    }
    g.back() = 0;
    for (int k = int(cols.size())-2; k >= 0; --k) {
        const auto& c = cols[k];
        for (size_t j = 0; j < c.later.size(); ++j)
            add_product(g[k], c.outgoing[j], g[c.later[j]], scratch);
    }
    return g;
}

// Set b_i = trunc(2^bits g_i). With exact transition probabilities w_ij/D,
// min_i and max_i of reward_i + sum P_ij (b_j-b_i)/2^bits bracket pi(reward).
static std::pair<Integer, Integer> residual_bounds(
        const std::vector<Real>& g, const std::vector<int>& profile, int mark,
        const std::vector<std::vector<Edge>>& rows, const std::vector<Integer>& weights,
        const Integer& denominator, unsigned bits) {
    std::vector<Integer> b(g.size());
    Real scale;
    for (size_t i = 0; i < g.size(); ++i) {
        mpf_mul_2exp(scale.get_mpf_t(), g[i].get_mpf_t(), bits);
        mpz_set_f(b[i].get_mpz_t(), scale.get_mpf_t());
    }
    Integer lo, hi, value, diff;
    for (size_t i = 0; i < b.size(); ++i) {
        value = profile[i] == mark ? denominator : Integer(0);
        for (auto [j, weight] : rows[i]) {
            mpz_sub(diff.get_mpz_t(), b[j].get_mpz_t(), b[i].get_mpz_t());
            mpz_addmul(value.get_mpz_t(), diff.get_mpz_t(), weights[weight].get_mpz_t());
        }
        if (!i || value < lo) lo = value;
        if (!i || value > hi) hi = value;
    }
    return {lo, hi};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, nweights, digits, certify;
    Integer base;
    if (!(std::cin >> n >> nweights >> digits >> certify >> base) || n < 1 || base <= 0)
        return 1;
    unsigned bits = static_cast<unsigned>(std::ceil(digits * std::log2(10.0))) + 8;
    mpf_set_default_prec(bits);
    std::vector<Integer> weights(nweights);
    std::vector<Real> values(nweights);
    for (int i = 0; i < nweights; ++i) {
        std::cin >> weights[i];
        values[i] = Real(weights[i]) / Real(base);
    }
    std::vector<int> profile(n);
    std::vector<std::vector<Edge>> rows(n);
    for (int i = 0; i < n; ++i) {
        int degree;
        std::cin >> profile[i] >> degree;
        for (int k = 0; k < degree; ++k) {
            int j, w;
            std::cin >> j >> w;
            rows[i].emplace_back(j, w);
        }
    }
    if (!std::cin) return 2;
    auto cols = symbolic(rows);
    for (int i = 0; i < n; ++i) {
        for (auto [j, w] : rows[i]) {
            auto& c = cols[std::min(i, j)];
            auto ix = std::lower_bound(c.later.begin(), c.later.end(), std::max(i, j))
                      - c.later.begin();
            (i < j ? c.outgoing : c.incoming).at(ix) = values[w];
        }
    }
    eliminate(cols);
    auto pi = stationary(cols);
    std::vector<Real> mass(4);
    for (int i = 0; i < n; ++i) mass[profile[i]] += pi[i];
    Integer denominator = base << bits;
    std::cout << std::scientific << std::setprecision(digits-1);
    for (int mark = 0; mark < 4; ++mark) {
        std::cout << mass[mark];
        if (certify) {
            auto g = bias(cols, profile, mark, mass[mark]);
            auto bounds = residual_bounds(g, profile, mark, rows, weights, denominator, bits);
            std::cout << ' ' << bounds.first << ' ' << bounds.second << ' ' << denominator;
        }
        std::cout << '\n';
    }
}
