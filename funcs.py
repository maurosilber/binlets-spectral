from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray
from scipy.stats import rv_continuous


@dataclass
class BinnedRV:
    """Compute the probabilities over bins for a random variable.

    To broadcast over rv.args, append a new dimension:
    - `args[..., np.newaxis]`, or
    - `np.expand_dims(args, axis=-1)`
    """

    rv: rv_continuous
    bin_edges: NDArray
    probability: NDArray = field(init=False)

    def __post_init__(self):
        prob = np.diff(self.rv.cdf(self.bin_edges))
        self.probability = prob / prob.sum(axis=-1, keepdims=True)

    @property
    def bin_center(self):
        bin_width = np.diff(self.bin_edges)
        return self.bin_edges[:-1] + bin_width / 2


def binned_fourier(y, /, *, n: int):
    t = np.linspace(0, 2 * np.pi, y.shape[-1], endpoint=False)
    return (y * np.exp(1j * n * t)).sum(axis=-1)


def binned_variance(mean, a0, a1):
    return a0 + a1 * mean


def phasor_covariance(N_bins, R0, R1, R2, a0, a1):
    r"""Covariance matrix for phasor r = R1/R0

    where
    - R_n = \sum^{N_bins} X_j e^{inwt_j}
    - E[X_j] = \mu_j
    - Var[X_j] = a_0 + a_1 \mu_j
    - Cov[X_i, X_j] = 0 if i ≠ j
    """

    R0 = R0.real
    r1 = R1 / R0
    r2 = R2 / R0

    shape = np.broadcast(N_bins, R0, R1, R2, a0, a1).shape
    cov = np.empty((2, 2) + shape, dtype=float)
    cov[0, 0] = a1 * R0 * (1 + r2.real - 2 * r1.real**2) + a0 * N_bins * (
        1 - 2 * r1.real**2
    )
    cov[1, 1] = a1 * R0 * (1 - r2.real - 2 * r1.imag**2) + a0 * N_bins * (
        1 - 2 * r1.imag**2
    )
    cov[0, 1] = cov[1, 0] = (
        a1 * R0 * r2.imag + 2 * (a0 * N_bins - a1 * R0) * r1.real * r1.imag
    )
    cov /= 2 * R0**2
    return cov


if __name__ == "__main__":
    import numpy as np
    import scipy.stats
    import funcs

    X = funcs.BinnedRV(
        rv=scipy.stats.expon(scale=1),
        bin_edges=np.linspace(0, 10, 32),
    )
    N_photons = 1_000
    a = [0, 1]  # variance = a[0] + a[1] * mean
    mean = N_photons * X.probability
    variance = funcs.binned_variance(mean, *a)

    rng = np.random.default_rng(0)
    hist = rng.normal(
        mean,
        variance**0.5,
        size=[10_000, mean.size],
    )

    R = funcs.binned_fourier(hist, n=np.arange(3)[:, None, None])

    r = R[1] / R[0]
    r_ecov = np.cov(r.real, r.imag)
    r_cov = funcs.phasor_covariance(mean.size, *R.mean(axis=-1), *a)

    print(r_ecov / r_cov)
