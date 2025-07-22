from pyspark.sql import SparkSession

def extrair_dados(spark: SparkSession, caminho: str):
    return spark.read.csv(caminho, header=True, inferSchema=True)