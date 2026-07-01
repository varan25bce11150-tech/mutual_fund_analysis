import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


def load_database():

    BASE = Path(__file__).resolve().parent.parent


    engine = create_engine(
        "sqlite:///bluestock_mf.db"
    )


    files = {

    "fact_nav":
    BASE/"data/processed/clean_nav_history.csv",


    "fact_transactions":
    BASE/"data/processed/clean_transactions.csv",


    "fact_performance":
    BASE/"data/processed/clean_performance.csv"

    }



    for table,file in files.items():

        try:

            df = pd.read_csv(file)


            df.to_sql(
                table,
                engine,
                if_exists="replace",
                index=False
            )


            print(table,"loaded")


        except Exception as e:

            print(table,"failed:",e)



    print("Database Loaded")