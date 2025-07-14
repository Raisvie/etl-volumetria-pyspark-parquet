# Escrita com particionamento
def save_data(df):
    df.write \
        .mode("overwrite") \
        .partitionBy("data_pedido") \
        .parquet("data/processed/pedidos/")