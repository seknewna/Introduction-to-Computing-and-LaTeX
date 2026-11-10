# %% [markdown]
# # 01 - Operators
# Python can be used as a calculator straight away. Every operator below can be
# typed in a notebook cell, or in the interactive prompt (`python3`).

# %% [markdown]
# ## Arithmetic operators

# %%
print(1 + 1)        # addition
print(5 - 1)        # subtraction
print(3 * 4)        # multiplication
print(7 / 2)        # true division: always a float -> 3.5
print(1035 // 3)    # integer (floor) division -> 345
print(7 % 2)        # modulus (remainder) -> 1
print(2 ** 10)      # exponent -> 1024

# %% [markdown]
# Floor division and modulus follow the sign of the divisor, so
# `a == (a // b) * b + a % b` always holds:

# %%
print(-7 // 2, -7 % 3)   # -4  2
print((-7 // 2) * 2 + (-7 % 2))   # -7

# %% [markdown]
# ## Comparison operators
# Each comparison returns `True` or `False`.

# %%
print(1 < 1)
print(1 <= 1)
print(1 > 1)
print(1 >= 1)
print("R" == "r")     # Python is case-sensitive
print(1 != 1)
print(1 < 2 < 3)      # comparisons can be chained

# %% [markdown]
# ## Logical operators
# In plain Python the logical operators are the words `and`, `or`, `not`.

# %%
print(not True)
print(not (True and False))
print(True and True, True and False, False and False)
print(True or True, True or False, False or False)

# %% [markdown]
# On NumPy arrays and pandas columns, use the symbols `&` (and), `|` (or) and
# `~` (not) to combine conditions element by element, with parentheses around
# each condition.

# %%
import numpy as np

scores = np.array([45, 72, 88, 61, 95])
print((scores > 60) & (scores < 90))   # between 60 and 90
print((scores < 50) | (scores > 90))   # very low or very high
print(~(scores > 60))                  # not above 60

# %% [markdown]
# ## Membership and value matching
# `in` tells you whether a value is present. `list.index()` gives its position
# — but remember that Python counts positions **from 0**.

# %%
columns = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"]

print("Species" in columns)          # True
print("Weight" not in columns)       # True
print(columns.index("Species"))      # 4  (the 5th element)

# %% [markdown]
# For many values at once on an array, use `np.isin`:

# %%
print(np.isin(["Species", "Weight"], columns))   # [ True False]
