"""
MathEpi 05 - The SEIR model

Adds an Exposed compartment (infected but not yet infectious):

    dS/dt = -beta * S * I / N
    dE/dt =  beta * S * I / N - sigma * E
    dI/dt =  sigma * E - gamma * I
    dR/dt =  gamma * I

sigma = 1 / (latent period).  Here: 5-day latent period, sigma = 0.2.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def seir(t, y, beta, sigma, gamma, N):
    S, E, I, R = y
    dS = -beta * S * I / N
    dE = beta * S * I / N - sigma * E
    dI = sigma * E - gamma * I
    dR = gamma * I
    return [dS, dE, dI, dR]


def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]


N = 1000
days = np.arange(0, 201)

seir_sol = solve_ivp(seir, (0, 200), [N - 1, 0, 1, 0],
                     args=(0.5, 0.2, 0.2, N), rtol=1e-8, t_eval=days)
sir_sol = solve_ivp(sir, (0, 200), [N - 1, 1, 0],
                    args=(0.5, 0.2, N), rtol=1e-8, t_eval=days)

plt.plot(days, sir_sol.y[1], "r", label="SIR")
plt.plot(days, seir_sol.y[2], "b", label="SEIR")
plt.xlabel("Day")
plt.ylabel("Infectious people")
plt.legend()
plt.show()

print("model   peak_day  peak_infectious")
print(f"SIR     {days[sir_sol.y[1].argmax()]:>8}  {sir_sol.y[1].max():>10.0f}")
print(f"SEIR    {days[seir_sol.y[2].argmax()]:>8}  {seir_sol.y[2].max():>10.0f}")
# Same R0 = beta / gamma = 2.5, so the same final size,
# but the latent period delays the epidemic and lowers the infectious peak.
