def write_to_postgres(df, config, table):

    df.write \
        .format("jdbc") \
        .option("url", config["url"]) \
        .option("dbtable", table) \
        .option("user", config["user"]) \
        .option("password", config["password"]) \
        .mode("append") \
        .save()