# geracao de dados sinteticos
from faker import Faker
import pandas as pd
import random

fake = Faker()
#padronização de dados para testes futuros padrão 42 de aleatorios
#random.seed(42)

def gerar_dados_sor(n_registros=1_000_000, salvar_em="data/raw/pedidos.csv"):
    data_gerados = []
    ## geração de 1 milhão de registros sintéticos de pedidos para simulação
    for i in range(1_000_000):
        data_gerados.append({
            "pedido_id": f"{random.randint(10000, 99999)}",
            "restaurante_id": f"{random.randint(10000, 99999)}",
            "cliente_id": f"{random.randint(10000, 99999)}",
            "valor_total": round(random.uniform(10, 150), 2),
            "data_pedido": fake.date_between(start_date='-30d', end_date='today').isoformat(),
            "forma_pagamento": random.choice(['crédito', 'débito', 'pix', 'voucher']),
        })

    df_SOR = pd.DataFrame(data_gerados)
    df_SOR.to_parquet("pedidos.parquet", index=False)

    print(f"✔️ {n_registros} registros salvos")

if __name__ == "__main__":
    gerar_dados_sor()