# %% [markdown]
# # 06 - Charts and Distribution Simulations
# We use **matplotlib** for plots and NumPy's random generator for simulation.

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.datasets import load_iris

rng = np.random.default_rng(12092024)

# %% [markdown]
# ## Basic charts
# ### Bar chart and pie chart

# %%
frequencies = {"Female": 35, "Children": 25, "Male": 40}
colours = ["purple", "salmon", "pink"]

fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].bar(frequencies.keys(), frequencies.values(), color=colours)
axes[0].set_title("Bar chart")
axes[1].pie(frequencies.values(),
            labels=[f"{k} ({v})" for k, v in frequencies.items()], colors=colours)
axes[1].set_title("Pie chart")
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Histogram and density

# %%
x = rng.integers(1, 121, size=1000)

fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].hist(x, density=True, color="lightgrey", edgecolor="white")
axes[0].set_title("Histogram (densities)")
grid = np.linspace(x.min(), x.max(), 200)
axes[1].plot(grid, stats.gaussian_kde(x)(grid), color="salmon")
axes[1].set_title("Density of x")
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Scatter plot

# %%
t = np.linspace(0, 2 * np.pi, 50)
plt.scatter(t, np.sin(t), color="blue")
plt.title("sin(x)")
plt.show()

# %% [markdown]
# **Exercise:** `petal length` against `petal width`, coloured by species, with a
# fitted regression line.

# %%
iris = load_iris()
width, length = iris.data[:, 3], iris.data[:, 2]
slope, intercept = np.polyfit(width, length, 1)

for k, name in enumerate(iris.target_names):
    mask = iris.target == k
    plt.scatter(width[mask], length[mask], label=name, s=18)
xs = np.array([width.min(), width.max()])
plt.plot(xs, intercept + slope * xs, "b--", linewidth=2)
plt.xlabel("Petal width")
plt.ylabel("Petal length")
plt.legend()
plt.show()

# %% [markdown]
# ## Simulating distributions
# ### Uniform distribution
# $$f_X(x)=\begin{cases}\frac{1}{b-a} & x\in[a,b]\\ 0 & \text{otherwise}\end{cases}$$

# %%
u = rng.uniform(size=1000)
plt.hist(u, bins=20, density=True, color="turquoise", edgecolor="white")
plt.axvline(u.mean(), color="blue", linestyle="--", label="Average")
plt.title("Histogram of a uniform distribution")
plt.legend()
plt.show()

# %% [markdown]
# A Kolmogorov-Smirnov test: a large p-value is consistent with "looks uniform";
# a Q-Q plot compares the sample with a normal distribution.

# %%
ks = stats.kstest(u, "uniform")
print(f"KS statistic = {ks.statistic:.3f}, p-value = {ks.pvalue:.3f}")

fig, ax = plt.subplots(figsize=(4.5, 4))
stats.probplot(u, dist="norm", plot=ax)
plt.show()

# %% [markdown]
# ### Binomial distribution
# $$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$$

# %%
b = rng.binomial(n=1, p=0.3, size=10000)
values, counts = np.unique(b, return_counts=True)

fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))
axes[0].pie(counts, labels=values)
axes[1].bar(values.astype(str), counts)
plt.tight_layout()
plt.show()

# %% [markdown]
# ### Gaussian (normal) distribution
# $$f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\}$$

# %%
g = rng.normal(0, 1, size=1000)
plt.hist(g, bins=30, density=True, color="turquoise", edgecolor="white")
grid = np.linspace(-4, 4, 200)
plt.plot(grid, stats.norm.pdf(grid), "r--")
plt.title("Standard normal distribution")
plt.show()
print(round(g.mean(), 3), round(g.std(ddof=1), 3))

# %% [markdown]
# ### A simulated linear relationship
# $$y_i=\alpha+\beta x_i+\varepsilon_i,\qquad \varepsilon_i\sim\mathcal N(0,1)$$

# %%
x = rng.normal(5, 1.5, size=1000)
z = 4 + 8 * x + rng.normal(size=1000)       # the true relationship is known

fit = stats.linregress(x, z)
print(f"intercept = {fit.intercept:.2f}, slope = {fit.slope:.2f}, R^2 = {fit.rvalue**2:.3f}")

# prediction for a new value x = 15
print("prediction at x = 15:", round(fit.intercept + fit.slope * 15, 2))

plt.scatter(x, z, s=6, color="darkorange", label="Actual")
xs = np.array([x.min(), 15])
plt.plot(xs, fit.intercept + fit.slope * xs, "b-", label="Fitted line")
plt.scatter([15], [fit.intercept + fit.slope * 15], color="darkgreen", label="Predicted")
plt.legend()
plt.show()

# %% [markdown]
# ### Exponential and Poisson distributions

# %%
e = rng.exponential(scale=1.0, size=1000)
p = rng.poisson(lam=2.5, size=1000)

fig, axes = plt.subplots(1, 2, figsize=(9, 3.8))
axes[0].hist(e, bins=30, density=True, color="turquoise", edgecolor="white")
axes[0].set_title("Exponential")
vals, cnt = np.unique(p, return_counts=True)
axes[1].bar(vals, cnt / cnt.sum(), color="turquoise")
axes[1].set_title("Poisson")
plt.tight_layout()
plt.show()
