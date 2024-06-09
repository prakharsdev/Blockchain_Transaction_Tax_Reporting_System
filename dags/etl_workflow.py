from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from google.cloud import bigquery
import requests
import json
import os

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    'etl_workflow',
    default_args=default_args,
    description='ETL workflow for blockchain data',
    schedule_interval='@daily',
)

def extract_data(**kwargs):
    response = requests.get('https://api.blockchain.com/v3/exchange/tickers')
    raw_data = response.json()
    with open('/path/to/your/data/raw/blockchain_data.json', 'w') as f:
        json.dump(raw_data, f)

def transform_data(**kwargs):
    with open('/path/to/your/data/raw/blockchain_data.json', 'r') as f:
        raw_data = json.load(f)
    
    transformed_data = []
    for item in raw_data:
        transformed_data.append({
            'symbol': item['symbol'],
            'price_24h': item['price_24h'],
            'volume_24h': item['volume_24h'],
        })

    with open('/path/to/your/data/processed/blockchain_data_transformed.json', 'w') as f:
        json.dump(transformed_data, f)

def load_data(**kwargs):
    client = bigquery.Client()
    dataset_ref = client.dataset('your_bigquery_dataset')
    table_ref = dataset_ref.table('blockchain_data')
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField('symbol', 'STRING'),
            bigquery.SchemaField('price_24h', 'FLOAT'),
            bigquery.SchemaField('volume_24h', 'FLOAT'),
        ],
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )

    with open('/path/to/your/data/processed/blockchain_data_transformed.json', 'rb') as f:
        job = client.load_table_from_file(f, table_ref, job_config=job_config)
    job.result()

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_task >> transform_task >> load_task
