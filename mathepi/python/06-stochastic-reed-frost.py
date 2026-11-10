"""
MathEpi 06 - Stochastic epidemics (Reed-Frost chain binomial)

With few infected people, chance matters. In discrete generations, if I_t
people are infectious and each pair has probability p of a transmitting
contact, a susceptible escapes with probability (1 - p)**I_t, so

    I_{t+1} ~ Binomial(S_t, 1 - (1 - p)**I_t)
"""
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)


def reed_frost(N=200, I0=1, p=0.01):
    S, I, total = N - I0, I0, I0
    while I > 0:
        new_I = rng.binomial(S, 1 - (1 - p) ** I)
        S -= new_I
        total += new_I
        I = new_I
    return total                      # total number ever infected


N, p = 200, 0.01
R0 = (N - 1) * p                      # about 2
print("R0 =", R0)

# Run many outbreaks
sizes = np.array([reed_frost(N=N, p=p) for _ in range(500)])

plt.hist(sizes, bins=30, color="lightgrey", edgecolor="grey")
plt.xlabel("Total infected (out of 200)")
plt.title("500 simulated outbreaks")
plt.show()
# The histogram is bimodal: minor outbreaks fizzle out, major ones take off.

# Probability of a minor outbreak
print("fraction that fizzled (<20 infected):", np.mean(sizes < 20))

# Early on the epidemic behaves like a branching process; the probability q
# that it dies out solves   q = exp(R0 * (q - 1)).
q = brentq(lambda q: q - np.exp(R0 * (q - 1)), 0, 0.999)
print("theory:", round(q, 3))
# Even with R0 ~ 2, roughly one introduction in five goes nowhere.
