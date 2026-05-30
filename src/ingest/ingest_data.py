def load_csv(spark, path):
    df = spark.read.csv(path, header=True, inferSchema=True)
    df = df.dropDuplicates()
    return df