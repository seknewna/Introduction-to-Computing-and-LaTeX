# %% [markdown]
# # 04 - Lists, Dictionaries and DataFrames

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)

# %% [markdown]
# ## Multi-dimensional arrays
# NumPy arrays can have any number of dimensions. A classic use is gridded data
# such as maps over time: `array[time, latitude, longitude]`.

# %%
arr = np.arange(1, 25).reshape(2, 3, 4)      # 2 time steps, each a 3 x 4 grid
print(arr.shape)
print(arr[1, 0, 0])      # first row, first column of the 2nd grid
print(arr[0])            # the whole first grid
print(arr.mean(axis=0))  # average over the first dimension

# %% [markdown]
# ## Lists, tuples, dictionaries and sets
# * **list** — ordered and changeable: `[1, 2, 3]`
# * **tuple** — ordered, fixed: `(1, 2)`
# * **dict** — key -> value pairs (like an R named list)
# * **set** — unique values

# %%
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits, fruits[0], fruits[-1], fruits[1:3], len(fruits))

point = (3, 4)
x, y = point                      # unpacking
print(x, y)

record = {"matrix": np.zeros((2, 2)), "sequence": list(range(1, 6)), "flag": True}
print(record["sequence"], list(record.keys()))
record["text"] = "I am learning Python"      # add a new entry
print(len(record))

print(set([1, 2, 2, 3, 3, 3]))               # {1, 2, 3}

# %% [markdown]
# ## DataFrames
# A pandas `DataFrame` is a table: rows are observations, columns are variables
# and each column can have a different type (R: `data.frame`).

# %% [markdown]
# ### Turning a continuous variable into categories

# %%
n = 120
df = pd.DataFrame({
    "ID": [f"Particip_{i}" for i in range(1, n + 1)],
    "age": rng.choice(np.arange(0, 121), size=n, replace=False),
})
print(df.head())

bins = np.arange(0, 121, 10)
df["age_group"] = pd.cut(df["age"], bins=bins, include_lowest=True)
print(df.head())

# %% [markdown]
# ### Exercise: summarise the age groups
# 1. Counts per age group

# %%
counts = df["age_group"].value_counts().sort_index()
print(counts)

# %% [markdown]
# 2. A bar chart of the groups

# %%
fig, ax = plt.subplots(figsize=(8, 4))
counts.plot.bar(ax=ax, color="purple")
ax.set_title("Distribution of ages")
ax.set_ylabel("participants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% [markdown]
# 3. A histogram of the raw ages

# %%
plt.figure(figsize=(7, 4))
plt.hist(df["age"], bins=12, color="pink", edgecolor="white")
plt.title("Histogram of ages")
plt.xlabel("age")
plt.show()

# %% [markdown]
# 4. IDs of the participants aged more than 70 up to 80

# %%
ids = df.loc[(df["age"] > 70) & (df["age"] <= 80), "ID"]
print(ids.tolist())

# %% [markdown]
# `groupby` splits the table into one piece per group (R: `split`):

# %%
groups = {key: part for key, part in df.groupby("age_group", observed=True)}
print(list(groups)[:3])
print(groups[pd.Interval(70, 80)]["ID"].tolist())

# %% [markdown]
# ### Creating a DataFrame directly

# %%
df2 = pd.DataFrame({"x": rng.normal(size=10), "y": rng.poisson(2, size=10)})
print(df2.head(3))
print(df2.dtypes)
print(df2.describe().round(2))
