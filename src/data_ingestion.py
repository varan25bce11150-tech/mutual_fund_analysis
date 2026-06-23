import pandas as pd
import os


files = [
    "fund_master.csv",
    "nav_history.csv",
    "transactions.csv"
]


path = "data/raw/"


for file in files:

    location = os.path.join(path,file)

    df = pd.read_csv(location)


    print("\n===================")
    print(file)

    print("Shape:")
    print(df.shape)


    print("\nData Types:")
    print(df.dtypes)


    print("\nFirst 5 rows:")
    print(df.head())


    print("\nMissing Values:")
    print(df.isnull().sum())