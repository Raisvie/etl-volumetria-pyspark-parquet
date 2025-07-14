# geracao de dados sinteticos
from faker import Faker
import pandas as pd
import random

fake = Faker()
data = []
for _ in range(1_000_000):
    data.append({
        "pedido_id": fake.uuid4(),
        "restaurante": fake.company(),
        "cliente_id": fake.uuid4(),
        "valor_total": round(random.uniform(10, 150), 2),
        "data_pedido": fake.date_between(start_date='-30d', end_date='today').isoformat(),
        "forma_pagamento": random.choice(['crédito', 'débito', 'pix', 'voucher']),
    })

df = pd.DataFrame(data)
df.to_csv("data/raw/pedidos.csv", index=False)