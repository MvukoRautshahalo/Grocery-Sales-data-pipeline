import yaml
from ingest.ingest_data import load_csv
from transform.transform_sales import transform_sales
from load.load_postgres import write_to_postgres


def run_pipeline(spark):

    config = yaml.safe_load(open("config/config.yaml"))

    # --- Ingest ---
    customers_df = load_csv(spark, config["files"]["customers"])
    products_df = load_csv(spark, config["files"]["products"])
    sales_df = load_csv(spark, config["files"]["sales"])

    # --- Transform ---
    features_df = transform_sales(sales_df, customers_df, products_df)

    # --- Load ---
    write_to_postgres(
        features_df,
        config["postgres"],
        "feature_customer_monthly"
    )


if __name__ == "__main__":
    run_pipeline(spark)