# etl-volumetria-pyspark-parquet

**Pipeline ETL modular em PySpark para processar grandes volumes de dados**  
geração de dados sinteticos, transformação de dados, particionamento e escrita em Parquet com boas práticas de engenharia de dados.

---

## 🛠️ Tecnologias

- **PySpark** – processamento distribuído  
- **Parquet** – formato colunar particionado por data  
- **Python 3.7+** – estrutura de projeto, configuração e testes  
- **pytest** – testes unitários das transformações  

---

## 🚀 Funcionalidades

1. **Geraçãp de dados_sinteticos**: Geração dados de alto volume (≥1 GB)
2. **Ingestão**: lê arquivos parquet de alto volume (≥1 GB)
3. **Transformação**: limpeza de dados, casting de tipos, enrich de colunas e deduplicação  
4. **Carga**: gravação em Parquet particionado (`data_pedido`)  
5. **Modularidade**:  
   - `src/config.py` → SparkSession e settings
   - `src/Dado_sinteticos_SOR.py` → Geração dados sinteticos
   - `src/ingest.py` → leitura dos dados  
   - `src/transform.py` → lógica de limpeza e enriquecimento  
   - `src/load.py` → escrita particionada  
   - `src/main.py` → orquestração do pipeline  
6. **Boas práticas**: configuração via `.env`, logging estruturado, testes unitários e diagrama de fluxo

---

## 💡 Como rodar

1. Clone o repositório  
   ```bash
   git clone https://github.com/seu-usuario/etl-volumetria-pyspark-parquet.git
   cd etl-volumetria-pyspark-parquet
