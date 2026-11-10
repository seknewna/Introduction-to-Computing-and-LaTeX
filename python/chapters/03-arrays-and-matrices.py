# %% [markdown]
# # 03 - Sequences, Arrays and Matrices
# Python's built-in `list` can hold anything, but for numerical work we use
# **NumPy** arrays: fast, one type per array, and arithmetic works on the whole
# array at once (like R vectors and matrices).

# %%
import numpy as np

rng = np.random.default_rng(123)    # reproducible randomness (R: set.seed)

# %% [markdown]
# ## One-dimensional arrays

# %%
mixed = [1, "R", True, None]                  # a list may mix types
print(mixed)

numbers = np.array([1, 4, 8, False, True])    # an array has ONE type: everything -> int
print(numbers, numbers.dtype)

words = np.array([1, "R", True])              # ... or text, if a string is present
print(words, words.dtype)

# %% [markdown]
# ### Sequences

# %%
x = np.linspace(0, 2 * np.pi, 90)             # 90 equally spaced points
print(len(x), round(np.diff(x)[0], 5))        # the common step
print(x[:3], x[-3:])                          # first / last values (indices start at 0)
print(x.min(), x.max(), np.ptp(x))            # range = max - min

print(np.arange(0, 10, 2))                    # 0, 2, 4, 6, 8 (end is excluded)

# %% [markdown]
# ### Repetition

# %%
print(np.repeat("I learn Python", 2))
print(np.tile([0, 1], 5))              # 0 1 0 1 0 1 0 1 0 1
print(np.repeat([0, 1], 3))            # 0 0 0 1 1 1   (like rep(each = 3))

# %% [markdown]
# ### Random sampling and counting

# %%
y = rng.choice([0, 1], size=200, p=[1/3, 2/3])
values, counts = np.unique(y, return_counts=True)
print(dict(zip(values.tolist(), counts.tolist())))
print(counts / counts.sum())           # proportions
print(np.mean(y == 0))                 # the mean of a boolean array is a proportion

# %% [markdown]
# ### A small survey with typing mistakes

# %%
from collections import Counter

gender = ["Female", "Male", "Male", "Male", "Female", "Female", "Male", "Femaale",
          "Male", "Female", "Malle", "Male", "Female", "Femmale", "Female", "Male"]
print(Counter(gender))                       # the table, typos included

fixes = {"Femaale": "Female", "Femmale": "Female", "Malle": "Male"}
gender = [fixes.get(g, g) for g in gender]   # replace known typos
print(Counter(gender))

# %% [markdown]
# ### Array arithmetic (broadcasting)

# %%
k = 2
v = np.array([1, 0, 3])
print(k + v, k - v, k * v, v / k, k / np.where(v == 0, np.nan, v))
print(np.array([np.pi, 0, 1, 4]) ** 0.5)
print(np.array([1, 2, 3]) + np.array([10, 20, 30]))   # element by element

# %% [markdown]
# ## Matrices (two dimensions)
# NumPy fills a matrix **row by row**; R fills it column by column. Pass
# `order="F"` to `reshape` for R's behaviour.

# %%
A5 = np.arange(1, 26).reshape(5, 5)               # filled by rows
print(A5)
print(np.arange(1, 26).reshape(5, 5, order="F"))  # filled by columns, like R

# %%
M = np.array([[1, 5, 4],
              [0, 2, 2],
              [2, 1, 0]])
print(M.shape)                      # (3, 3)
print(np.zeros((2, 4)))             # a zero matrix

v1, v2, v3 = np.array([1, 0, 2]), np.array([5, 2, 1]), np.array([4, 2, 0])
print(np.column_stack([v1, v2, v3]))      # R: cbind
print(np.vstack([v1, v2, v3]))            # R: rbind

# %% [markdown]
# ### Matrix operations

# %%
A = M
B = np.array([[2, 3, 0],
              [5, 1, 1],
              [2, 1, 1]])

print(A.T)             # transpose
print(A + B)           # element-wise sum
print(A - B)
print(A * B)           # element-wise product (NOT the matrix product)
print(A @ B)           # matrix product

# %%
A_inv = np.linalg.inv(A)
print(np.round(A_inv, 3))
print(np.round(A @ A_inv))        # the identity matrix

# %% [markdown]
# ### Solving a system of equations
# $$
# \begin{cases} 2x + 2y = 0 \\ x + 3y = 2 \end{cases}
# $$

# %%
A1 = np.array([[2, 2],
               [1, 3]])
b = np.array([0, 2])
print(np.linalg.solve(A1, b))     # x = -1, y = 1

# %% [markdown]
# ### Eigenvalues and eigenvectors
# The eigenvalues $\lambda$ of a square matrix $A$ solve
# $\det(A - \lambda I) = 0$. They are the basis of Principal Component Analysis.

# %%
S = np.array([[2., -1., 0.],
              [-1., 2., -1.],
              [0., -1., 2.]])           # a symmetric matrix
values, vectors = np.linalg.eigh(S)     # eigh: for symmetric matrices
print(np.round(values, 4))
print(np.round(vectors.T @ S @ vectors, 4))   # a diagonal matrix of the eigenvalues

# %% [markdown]
# ## Worked exercise: PCA by hand on the iris data
# 1. Keep the four numeric columns.
# 2. Centre every column.
# 3. Eigen-decompose `X.T @ X`.
# 4. Project onto the first two eigenvectors.

# %%
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

X = load_iris().data                       # 150 flowers x 4 measurements
col_means = X.mean(axis=0)
print(np.round(col_means, 3))

Xc = X - col_means                         # centred data
cov = Xc.T @ Xc
eigvals, eigvecs = np.linalg.eigh(cov)     # eigenvalues in ascending order
order = np.argsort(eigvals)[::-1]          # sort from largest to smallest
eigvals, eigvecs = eigvals[order], eigvecs[:, order]
print(np.round(eigvals, 3))

projection = Xc @ eigvecs[:, :2]
print(np.round(projection[:3], 3))

# %% [markdown]
# This is exactly what scikit-learn's `PCA` does (the sign of an axis is
# arbitrary, so we compare absolute values):

# %%
scores = PCA(n_components=2).fit_transform(X)
print(np.allclose(np.abs(projection), np.abs(scores)))   # True
