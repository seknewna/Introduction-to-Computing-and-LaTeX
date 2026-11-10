"""
MathEpi 02 - The SIR model

Susceptible -> Infectious -> Recovered, in a population of size N:

    dS/dt = -beta * S * I / N
    dI/dt =  beta * S * I / N - gamma * I
    dR/dt =  gamma * I

Needs: numpy, scipy, matplotlib
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def sir(t, y, beta, gamma, N):
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dR]


N = 1000
beta, gamma = 0.5, 0.2
y0 = [N - 1, 1, 0]                       # S, I, R at time 0
days = np.arange(0, 121)                 # 0, 1, ..., 120

# rtol sets how accurately the solver works; a tight value gives the same
# numbers as R's deSolve
sol = solve_ivp(sir, (0, 120), y0, args=(beta, gamma, N), rtol=1e-8, t_eval=days)
S, I, R = sol.y

plt.plot(sol.t, S, "b", label="S")
plt.plot(sol.t, I, "r", label="I")
plt.plot(sol.t, R, "g", label="R")
plt.xlabel("Day")
plt.ylabel("People")
plt.title("SIR epidemic")
plt.legend()
plt.show()

print(f"peak infectious     = {I.max():.0f}")
print(f"peak day            = {sol.t[I.argmax()]:.0f}")
print(f"total ever infected = {R[-1]:.0f}")
