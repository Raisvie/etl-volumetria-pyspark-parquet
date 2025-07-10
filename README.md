# etl-volumetria-pyspark-parquet

**Pipeline ETL modular em PySpark para processar grandes volumes de dados**  
Leitura de CSV, transformação de dados, particionamento e escrita em Parquet com boas práticas de engenharia.

---

## 🛠️ Tecnologias

- **PySpark** – processamento distribuído  
- **Parquet** – formato colunar particionado por data  
- **Python 3.8+** – estrutura de projeto, configuração e testes  
- **pytest** – testes unitários das transformações  

---

## 🚀 Funcionalidades

1. **Ingestão**: lê arquivos CSV de alto volume (≥1 GB)  
2. **Transformação**: limpeza de dados, casting de tipos, enrich de colunas e deduplicação  
3. **Carga**: gravação em Parquet particionado (`data_pedido`)  
4. **Modularidade**:  
   - `src/config.py` → SparkSession e settings  
   - `src/ingest.py` → leitura dos dados  
   - `src/transform.py` → lógica de limpeza e enriquecimento  
   - `src/load.py` → escrita particionada  
   - `src/main.py` → orquestração do pipeline  
5. **Boas práticas**: configuração via `.env`, logging estruturado, testes unitários e diagrama de fluxo

---

## 💡 Como rodar

1. Clone o repositório  
   ```bash
   git clone https://github.com/seu-usuario/etl-volumetria-pyspark-parquet.git
   cd etl-volumetria-pyspark-parquet
