import pandas as pd
import numpy as np
from numpy.random import randn


def run():
    labels = ['a', 'b', 'c', 'd']
    my_list = [10, 20, 30, 40]
    arr = np.array([10, 20, 30, 40])
    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

    # Create a pandas Series from a list. Automatically assigns an index.
    pd.Series(labels)

    # Create a pandas Series from a list with custom index.
    pd.Series(data=labels, index=my_list)

    # Create a pandas Series from a numpy array. Automatically assigns an index.
    pd.Series(arr)

    # Create a pandas Series from a dictionary. The keys become the index.
    pd.Series(my_dict)

    ser1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
    ser2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])

    ser1['USA']  # Accessing a single value by index

    ser1 + ser2  # Adding two Series together, aligning by index

    # Create a DataFrame from a dictionary of Series.
    df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(),
                      columns='W X Y Z'.split())
    print(df)

    # This is a series of operations on the DataFrame.
    print(df['W'])  # Accessing a single column

    # Create a new column in the DataFrame
    df['new'] = df['W'] + df['Y']
    print(df)

    # Drop a column from the DataFrame
    # axis=1 means column, axis=0 means row, inplace=True modifies the DataFrame in place
    df.drop('new', axis=1, inplace=True)
    print(df)

    print(df.loc['A'])  # Accessing a row by label
    print(df.iloc[0])  # Accessing a row by index position

    print(df.loc[['A', 'B'], 'W'])  # Accessing specific rows and columns
    print(df.iloc[0:2, 0:2])  # Slicing rows and columns

    print(df > 0)  # Boolean indexing, returns rows where the condition is True
    # Returns the DataFrame with NaN where the condition is False
    print(df[df > 0])

    # Filtering rows based on a condition in a specific column
    print(df[df['W'] > 0])

    print(df.index)  # Accessing the index of the DataFrame
    print(df.columns)  # Accessing the columns of the DataFrame


if __name__ == "__main__":
    print("Pandas & Numpy.")
    run()
