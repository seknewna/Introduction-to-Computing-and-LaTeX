# %% [markdown]
# # 14 - Regular Expressions
# A regular expression (regex) is a pattern used to detect, extract or replace
# text. Python's `re` module provides them, and pandas exposes them through
# `Series.str`.

# %%
import re

text = ["dave@example.com", "call 555-1234", "no match here", "ID: R2024-001"]

# %% [markdown]
# ## Detecting matches
# `re.search` finds a pattern *anywhere* in a string and returns a match object
# (or `None`).

# %%
print([bool(re.search(r"[0-9]+", t)) for t in text])
print([t for t in text if re.search(r"[0-9]+", t)])        # keep the matching strings

# %% [markdown]
# ## Replacing matches
# `re.sub` replaces **every** match; add `count=1` to replace only the first.

# %%
print([re.sub(r"[0-9]+", "#", t) for t in text])
print([re.sub(r"[0-9]+", "#", t, count=1) for t in text])

# %% [markdown]
# ## Extracting matches
# `re.findall` returns every match; `match.group()` returns the text of one.

# %%
print([re.findall(r"[0-9]+", t) for t in text])
print([m.group() if (m := re.search(r"[0-9]+", t)) else None for t in text])

# %% [markdown]
# ## Capturing parts of a match with groups

# %%
m = re.search(r"(?P<user>[\w.]+)@(?P<domain>[\w.]+)", "write to dave@example.com today")
print(m.group("user"), m.group("domain"), m.span())

# %% [markdown]
# ## A practical pattern: validating an email address
# `re.fullmatch` requires the *whole* string to match.

# %%
email_pattern = re.compile(r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}")

for candidate in ["dave@example.com", "bad.email@@x", "no-at-sign.com", "user@nodot", "a.b@c.org"]:
    print(f"{candidate:20s} {bool(email_pattern.fullmatch(candidate))}")

# %% [markdown]
# ## Common building blocks
#
# | Pattern | Matches |
# |---|---|
# | `[0-9]` or `\d` | any digit |
# | `[a-zA-Z]` | any letter |
# | `.` | any single character |
# | `+` | one or more of the previous token |
# | `*` | zero or more of the previous token |
# | `^` / `$` | start / end of the string |
# | `\s` | whitespace |
# | `a\|b` | `a` or `b` |
#
# Write patterns as **raw strings** (`r"..."`) so that backslashes are kept.

# %% [markdown]
# ## Regex in pandas (R: stringr)

# %%
import pandas as pd

s = pd.Series(text)
print(s.str.contains(r"[0-9]+").tolist())
print(s.str.extract(r"([0-9]+)")[0].tolist())            # first number, NaN if none
print(s.str.replace(r"[0-9]+", "#", regex=True).tolist())
print(s.str.findall(r"[0-9]+").tolist())

# %% [markdown]
# ## Exercise: standardise messy product codes
# Extract only the numeric ID from codes written in different styles.

# %%
codes = ["PRD-2023-001", "prd2023002", "PRD_2023_003", "Prd 2023 004", "PRD-2023-005"]
ids = [re.search(r"(\d{3})\D*$", c).group(1) for c in codes]       # the last three digits
print(ids)
years = [re.search(r"(20\d\d)", c).group(1) for c in codes]
print([f"PRD-{year}-{i}" for year, i in zip(years, ids)])
