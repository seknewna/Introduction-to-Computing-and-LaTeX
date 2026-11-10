# %% [markdown]
# # 15 - Introduction to Modeling: PCA, Clustering, KNN and Regression
# **scikit-learn** is Python's standard machine-learning library. Every model
# follows the same pattern: create it, `fit` it on data, then `predict` or
# `transform`.

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
species = iris.target_names

# %% [markdown]
# ## Principal Component Analysis
# Chapter 03 built PCA by hand; `PCA` does the same, plus scaling.

# %%
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X_scaled = StandardScaler().fit_transform(X)
pca = PCA().fit(X_scaled)
print(np.round(pca.explained_variance_ratio_, 3))      # share of the variance per component

scores = PCA(n_components=2).fit_transform(X_scaled)
for k, name in enumerate(species):
    plt.scatter(scores[y == k, 0], scores[y == k, 1], label=name, s=18)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.title("iris projected onto PC1 / PC2")
plt.show()

# %% [markdown]
# The first two components already explain most of the spread of the data.

# %% [markdown]
# ## Clustering
# ### K-means
# K-means never sees the species; comparing its groups with the real labels is
# only for evaluation.

# %%
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, n_init=10, random_state=1).fit(X)
print(pd.crosstab(km.labels_, species[y], rownames=["cluster"], colnames=["species"]))

# %% [markdown]
# ### Hierarchical clustering

# %%
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage

subset = X[:20]                                   # a small subset keeps the tree readable
tree = linkage(subset, method="complete")
dendrogram(tree)
plt.title("Hierarchical clustering (first 20 flowers)")
plt.show()
print(fcluster(tree, t=3, criterion="maxclust"))    # cut the tree into 3 groups

# %% [markdown]
# ## K-Nearest Neighbours (KNN)
# A supervised classifier: a flower gets the majority label of its `k` closest
# neighbours in the training data.

# %%
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
pred = knn.predict(X_test)
print("accuracy:", round(accuracy_score(y_test, pred), 3))
print(confusion_matrix(y_test, pred))

# %% [markdown]
# ## Simple linear regression
# Petal length explained by petal width (see also chapter 06):

# %%
from sklearn.linear_model import LinearRegression

petal_width, petal_length = X[:, [3]], X[:, 2]
lin = LinearRegression().fit(petal_width, petal_length)
print("intercept:", round(lin.intercept_, 3), " slope:", round(lin.coef_[0], 3))
print("R^2:", round(lin.score(petal_width, petal_length), 3))

# %% [markdown]
# ## Logistic regression
# For a yes/no outcome we use logistic regression. Here: *virginica* (1) versus
# *versicolor* (0), from the two sepal measurements. scikit-learn applies a
# regularisation penalty by default; a very large `C` switches it off in practice
# and gives the classical logistic regression.

# %%
from sklearn.linear_model import LogisticRegression

mask = y != 0                                    # keep versicolor and virginica
Xs, ys = X[mask][:, :2], (y[mask] == 2).astype(int)

logit = LogisticRegression(C=1e10, max_iter=5000).fit(Xs, ys)
print("coefficients:", np.round(logit.coef_[0], 3), " intercept:", np.round(logit.intercept_, 3))

prob = logit.predict_proba(Xs)[:, 1]
predicted = (prob > 0.5).astype(int)             # turn probabilities into classes at 0.5
print("accuracy:", round(accuracy_score(ys, predicted), 3))
print(confusion_matrix(ys, predicted))

# %% [markdown]
# For p-values and confidence intervals, the `statsmodels` package
# (`pip install statsmodels`) reports a full statistical summary, like R's
# `summary(glm(...))`.
