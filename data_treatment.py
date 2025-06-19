import pandas as pd
import numpy as np


def run():
    df = pd.DataFrame({'A': [1, 2, np.nan],
                       'B': [5, np.nan, np.nan],
                       'C': [9, 10, 11]})
    print(df)
    print("------------------------------------------")
    print(df.dropna())  # Drop rows with any NaN values
    print("------------------------------------------")
    print(df.fillna(0))  # Fill NaN values with 0
    print("------------------------------------------")
    # Fill NaN with different values for each column
    print(df.fillna({'A': 0, 'B': 1, 'C': 2}))
    print("------------------------------------------")
    print(df.ffill())  # Forward fill NaN values
    print("------------------------------------------")


if __name__ == "__main__":
    run()
