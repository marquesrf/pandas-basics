import pandas as pd


def run():
    num_days = 100

    dates = pd.date_range(start="2023-01-01", periods=num_days)
    df = pd.DataFrame(range(num_days), index=dates, columns=["number"])
    print(df)

    print(df.index[47].day)
    print(df.index[47].month)
    print(df.index[47].year)
    print(df.index[47].hour)
    print(df[df.index.day == 5])


if __name__ == "__main__":
    run()
