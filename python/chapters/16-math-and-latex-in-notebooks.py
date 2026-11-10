# %% [markdown]
# # 16 - Math and LaTeX in Python Notebooks
# Jupyter notebooks (and the `# %% [markdown]` cells of these files) render
# LaTeX mathematics, so you can write the equations behind a model next to the
# code that fits it.
#
# ## Inline and display math
# Single dollar signs keep a formula inside the sentence: the variance of
# $X=(X_1,\ldots,X_n)$ is written right in the text.
#
# Double dollar signs put the equation on its own line:
#
# $$
# \operatorname{Var}(X)=\frac{1}{n}\sum_{i=1}^{n}\left(X_i-\bar X\right)^2,
# \qquad \bar X=\frac{1}{n}\sum_{i=1}^{n}X_i
# $$
#
# ## Equations in code output
# `IPython.display.Math` renders a LaTeX string in a notebook cell. (Run as a
# plain script it only prints an object; in a notebook it shows the formula.)

# %%
try:
    from IPython.display import Math, display

    display(Math(r"f(x) = x^3"))
except ImportError:                      # IPython is installed with Jupyter
    print(r"f(x) = x^3")

# %% [markdown]
# ## Mathematics inside plots
# matplotlib understands a subset of LaTeX ("mathtext") in any text, as long as
# the formula is between dollar signs and the string is a raw string `r"..."`.

# %%
import matplotlib.pyplot as plt
import numpy as np


def cube(x):
    return x ** 3


x = np.linspace(-2, 2, 100)
plt.plot(x, cube(x), label=r"$f(x)=x^3$")
plt.plot(x, np.sin(x), "--", label=r"$g(x)=\sin(x)$")
plt.title(r"Two functions: $f(x)=x^3$ and $g(x)=\sin x$")
plt.xlabel(r"$x$")
plt.ylabel(r"$y=f(x)$")
plt.legend()
plt.show()

print(cube(3))

# %% [markdown]
# ## A fitted model written as an equation
# Use the numbers from a fitted model to build the LaTeX text automatically:

# %%
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

iris = load_iris()
fit = LinearRegression().fit(iris.data[:, [3]], iris.data[:, 2])

equation = rf"$\widehat{{\mathrm{{length}}}} = {fit.intercept_:.2f} + {fit.coef_[0]:.2f}\,\mathrm{{width}}$"
print(equation)

plt.figure(figsize=(6, 2))
plt.axis("off")
plt.text(0.5, 0.5, equation, ha="center", va="center", fontsize=18)
plt.show()

# %% [markdown]
# ## From notebook to PDF
# `jupyter nbconvert --to pdf notebook.ipynb` produces a PDF; it needs a LaTeX
# distribution such as TeX Live or MiKTeX (see Part 3 of the course). To use
# full LaTeX for the text inside matplotlib figures, set
# `plt.rcParams["text.usetex"] = True` (also requires LaTeX).
