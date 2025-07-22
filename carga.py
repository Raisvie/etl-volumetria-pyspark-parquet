from pyspark.sql import SparkSession
from src.etl.extracao import extrair_dados
from src.etl.transform import limpar_dados
from src.etl.load import salvar_parquet

def criar_spark():
    return SparkSession.builder \
        .appName("ETL Restaurantes") \
        .getOrCreate()

if __name__ == "__main__":
    spark = criar_spark()

    df_raw = extrair_dados(spark, "data/raw/pedidos.csv")
    df_limpo = limpar_dados(df_raw)
    salvar_parquet(df_limpo, "data/processed/pedidos.parquet")

    spark.stop()