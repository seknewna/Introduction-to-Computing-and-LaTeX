# %% [markdown]
# # 02 - Objects, Assignment and Data Types

# %% [markdown]
# ## Assignment
# Python uses a single assignment operator, `=`. A name:
# * may contain letters, digits and underscores, but cannot start with a digit;
# * is case-sensitive (`age` and `Age` are different);
# * cannot be a reserved word such as `for`, `if`, `class`.

# %%
a = 1
b = 2
a1 = a              # a new name for the same value
x, y = 10, 20       # assign several names at once
x, y = y, x         # swap two values
print(a, b, a1, x, y)

count = 5
count += 1          # shorthand for count = count + 1
print(count)

# %%
import keyword

print(keyword.kwlist[:10], "...")

# An invalid name raises a SyntaxError. We catch it here so the notebook goes on.
try:
    compile("v rsion = 4", "<demo>", "exec")      # a space inside a name
except SyntaxError as err:
    print("SyntaxError:", err.msg)

# %% [markdown]
# ## Data types
# Every value has a type. `type()` shows it and `isinstance()` tests it.

# %% [markdown]
# ### int and float (R: integer and numeric)

# %%
n = 55
pi_value = 3.14159
print(type(n), type(pi_value))
print(2 ** 100)          # Python integers can be arbitrarily large
print(0.1 + 0.2)         # floats are approximate: 0.30000000000000004

# %% [markdown]
# ### complex
# The imaginary unit is written `j`: `9 + 3j`.

# %%
z = 9 + 3j
print(z, type(z), z.real, z.imag)

z1 = a + 1j * b           # build a complex number from two real ones
print(z1, type(z1))

# %% [markdown]
# ### str (R: character)

# %%
text = "I am learning Python"
print(text, type(text), len(text))
print("LeaRning" == "Learning")      # case matters
print(text.upper(), "|", text.split())

# %% [markdown]
# ### bool (R: logical)

# %%
v = True
w = False
print(type(v), not v, v and w)
print(isinstance(True, int), True + True)   # bool is a kind of int: True == 1

# %% [markdown]
# ### bytes (R: raw)

# %%
raw_text = "I am learning Python.".encode("utf-8")
print(raw_text[:12], type(raw_text))
print(raw_text.decode("utf-8"))

# %% [markdown]
# ### None
# `None` represents "no value" (similar to R's `NULL`).

# %%
result = None
print(result, result is None, type(result))

# %% [markdown]
# ### Categories (R: factor)
# For categorical data, pandas provides a `category` type.

# %%
import pandas as pd

gender = pd.Series(["Female", "Male", "Male", "Female"], dtype="category")
print(gender.dtype)
print(gender.cat.categories.tolist())

# %% [markdown]
# ## Conversions
# Convert with the type's own name: `str()`, `int()`, `float()`, `bool()`.

# %%
print(str(55), type(str(55)))            # number -> text
print(int("123") + 1)                    # text -> integer
print(float("3.9"))                      # text -> float
print(int(3.9))                          # float -> int TRUNCATES: 3
print(bool(0), bool(""), bool("a"))      # empty/zero values are False

# %% [markdown]
# A string that is not a valid number raises an error instead of silently
# becoming a missing value (unlike R). Handle it with `try` / `except`:

# %%
try:
    int("3.9")        # not a valid integer literal
except ValueError as err:
    print("ValueError:", err)

# pandas can instead turn bad values into NaN, like R's NA:
print(pd.to_numeric("abc", errors="coerce"))
print(pd.to_numeric(pd.Series(["10", "x", "30"]), errors="coerce").tolist())
