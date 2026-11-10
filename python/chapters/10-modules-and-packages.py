# %% [markdown]
# # 10 - Modules and Packages
# A **module** is a file of Python code; a **package** is a collection of
# modules. Python ships with a large *standard library*, and the community
# provides hundreds of thousands more packages on PyPI.

# %% [markdown]
# ## Importing

# %%
import math                       # the whole module
from math import sqrt, pi         # only some names
import numpy as np                # with a short alias (a universal convention)

print(math.sqrt(16), sqrt(25), round(pi, 4), np.sqrt(36))

# %% [markdown]
# ## A tour of the standard library

# %%
import random
import statistics
from datetime import date
from pathlib import Path

random.seed(1)
print(random.sample(range(1, 50), 6))                 # six lottery numbers
print(statistics.mean([2, 4, 4, 4, 5, 5, 7, 9]), statistics.stdev([2, 4, 4, 4, 5, 5, 7, 9]))
print(date(2026, 11, 10).strftime("%A %d %B %Y"))
print(Path.cwd().name)

# %% [markdown]
# ## Finding out what a module offers

# %%
print([name for name in dir(math) if not name.startswith("_")][:8], "...")
print(math.sqrt.__doc__)          # or: help(math.sqrt)

# %% [markdown]
# ## Installing packages
# Packages are installed with **pip**, in a terminal (not in Python code):
# ```bash
# pip install pandas matplotlib scikit-learn
# pip list                      # what is installed
# pip install --upgrade pandas
# ```
# From a notebook cell you can use `%pip install pandas`.
#
# Check from Python whether a package is available, and which version:

# %%
import importlib.metadata as metadata
import importlib.util

for package in ["numpy", "pandas", "not_a_real_package"]:
    if importlib.util.find_spec(package):
        print(f"{package:20s} installed, version {metadata.version(package)}")
    else:
        print(f"{package:20s} NOT installed -> pip install {package}")

# %% [markdown]
# ## pandas verbs (R: the dplyr verbs)
# The data-manipulation vocabulary of R's `dplyr` has a direct counterpart in
# pandas:
#
# | dplyr | pandas |
# |---|---|
# | `select()` | `df[["a", "b"]]`, `df.drop(columns=...)` |
# | `filter()` | `df[condition]`, `df.query("...")` |
# | `arrange()` | `df.sort_values(...)` |
# | `rename()` | `df.rename(columns=...)` |
# | `mutate()` | `df.assign(new=...)` |
# | `group_by() + summarise()` | `df.groupby(...).agg(...)` |

# %%
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns=lambda c: c.replace(" (cm)", "").replace(" ", "_"))
df["species"] = df.pop("target").map(dict(enumerate(iris.target_names)))

print(df[["sepal_length", "petal_length"]].head(3))                    # select
print(df.drop(columns="species").columns.tolist())

# %%
print(df[(df["species"] == "setosa") & (df["petal_length"] > 1.4)].head(3))   # filter
print(df.query("species == 'setosa' and petal_length > 1.4").shape)

print(df.sort_values("sepal_length", ascending=False).head(3))                 # arrange
print(df.rename(columns={"petal_length": "PetalLength"}).columns.tolist())     # rename

print(df.assign(ratio=df["petal_length"] / df["petal_width"]).head(3))         # mutate
print(df.groupby("species")["petal_width"].mean().round(3))                    # summarise
