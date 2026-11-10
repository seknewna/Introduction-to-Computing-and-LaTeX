# %% [markdown]
# # 12 - Method Chaining and Data Manipulation
# R's pipe (`%>%` or `|>`) lets you read a sequence of steps from left to right.
# pandas does the same with **method chaining**: every method returns a new
# DataFrame, so you can add `.` after the previous step. Wrapping the chain in
# parentheses lets you put each step on its own line.

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns=lambda c: c.replace(" (cm)", "").replace(" ", "_"))
df["species"] = df.pop("target").map(dict(enumerate(iris.target_names)))

# %% [markdown]
# ## A first chain

# %%
result = (
    df.groupby("species")["petal_width"]
      .mean()
      .round(3)
      .rename("mean_petal_width")
      .reset_index()
)
print(result)

# %% [markdown]
# Without chaining, the same work needs temporary names (or nested calls that
# read inside-out):

# %%
step1 = df.groupby("species")["petal_width"]
step2 = step1.mean()
print(step2.round(3))

# %% [markdown]
# ## Frequency table of a categorical variable
# `.pipe()` lets you put your own function inside a chain.

# %%
gender = pd.Series(["Female", "Male", "Male", "Female", "Female", "Male"])

table = (
    gender.value_counts()
          .rename_axis("Gender")
          .reset_index(name="Count")
          .assign(Rel_freq=lambda t: (t["Count"] / t["Count"].sum()).round(2))
)
print(table)

def percent(frame, column):
    return frame.assign(**{column + "_pct": (frame[column] * 100).round(0)})

print(table.pipe(percent, "Rel_freq"))

table.plot.bar(x="Gender", y="Rel_freq", legend=False)
plt.ylabel("Relative frequency")
plt.show()

# %% [markdown]
# ## Reshaping: wide to long and back (R: reshape2 / tidyr)

# %%
stats = df.groupby("species").agg(["mean", "std"])      # columns are (variable, statistic)
print(stats.round(2))

# wide -> long: one row per species / variable / statistic
flat = stats.copy()
flat.columns = [f"{var}|{stat}" for var, stat in flat.columns]       # e.g. "petal_length|mean"
long = flat.reset_index().melt(id_vars="species", value_name="value")
long[["variable", "metric"]] = long["variable"].str.split("|", expand=True)
long = long[["species", "variable", "metric", "value"]]
print(long.head(6).round(2))

# long -> wide again
wide = long.pivot(index=["species", "variable"], columns="metric", values="value").reset_index()
wide["std_error"] = wide["std"] / np.sqrt(len(df))      # standard error of the mean
print(wide.round(3).head(4))

# %%
fig, axes = plt.subplots(1, 4, figsize=(12, 3.2), sharey=False)
for ax, (variable, part) in zip(axes, wide.groupby("variable")):
    ax.bar(part["species"], part["mean"], yerr=part["std_error"], color="forestgreen", alpha=0.6,
           ecolor="orange", capsize=4)
    ax.set_title(variable)
    ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.show()

# %% [markdown]
# ## Combining tables: merge (R: left_join)

# %%
info = pd.DataFrame({"species": ["setosa", "versicolor", "virginica"],
                     "code": ["SET", "VER", "VIR"]})        # a small look-up table
merged = df.merge(info, on="species", how="left")
print(merged.drop_duplicates("species")[["species", "code"]])

# %% [markdown]
# ## Presenting tables
# * In a notebook the last expression of a cell is displayed as a formatted
#   table; `df.style` adds colours and formats (needs `jinja2`).
# * `df.to_markdown()` (needs `tabulate`) gives a Markdown table.
# * `df.to_excel("file.xlsx")` and the `python-docx` / `python-pptx` packages
#   create Word and PowerPoint files from Python.

# %%
print(wide[["species", "variable", "mean"]].head(3).round(2).to_markdown(index=False))
