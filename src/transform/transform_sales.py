from pyspark.sql.functions import col, to_timestamp, trunc, sum as _sum, count, avg


def transform_sales(sales_df, customers_df, products_df):

    # --- Clean sales ---
    sales_df = sales_df.withColumn(
        "sales_date", to_timestamp(col("SalesDate"))
    )

    sales_df = sales_df.withColumn(
        "month", trunc(col("sales_date"), "month")
    )

    # --- Join dimensions ---
    df = sales_df \
        .join(customers_df, "CustomerID", "left") \
        .join(products_df, "ProductID", "left")

    # --- Aggregation (customer-level features) ---
    agg_df = df.groupBy("CustomerID", "month").agg(
        _sum("TotalPrice").alias("total_spend"),
        count("SalesID").alias("order_count"),
        avg("TotalPrice").alias("avg_order_value"),
        _sum("Quantity").alias("total_units")
    )

    return agg_df