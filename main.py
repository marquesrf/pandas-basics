import pandas as pd

df_data = pd.read_csv('./datasets/supermarket_sales.csv')


def run():
    """
    Main function to run the script.
    """
    print(df_data.head())
    print(f"Total records: {len(df_data)}")
    print(f"Columns: {df_data.columns.tolist()}")


if __name__ == "__main__":
    print("Data loaded successfully.")
    run()
