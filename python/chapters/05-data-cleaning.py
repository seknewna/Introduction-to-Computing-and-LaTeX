# %% [markdown]
# # 05 - Data Cleaning: Missing Values and Outliers

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# ## Missing values (`NaN`)
# Missing numbers are represented by `np.nan` ("not a number"; R: `NA`).

# %%
x = np.array([np.nan, 1, 2, np.nan, 3, np.nan, 3.55])

print(np.where(np.isnan(x))[0])        # positions of the missing values
print(np.where(x >= 2)[0])             # NaN compares as False, so it drops out
print(np.where(~np.isnan(x))[0])       # positions that are NOT missing
print(np.mean(x), np.nanmean(x))       # NaN spreads through a mean; nanmean ignores it

# %% [markdown]
# Replace the missing values with the mean of the others:

# %%
x[np.isnan(x)] = np.nanmean(x)
print(x)

# %% [markdown]
# pandas has dedicated tools: `isna`, `fillna`, `dropna`, `interpolate`.

# %%
s = pd.Series([4.0, np.nan, 7.0, np.nan, 10.0])
print(s.isna().sum(), "missing")
print(s.fillna(s.mean()).tolist())
print(s.dropna().tolist())
print(s.interpolate().tolist())

# %% [markdown]
# ## Missing values created by conversion
# Converting messy text to numbers fails for anything that is not a clean number:

# %%
raw = pd.Series(["2", "1", "2", "7", "$8", "3", "2.5", "9", "2,7"])
y = pd.to_numeric(raw, errors="coerce")        # bad values become NaN
print(y.tolist())
print(raw[y.isna()].tolist())                  # the entries that failed

# %% [markdown]
# Clean the offending characters first, then convert:

# %%
messy = pd.Series(["2", "1", "2", ",7", "$8", "3", "&2.5", "9", "2,7"])
clean = (messy.str.replace(r"[$&]", "", regex=True)      # drop currency / junk symbols
              .str.replace(",", ".", regex=False))       # decimal comma -> dot
print(pd.to_numeric(clean).tolist())

# %% [markdown]
# ## Outlier detection: the IQR method
# A value is an outlier if it lies outside
# $$[Q_1 - 1.5\times IQR,\; Q_3 + 1.5\times IQR]$$
# where $IQR = Q_3 - Q_1$.

# %%
x = np.array([19.103, 19.632, 22.494, 20.113, 10.5, 22.744, 20.737, 17.976,
              18.901, 192.87, 21.959, 0.001, 20.641, 20.177, 19.111, 22.859,
              207.97, 16.853, 21.122, 19.244, 18.291, 19.651, 18.358, 18.834, 19])
x_original = x.copy()

plt.boxplot(x_original)
plt.title("Before handling outliers")
plt.show()

# %%
q1, q2, q3 = np.percentile(x, [25, 50, 75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print(f"Q1={q1:.3f}  Q3={q3:.3f}  IQR={iqr:.3f}  limits=({lower:.2f}, {upper:.2f})")

is_outlier = (x < lower) | (x > upper)
print(x[is_outlier])                    # the outliers themselves

# %% [markdown]
# ### Imputing the outliers
# Treat them as missing and fill them with the mean of the remaining values.

# %%
x[is_outlier] = np.nan
x[np.isnan(x)] = np.nanmean(x)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].boxplot(x_original)
axes[0].set_title("Before")
axes[1].boxplot(x)
axes[1].set_title("After")
plt.tight_layout()
plt.show()

# %% [markdown]
# No outliers remain after the replacement (see the right-hand panel).
