import pandas as pd
from pathlib import Path


def ingest_data():

    BASE = Path(__file__).resolve().parent.parent

    raw_path = BASE / "data" / "raw"


    files = [
        "fund_master.csv",
        "nav_history.csv",
        "transactions.csv"
    ]


    data = {}


    for file in files:

        location = raw_path / file


        try:

            df = pd.read_csv(location)

            data[file] = df

            print(file, "loaded successfully")


        except Exception as e:

            print(file, "failed:", e)



    return data