# %% [markdown]
# # 07 - Flow Control: Conditionals and Loops
# Python marks blocks with **indentation** (4 spaces) instead of braces.

# %%
import numpy as np

rng = np.random.default_rng(123)

# %% [markdown]
# ## if / elif / else

# %%
x = 3
if x < 4:
    print(True)
else:
    print(False)

print(True if x < 4 else False)      # one-line conditional expression

values = np.array([3, 4, 6, 7, 0, 4])
print(np.where(values < 4, True, False))    # vectorised version (R: ifelse)

# %% [markdown]
# ### Grading example
# Categorise each mark: Fail [0, 60), Pass [60, 70), Good Pass [70, 80),
# Very Good Pass [80, 85), Distinction [85, ...).

# %%
marks = np.round(rng.normal(60, 15, size=50), 2)

# Approach 1: loop over the values
categories = []
for m in marks:
    if m < 60:
        categories.append("Fail")
    elif m < 70:
        categories.append("Pass")
    elif m < 80:
        categories.append("Good Pass")
    elif m < 85:
        categories.append("Very Good Pass")
    else:
        categories.append("Distinction")
print(list(zip(marks[:5], categories[:5])))

# %%
# Approach 2: vectorised with np.select
conditions = [marks < 60, marks < 70, marks < 80, marks < 85]
labels = ["Fail", "Pass", "Good Pass", "Very Good Pass"]
categories2 = np.select(conditions, labels, default="Distinction")
print(list(categories) == categories2.tolist())      # True: same result

# %% [markdown]
# ## for loops

# %%
for i in range(1, 11):          # 1 .. 10  (the end value 11 is excluded)
    if i % 3 == 0:
        print(i, "is a multiple of 3")
    elif i % 2 == 0:
        print(i, "is a multiple of 2")
    else:
        print(i, "is neither a multiple of 2 nor 3")

# %% [markdown]
# ### Exercise 1: odd or even

# %%
for i in range(1, 11):
    print(i, "is even" if i % 2 == 0 else "is odd")

# %% [markdown]
# `enumerate` gives the position and the value; `zip` walks through several
# sequences together:

# %%
names = ["Ada", "Bob", "Chloe"]
ages = [36, 41, 29]
for position, (name, age) in enumerate(zip(names, ages), start=1):
    print(position, name, age)

# %% [markdown]
# ### Exercise 2: import every CSV file in a folder
# We first create a small demo folder, then read all its files in a loop.

# %%
import tempfile
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris

folder = Path(tempfile.mkdtemp()) / "demo_csv"
folder.mkdir()
iris = load_iris(as_frame=True).frame
iris.head(3).to_csv(folder / "iris_part.csv", index=False)
iris.tail(3).to_csv(folder / "iris_end.csv", index=False)

data = {}
for path in sorted(folder.glob("*.csv")):        # every .csv file in the folder
    data[path.name] = pd.read_csv(path)
for name, frame in data.items():
    print(name, frame.shape)

# %% [markdown]
# ## while loops

# %%
i = 0
while i <= 10:
    print(i * 2)
    i += 10

# %% [markdown]
# ### Exercise: a dice streak game
# Roll a die until three 5s appear **in a row**.

# %%
streak, rolls = 0, 0
while streak < 3:
    rolls += 1
    roll = int(rng.integers(1, 7))
    streak = streak + 1 if roll == 5 else 0
print(f"YOU WON! after {rolls} rolls")

# %% [markdown]
# ### `break`, `continue` and `while True`
# `while True` with `break` plays the role of R's `repeat`.

# %%
i = 0
while True:
    i += 1
    if i == 3:
        continue          # skip the rest of this round
    print(i)
    if i >= 5:
        break             # leave the loop

# %% [markdown]
# ### Exercise: an interactive multiplication table
# `input()` waits for the user, so this needs a live session. Put the code in a
# function and call it yourself:

# %%
def multiplication_table():
    while True:
        number = int(input("Enter a number 0-9: "))
        for k in range(1, 11):
            print(f"{number} x {k} = {number * k}")
        if input("Continue? (y/n): ").lower() != "y":
            break

# multiplication_table()      # un-comment to try it in a notebook
