import pandas as pd


def run():
    df = pd.read_csv("./datasets/exemplo.csv", sep=",", decimal=",")
    print(df)


if __name__ == "__main__":
    run()
