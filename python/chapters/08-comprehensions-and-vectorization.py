# %% [markdown]
# # 08 - Comprehensions and Vectorisation
# R has the *apply family* to avoid explicit loops. In Python the same job is
# done by **comprehensions**, `map`/`filter`, NumPy's `axis=` argument and
# pandas' `apply`, `agg` and `groupby`.

# %%
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns=lambda c: c.replace(" (cm)", "").replace(" ", "_"))
df["species"] = df.pop("target").map(dict(enumerate(iris.target_names)))
print(df.head(3))

# %% [markdown]
# ## Comprehensions (R: sapply / lapply)

# %%
squares = [n ** 2 for n in range(1, 11)]
print(squares)

even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]    # with a condition
print(even_squares)

lengths = {name: len(name) for name in ["Ada", "Bob", "Chloe"]}   # dict comprehension
print(lengths)

print(list(map(lambda v: v + 1, [1, 2, 3])))
print(list(filter(lambda v: v > 1, [1, 2, 3])))

# %% [markdown]
# ## Along the axes of an array (R: apply on a matrix)
# `axis=0` works down the columns, `axis=1` across the rows.

# %%
A = np.array([[1, 2],
              [3, 4]])
print(A.sum(axis=0), A.sum(axis=1))
print(np.apply_along_axis(lambda row: row.max() - row.min(), 1, A))

# %% [markdown]
# ## DataFrame columns (R: apply / sapply)

# %%
numeric = df.select_dtypes("number")
print(numeric.apply(np.mean))
print(numeric.agg(["min", "max", "std"]).round(2))
print(numeric.apply(lambda col: col.max() - col.min()))      # the range of every column

# %%
def coef_dispersion(s):
    return s.std() / s.mean()

summary = numeric.apply(lambda s: pd.Series({
    "min": s.min(), "max": s.max(), "std": s.std(),
    "Q1": s.quantile(0.25), "median": s.median(), "Q3": s.quantile(0.75),
    "dispersion": coef_dispersion(s)}))
print(summary.round(3))

# %% [markdown]
# ## Statistics by group (R: tapply)

# %%
print(df.groupby("species")["sepal_length"].mean())
print(df.groupby("species")[["sepal_length", "petal_length"]].agg(["mean", "std"]).round(2))

# %% [markdown]
# ## Quantiles of every column (R: vapply)

# %%
print(numeric.quantile([0, 0.25, 0.5, 0.75, 1]))
