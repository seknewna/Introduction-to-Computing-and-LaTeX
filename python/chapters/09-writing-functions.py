# %% [markdown]
# # 09 - Writing Functions in Python

# %% [markdown]
# ## Function syntax
# ```python
# def function_name(arg1, arg2=default):
#     """Docstring: what the function does."""
#     ...
#     return result
# ```

# %%
import numpy as np

rng = np.random.default_rng(1)


def toss_die():
    """Roll one six-sided die."""
    return int(rng.integers(1, 7))


print([toss_die() for _ in range(10)])


def add_one(x):
    return x + 1


i = 1
i = add_one(i)
print(i)

# %% [markdown]
# ## Default values, keyword arguments and several results

# %%
def describe(values, decimals=2):
    """Return (mean, standard deviation) of a sequence."""
    values = np.asarray(values, dtype=float)
    return round(values.mean(), decimals), round(values.std(ddof=1), decimals)


mean, sd = describe([4, 8, 15, 16, 23, 42])         # a function can return several values
print(mean, sd)
print(describe([4, 8, 15, 16, 23, 42], decimals=0))  # a keyword argument

square = lambda v: v ** 2        # a short anonymous function
print(square(7))

# %%
def total(*numbers, **options):
    """*numbers collects extra positional arguments, **options keyword ones."""
    result = sum(numbers)
    return result * options.get("factor", 1)


print(total(1, 2, 3), total(1, 2, 3, factor=10))

# %% [markdown]
# ## Exercises
# ### 1. Replace missing values with a summary statistic

# %%
def replace_missing(x, fun=np.nanmean):
    """Replace NaN values in x by fun(x), ignoring NaN. Returns a new array."""
    x = np.asarray(x, dtype=float).copy()
    x[np.isnan(x)] = fun(x)
    return x


test = [1, 2, np.nan, 4, np.nan, 6]
print(replace_missing(test))
print(replace_missing(test, fun=np.nanmedian))

# %% [markdown]
# ### 2. Solve a quadratic equation and comment on its discriminant
# For $ax^2+bx+c=0$ the discriminant is $\Delta=b^2-4ac$:
# * $\Delta>0$ — two distinct real roots
# * $\Delta=0$ — one repeated real root
# * $\Delta<0$ — two complex conjugate roots

# %%
import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a must be non-zero for a quadratic equation")
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        print("Two distinct real roots")
        return ((-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a))
    if delta == 0:
        print("One repeated real root")
        return (-b / (2 * a),)
    print("Two complex conjugate roots")
    real, imag = -b / (2 * a), math.sqrt(-delta) / (2 * a)
    return (complex(real, imag), complex(real, -imag))


print(solve_quadratic(1, -3, 2))   # delta > 0
print(solve_quadratic(1, 2, 1))    # delta = 0
print(solve_quadratic(1, 0, 1))    # delta < 0

# %% [markdown]
# ## Scope
# A variable created inside a function is local to it.

# %%
counter = 0


def increase():
    counter = 100          # a NEW local variable; the outer one is untouched
    return counter


increase()
print(counter)             # still 0
