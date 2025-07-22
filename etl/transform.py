from pyspark.sql.functions import col

def limpar_dados(df):
    return (df
            .dropna()
            .dropDuplicates()
            .withColumn("valor_pedido", col("valor_pedido").cast("float"))
            .filter(col("valor_pedido") > 0)
    )