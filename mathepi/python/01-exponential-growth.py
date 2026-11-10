"""
MathEpi 01 - Exponential growth and doubling time

At the start of an outbreak almost everyone is susceptible, so cases grow
roughly exponentially:   I(t) ~ I0 * exp(r * t)
The growth rate r can be estimated from data, and the doubling time is
    T_d = ln(2) / r
"""
import numpy as np
import matplotlib.pyplot as plt

# Simulate daily case counts: true r = 0.15 per day, 5 cases on day 0,
# plus Poisson noise (real counts are never perfectly smooth).
rng = np.random.default_rng(1)          # (R: set.seed(1))
r_true = 0.15
day = np.arange(30)                      # days 0..29
cases = rng.poisson(5 * np.exp(r_true * day))
print("first days:", cases[:6])

# Taking logs turns the exponential into a straight line:
#     log I(t) = log I0 + r * t
# so a straight-line fit of log(cases) against day gives r as the slope.
slope, intercept = np.polyfit(day, np.log(cases), 1)
r_hat = slope
print(f"estimated r      = {r_hat:.3f}   (true {r_true})")
print(f"doubling time    = {np.log(2) / r_hat:.2f} days")
print(f"true doubling    = {np.log(2) / r_true:.2f} days")

# Plot data and fit on a log scale (a straight line = exponential growth)
plt.semilogy(day, cases, "o", label="Observed")
plt.semilogy(day, np.exp(intercept + slope * day), "r-", label="Fitted")
plt.xlabel("Day")
plt.ylabel("Daily cases (log scale)")
plt.legend()
plt.show()
