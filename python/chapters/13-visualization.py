# %% [markdown]
# # 13 - Visualization: seaborn and plotly
# * **seaborn** builds statistical graphics on top of matplotlib — the Python
#   counterpart of `ggplot2` for everyday plots.
# * **plotly** makes interactive charts (hover, zoom).
#
# Install them with `pip install seaborn plotly`.

# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns=lambda c: c.replace(" (cm)", "").replace(" ", "_"))
df["species"] = df.pop("target").map(dict(enumerate(iris.target_names)))

# %% [markdown]
# ## seaborn
# Describe *which variables go where*; seaborn takes care of the rest.

# %%
sns.set_theme(style="whitegrid")

sns.boxplot(data=df, x="species", y="petal_length", hue="species", legend=False)
plt.title("Petal length by species")
plt.show()

# %% [markdown]
# A grid of small plots, one per species (R: `facet_grid`):

# %%
grid = sns.FacetGrid(df, col="species", height=3)
grid.map_dataframe(sns.histplot, x="petal_length", bins=10)
plt.show()

# %% [markdown]
# Relationships between several variables at once:

# %%
sns.pairplot(df, hue="species", height=1.8)
plt.show()

# %% [markdown]
# ## plotly
# `plotly.express` creates interactive figures in one line. In a notebook
# `fig.show()` displays them in place; in a script it opens your browser.

# %%
import plotly.express as px

counts = df["species"].value_counts().rename_axis("species").reset_index(name="n")
fig = px.pie(counts, names="species", values="n", title="Flowers per species")
fig.show()

# %%
fig = px.scatter(df, x="petal_width", y="petal_length", color="species",
                 hover_data=["sepal_length"], title="Hover over the points")
fig.show()

# %% [markdown]
# Save an interactive figure as a stand-alone web page you can share:

# %%
import tempfile
from pathlib import Path

html_path = Path(tempfile.mkdtemp()) / "iris_scatter.html"
fig.write_html(html_path, include_plotlyjs="cdn")      # the page loads plotly.js from the internet
print("saved:", html_path.name, round(html_path.stat().st_size / 1e3), "kB")
