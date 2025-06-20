import pandas as pd


def run():
    df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                      444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'jkl']})
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df["col1"].mean())
    print(df["col1"].max())
    print(df["col1"].min())
    print(df["col1"].sum())

    print(df["col2"].value_counts())
    print(df["col1"].apply(comp))


def comp(x):
    return x ** 2 + 3


if __name__ == "__main__":
    run()
