# %% [markdown]
# # 11 - Importing Data
# > **Note on file paths.** The examples below create small temporary files and
# > read them back, so every cell runs on any computer. To use your own data,
# > replace the temporary path by the path of your file.

# %%
import tempfile
import time
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris

workdir = Path(tempfile.mkdtemp())

# %% [markdown]
# ## Built-in data
# scikit-learn ships small example datasets that are ready to use.

# %%
iris = load_iris(as_frame=True)
df = iris.frame.rename(columns=lambda c: c.replace(" (cm)", "").replace(" ", "_"))
df["species"] = df.pop("target").map(dict(enumerate(iris.target_names)))

df.info()                                   # column names, types, missing values
print(df.describe().round(2))
print(df.shape)

# %% [markdown]
# Checking the type of every column, timed with the standard `time` module:

# %%
start = time.perf_counter()
dtypes = [str(df[col].dtype) for col in df.columns]
print(f"{time.perf_counter() - start:.6f} seconds")
print(sorted(set(dtypes)))

# %% [markdown]
# ## CSV files (R: read.csv / read_csv)

# %%
csv_path = workdir / "iris.csv"
df.to_csv(csv_path, index=False)             # write
data = pd.read_csv(csv_path)                 # read
print(data.head(3))
print(data["species"].dtype)                 # text ("object" / "str")

data["species"] = data["species"].astype("category")     # R: stringsAsFactors
print(data["species"].dtype)

# %% [markdown]
# Useful options of `read_csv`: `sep=";"`, `decimal=","`, `na_values=["NA", "-"]`,
# `usecols=[...]`, `nrows=100`, `encoding="latin-1"`.

# %% [markdown]
# ## Excel files (needs the `openpyxl` package: `pip install openpyxl`)

# %%
xlsx_path = workdir / "iris.xlsx"
try:
    df.head(5).to_excel(xlsx_path, index=False)
    print(pd.read_excel(xlsx_path).head(2))
except ImportError:
    print("Install openpyxl first:  pip install openpyxl")

# %% [markdown]
# ## JSON files

# %%
json_path = workdir / "iris.json"
df.head(3).to_json(json_path, orient="records")
print(json_path.read_text()[:120], "...")
print(pd.read_json(json_path).shape)

# %% [markdown]
# ## Exercise: import every CSV file in a folder with a loop

# %%
folder = workdir / "demo_csv"
folder.mkdir()
df.head(3).to_csv(folder / "iris_part.csv", index=False)
df.tail(3).to_csv(folder / "iris_end.csv", index=False)

frames = {}
for path in sorted(folder.glob("*.csv")):
    frames[path.name] = pd.read_csv(path)
    print(path.name, frames[path.name].shape)

combined = pd.concat(frames, names=["file", "row"])     # one table, remembering the file
print(combined.shape)
print(combined.reset_index(level="file").head(4))
