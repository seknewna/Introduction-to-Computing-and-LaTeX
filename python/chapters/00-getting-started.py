# %% [markdown]
# # 00 - Getting Started with Python
# *Python Programming — the Python counterpart of the R course*
#
# ## What is Python?
# Python is a general-purpose programming language created by Guido van Rossum
# and first released in 1991. Its clear, readable syntax and its huge ecosystem
# (data analysis, machine learning, web, automation) have made it one of the
# most widely used languages in the world.
#
# ## Install Python
# Download the installer for your system from <https://www.python.org/downloads/>.
# On Linux, Python is usually pre-installed; if not:
# `sudo apt install python3 python3-pip python3-venv`.
#
# ## Check the installation (in a terminal)
# ```bash
# python3 --version
# pip --version
# ```
#
# ## Work in a virtual environment
# A virtual environment keeps the packages of one project separate from another.
# ```bash
# python3 -m venv .venv
# source .venv/bin/activate          # Windows: .venv\Scripts\activate
# pip install numpy pandas matplotlib scipy scikit-learn jupyterlab
# ```
#
# ## Where to write code
# * **JupyterLab / Jupyter Notebook** — notebooks mix text, code and results.
# * **VS Code** with the Python extension.
# * **Google Colab** — nothing to install, runs in the browser.
#
# These chapters are written in the "percent" format: every line that starts
# with `# %%` begins a new cell. Jupyter (with Jupytext), VS Code and Spyder open
# them as notebooks, and they also run as ordinary scripts with
# `python3 chapter.py`. A ready-made `.ipynb` version of each chapter is
# provided next to it.

# %%
# Run this cell to check your setup.
import sys

print("Python", sys.version.split()[0])

packages = {"numpy": "numpy", "pandas": "pandas", "matplotlib": "matplotlib",
            "scipy": "scipy", "sklearn": "scikit-learn"}
for module_name, pip_name in packages.items():
    try:
        module = __import__(module_name)
        print(f"{module_name:12s} {module.__version__}")
    except ImportError:
        print(f"{module_name:12s} NOT INSTALLED  ->  pip install {pip_name}")

# %%
print("Hello, Python!")
