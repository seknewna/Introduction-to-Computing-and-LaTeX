"""
MathEpi 04 - Vaccination and interventions

Idealised vaccination: a fraction `vacc` of the population starts fully
immune (in R). Distancing: reduce beta.
With R0 = 2.5 the herd immunity threshold is 1 - 1/2.5 = 0.6.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


def run_sir(beta=0.5, gamma=0.2, N=1000, vacc=0.0, days=200):
    y0 = [N - vacc * N - 1, 1, vacc * N]
    return solve_ivp(sir, (0, days), y0, args=(beta, gamma, N),
                     rtol=1e-8, t_eval=np.arange(0, days + 1))


# Compare vaccination coverage
for p, colour in zip([0, 0.3, 0.5, 0.7], ["black", "blue", "green", "red"]):
    sol = run_sir(vacc=p)
    plt.plot(sol.t, sol.y[1], color=colour, label=f"{int(p * 100)}% vaccinated")
plt.xlabel("Day")
plt.ylabel("Infectious people")
plt.legend()
plt.show()


# How many people are infected at each coverage level?
def infected_by_coverage(p, N=1000):
    sol = run_sir(vacc=p, N=N)
    return sol.y[2, -1] - p * N          # recovered minus those vaccinated


p_grid = np.arange(0, 0.95, 0.05)
total_infected = [infected_by_coverage(p) for p in p_grid]

plt.plot(p_grid, total_infected, "o-")
plt.axvline(0.6, linestyle="--", color="grey")
plt.xlabel("Vaccination coverage")
plt.ylabel("People infected (of 1000)")
plt.show()

# Reducing transmission instead: a 40% cut in contacts (beta 0.5 -> 0.3)
base = run_sir(beta=0.5)
cut40 = run_sir(beta=0.3)
print(f"peak, baseline       = {base.y[1].max():.0f}")
print(f"peak, with distancing = {cut40.y[1].max():.0f}")
