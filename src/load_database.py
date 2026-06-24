import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
"sqlite:///bluestock_mf.db"
)


files = {

"fact_nav":
"data/processed/clean_nav_history.csv",

"fact_transactions":
"data/processed/clean_transactions.csv",

"fact_performance":
"data/processed/clean_performance.csv"

}


for table,file in files.items():

    df=pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )


print("Database Loaded")