import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

dates = pd.date_range("20130101", periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

# print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

# print(df.columns)
# print(df.to_numpy())
# rnd = np.random.randn(3, 2)
# print(rnd)

# dfs = df.sort_values(by="B")
# print(dfs)
# print(dfs["A"])
# print(dfs[0:3])

# Selection by labe
# print(df.loc[dates[1]])

# Selecting on a multi-axis by label:
# print(df.loc[:,["A","B"]])

# print(df.at[dates[0], "A"])


# Selection by position
# print(df.iloc[3])

# print(df.iloc[4:5, 0:4])

# print(df.iloc[[1,2,3],[0,2]])

# For getting fast access to a scalar (equivalent to the prior method):
# df.iloc[1, 1]
# print(df.iat[1,1])

# print(df[df["B"] > 0])

# print(df[df> 0])

# df2 = df.copy()
# df2["E"] = ["one", "one", "two", "three", "four", "three"]
#
# print(df2[df2["E"]].isin())

# print(df.sum())
print(df.apply(lambda x: x.max() - x.min()))