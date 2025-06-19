import pandas as pd
import numpy as np


def run():
    data = {'Class': ['Junior', 'Junior', 'Mid', 'Mid', 'Senior', 'Senior'],
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
            'Sales': [200, 150, 300, 400, 500, 600], }

    df = pd.DataFrame(data)
    print(df)

    print("------------------------------------------")

    by_class = df.groupby('Class')
    print(by_class.sum())  # Sum of sales by class


if __name__ == "__main__":
    run()
