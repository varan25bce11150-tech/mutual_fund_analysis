from data_ingestion import ingest_data
from load_database import load_database


def run_pipeline():

    print("Starting ETL Pipeline")


    ingest_data()


    load_database()


    print("ETL Pipeline Completed Successfully")


if __name__ == "__main__":

    run_pipeline()