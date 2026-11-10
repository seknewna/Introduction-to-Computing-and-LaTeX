"""
MathEpi 03 - R0, herd immunity and final size

  R0                = beta / gamma         (an outbreak needs R0 > 1)
  herd immunity     = 1 - 1 / R0
  final size z      solves   z = 1 - exp(-R0 * z)
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib.pyplot as plt

beta, gamma = 0.5, 0.2
R0 = beta / gamma
print(f"R0 = {R0},  herd immunity threshold = {1 - 1 / R0:.2f}")


# The final-size equation has no closed form, so find its root numerically
# (R: uniroot).
def final_size(R0):
    if R0 <= 1:
        return 0.0
    return brentq(lambda z: z - (1 - np.exp(-R0 * z)), 1e-6, 1)


print(f"final size from the equation = {final_size(R0):.4f}")


# Check against a simulated epidemic
def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


N = 1000
sol = solve_ivp(sir, (0, 300), [N - 1, 1, 0], args=(beta, gamma, N),
                rtol=1e-8, t_eval=np.arange(0, 301))
print(f"final size from the simulation = {sol.y[2, -1] / N:.4f}")

# How the final size depends on R0
print("\n  R0   herd immunity   final size")
for R in [1.2, 1.5, 2, 2.5, 3, 4]:
    print(f"  {R:<4} {1 - 1 / R:>10.3f} {final_size(R):>12.3f}")

R0_grid = np.arange(1.05, 5.01, 0.05)
plt.plot(R0_grid, [final_size(R) for R in R0_grid], label="Final size")
plt.plot(R0_grid, 1 - 1 / R0_grid, "--", label="Herd immunity threshold")
plt.xlabel("R0")
plt.ylabel("Fraction of population")
plt.legend()
plt.show()
# The final size is always larger than the herd immunity threshold:
# the epidemic overshoots because infections continue while I is still large.
