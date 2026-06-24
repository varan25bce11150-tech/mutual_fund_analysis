import pandas as pd
import os


RAW = "../data/raw/"
OUT = "../data/processed/"


# NAV CLEANING

nav = pd.read_csv(
    RAW+"nav_history.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

nav = nav.sort_values(
    ["scheme_code","date"]
)

nav["nav"] = nav["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]


nav.to_csv(
    OUT+"clean_nav_history.csv",
    index=False
)



# TRANSACTION CLEANING

txn = pd.read_csv(
    RAW+"transactions.csv"
)


txn["transaction_type"] = (
    txn["transaction_type"]
    .str.lower()
)


txn["transaction_type"] = txn[
"transaction_type"
].replace({

"sip":"SIP",
"lumpsum":"Lumpsum",
"redemption":"Redemption"

})


txn["amount"] = pd.to_numeric(
    txn["amount"]
)


txn = txn[txn["amount"] > 0]


txn["date"] = pd.to_datetime(
    txn["date"]
)


txn.to_csv(
    OUT+"clean_transactions.csv",
    index=False
)



# PERFORMANCE CLEANING

perf = pd.read_csv(
    RAW+"scheme_performance.csv"
)


perf["expense_ratio"] = pd.to_numeric(
    perf["expense_ratio"]
)


perf = perf[
(perf["expense_ratio"] >=0.1)
&
(perf["expense_ratio"]<=2.5)
]


perf.to_csv(
    OUT+"clean_performance.csv",
    index=False
)


print("Cleaning Completed")