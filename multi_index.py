import pandas as pd
import numpy as np


def run():
    # Index levels
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
    inside = [1, 2, 3, 1, 2, 3]

    hier_index = list(zip(outside, inside))
    hier_index = pd.MultiIndex.from_tuples(hier_index,
                                           names=['Group', 'Number'])
    print(hier_index)

    df = pd.DataFrame(np.random.randn(
        6, 2), index=hier_index, columns=['A', 'B'])
    print(df)

    print(df.loc['G1'])  # Select all rows with index 'G1'
    print(df.loc['G1'].loc[1])  # Select row with index 'G

    # Cross-section for level 'Number' with value '1'
    print(df.xs(1, level='Number'))


if __name__ == "__main__":
    run()
