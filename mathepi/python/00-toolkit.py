"""
MathEpi 00 - Toolkit: R and Python side by side

Run with:  python 00-toolkit.py
Needs:     numpy, matplotlib   (pip install numpy matplotlib)

The basic reproduction number R0 is the average number of people one
infectious person infects in a fully susceptible population.
In the simplest model:  R0 = beta / gamma
  beta  = transmission rate (per day)
  gamma = recovery rate (per day), so 1/gamma is the infectious period
"""
import numpy as np
import matplotlib.pyplot as plt


# A function (R: r0 <- function(beta, gamma) beta / gamma)
def r0(beta, gamma):
    return beta / gamma


print("R0 =", r0(beta=0.5, gamma=0.2))   # 2.5

# Arrays and loops (R: betas <- c(0.2, 0.4, 0.6, 0.8))
betas = np.array([0.2, 0.4, 0.6, 0.8])
gamma = 0.25

for b in betas:
    print(f"beta = {b} -> R0 = {r0(b, gamma):.1f}")

print(r0(betas, gamma))   # numpy functions work on whole arrays at once

# A small table of scenarios (R: a data frame)
print("\n beta   gamma   R0    can_spread")
for b in betas:
    R0 = r0(b, gamma)
    print(f" {b:.1f}    {gamma:.2f}   {R0:.1f}   {R0 > 1}")   # an outbreak needs R0 > 1

# A first plot
plt.plot(betas, r0(betas, gamma), "o-")
plt.axhline(1, linestyle="--", color="grey")    # the threshold R0 = 1
plt.xlabel("Transmission rate (beta)")
plt.ylabel("R0")
plt.title("R0 grows with the transmission rate")
plt.show()

# ---------------------------------------------------------------
# R vs Python cheat sheet
#   Task            R                          Python (numpy)
#   array           c(1, 2, 3)                 np.array([1, 2, 3])
#   sequence        seq(0, 1, by = 0.1)        np.linspace(0, 1, 11)
#   length          length(x)                  len(x)
#   first element   x[1]                       x[0]   <- Python counts from 0!
#   loop            for (i in 1:3) { ... }     for i in range(3): ...
#   function        f <- function(x) x^2       def f(x): return x**2
#   power           x^2                        x**2
#   plot            plot(x, y)                 plt.plot(x, y)
# ---------------------------------------------------------------
