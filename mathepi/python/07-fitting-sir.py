"""
MathEpi 07 - Fitting a model to data (least squares)

Generate "observed" data from an SIR epidemic with known parameters, then
recover the transmission rate beta by choosing the value that makes the
model curve closest to the data.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt


def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


N = 1000
gamma = 0.2                     # assume the infectious period is known (5 days)
days = np.arange(0, 61)


def model_I(beta):
    sol = solve_ivp(sir, (0, 60), [N - 1, 1, 0], args=(beta, gamma, N), rtol=1e-8, t_eval=days)
    return sol.y[1]


# Simulate noisy observations (Poisson noise around the true curve)
rng = np.random.default_rng(10)
true_beta = 0.5
observed = rng.poisson(model_I(true_beta))


# Least squares: pick the beta that minimises the sum of squared errors
def sse(beta):
    return np.sum((observed - model_I(beta)) ** 2)


fit = minimize_scalar(sse, bounds=(0.1, 1.0), method="bounded")
beta_hat = fit.x
print(f"estimated beta = {beta_hat:.4f}   (true {true_beta})")
print(f"estimated R0   = {beta_hat / gamma:.3f}   (true 2.5)")

plt.plot(days, observed, "ko", label="Observed")
plt.plot(days, model_I(beta_hat), "r-", label="Fitted SIR")
plt.xlabel("Day")
plt.ylabel("Infectious people")
plt.legend()
plt.show()

# The error curve has a clear minimum near the true beta
beta_grid = np.arange(0.3, 0.701, 0.01)
plt.plot(beta_grid, [sse(b) for b in beta_grid])
plt.axvline(beta_hat, linestyle="--", color="red")
plt.xlabel("beta")
plt.ylabel("Sum of squared errors")
plt.show()
