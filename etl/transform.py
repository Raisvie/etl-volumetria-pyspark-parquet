from pyspark.sql.functions import col, to_date, when

def transform_data(df):
    return df \
        .withColumn("data_pedido", to_date(col("data_pedido"))) \
        .withColumn("valor_total", col("valor_total").cast("double")) \
        .withColumn("categoria_pagamento",
            when(col("forma_pagamento") == "pix", "instantâneo")
            .when(col("forma_pagamento") == "crédito", "crédito")
            .otherwise("outros")
        ) \
        .dropDuplicates(["pedido_id"])