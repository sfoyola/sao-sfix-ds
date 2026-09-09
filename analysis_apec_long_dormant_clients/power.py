import math
from scipy.optimize import brentq
from statsmodels.stats.proportion import power_proportions_2indep
from itertools import product
from scipy.stats import norm

def n_total_statsmodels(
    baseline_rate,
    mde_relative,
    split_ratio=0.5,
    alpha=0.05,
    power=0.8,
    two_sided=True,
):
    """
    Compute required sample sizes for one or many combinations of
    relative MDEs and treatment split ratios.  p_c = baseline_rate
    Parameters
    ----------
    baseline_rate : float
        Baseline/control conversion rate.
    mde_relative : float or iterable of float
        Relative MDE(s), e.g. 0.05 for a 5% relative lift.
    split_ratio : float or iterable of float
        Treatment allocation share(s), e.g. 0.5 for 50/50 or 0.2 for 20/80.
    alpha : float
        Type I error rate.
    power : float
        Statistical power target.
    two_sided : bool
        Whether to use a two-sided alternative.
    Returns
    -------
    dict
        Dictionary keyed by readable scenario labels. Each value is a flat
        dictionary that can be easily converted to a pandas DataFrame.
    """

    def _as_list(x):
        if isinstance(x, (list, tuple, set)):
            return list(x)
        return [x]

    mde_list = _as_list(mde_relative)
    split_list = _as_list(split_ratio)
    alternative = "two-sided" if two_sided else "larger"

    results = {}

    for mde_rel, split in product(mde_list, split_list):
        p_c = baseline_rate
        p_t = baseline_rate * (1 + mde_rel)
        diff = p_t - p_c

        if not (0 < split < 1):
            raise ValueError(f"split_ratio must be in (0,1). Got {split}.")
        if not (0 < p_c < 1):
            raise ValueError(f"baseline_rate must be in (0,1). Got {p_c}.")
        if not (0 < p_t < 1):
            raise ValueError(
                "baseline_rate * (1 + mde_relative) must be in (0,1). "
                f"Got {p_t} for mde_relative={mde_rel}."
            )

        # statsmodels uses nobs2 = ratio * nobs1
        # let sample 1 = treatment, sample 2 = control
        ratio = (1 - split) / split

        def f(n_treatment):
            pwr = power_proportions_2indep(
                diff=diff,
                prop2=p_c,
                nobs1=n_treatment,
                ratio=ratio,
                alpha=alpha,
                alternative=alternative,
                return_results=False,
            )
            return pwr - power

        n_t = math.ceil(brentq(f, 2, 1e9))
        n_c = math.ceil(ratio * n_t)

        label = f"mde={mde_rel:.3%} | split={split:.0%}/{1 - split:.0%}"
        results[label] = {
            "total_n": n_t + n_c,
            "n_treatment": n_t,
            "n_control": n_c,
            "p_control": p_c,
            "p_treatment": p_t,
            "abs_mde": diff,
            "mde_relative": mde_rel,
            "split_ratio": split,
            "alpha": alpha,
            "power": power,
            "two_sided": two_sided,
        }

    return results

def n_total_continuous(
    baseline_mean,
    std_dev,
    mde_absolute,
    split_ratio=0.5,
    alpha=0.05,
    power=0.8,
    two_sided=True,
):
    """
    Compute required sample sizes for one or many combinations of
    absolute MDEs and treatment split ratios for a continuous metric.

    Parameters
    ----------
    baseline_mean : float
        Baseline/control mean of the metric.
    std_dev : float
        Standard deviation of the metric at the unit of analysis.
    mde_absolute : float or iterable of float
        Absolute MDE(s), e.g. 5 means detecting a lift from 120 to 125.
    split_ratio : float or iterable of float
        Treatment allocation share(s), e.g. 0.5 for 50/50 or 0.2 for 20/80.
    alpha : float
        Type I error rate.
    power : float
        Statistical power target.
    two_sided : bool
        Whether to use a two-sided test.

    Returns
    -------
    dict
        Dictionary keyed by readable scenario labels. Each value is a flat
        dictionary that can be easily converted to a pandas DataFrame.
    """

    def _as_list(x):
        if isinstance(x, (list, tuple, set)):
            return list(x)
        return [x]

    if std_dev <= 0:
        raise ValueError(f"std_dev must be > 0. Got {std_dev}.")

    mde_list = _as_list(mde_absolute)
    split_list = _as_list(split_ratio)

    z_alpha = norm.ppf(1 - alpha / 2) if two_sided else norm.ppf(1 - alpha)
    z_beta = norm.ppf(power)

    results = {}

    for mde_abs, split in product(mde_list, split_list):
        if not (0 < split < 1):
            raise ValueError(f"split_ratio must be in (0,1). Got {split}.")
        if mde_abs <= 0:
            raise ValueError(f"mde_absolute must be > 0. Got {mde_abs}.")

        mu_c = baseline_mean
        mu_t = baseline_mean + mde_abs

        # If treatment share is split, then:
        # n_t = split * N
        # n_c = (1 - split) * N
        #
        # For equal variances:
        # SE(diff) = std_dev * sqrt(1/n_t + 1/n_c)
        #
        # Solve:
        # mde_abs = (z_alpha + z_beta) * std_dev * sqrt(1/n_t + 1/n_c)

        total_n = (
            ((z_alpha + z_beta) ** 2)
            * (std_dev ** 2)
            * (1 / split + 1 / (1 - split))
            / (mde_abs ** 2)
        )

        n_t = math.ceil(total_n * split)
        n_c = math.ceil(total_n * (1 - split))

        label = f"mde={mde_abs:.3f} | split={split:.0%}/{1 - split:.0%}"
        results[label] = {
            "total_n": n_t + n_c,
            "n_treatment": n_t,
            "n_control": n_c,
            "baseline_mean": mu_c,
            "treatment_mean": mu_t,
            "mde_absolute": mde_abs,
            "std_dev": std_dev,
            "alpha": alpha,
            "power": power,
            "two_sided": two_sided,
            "split_ratio": split,
        }

    return results