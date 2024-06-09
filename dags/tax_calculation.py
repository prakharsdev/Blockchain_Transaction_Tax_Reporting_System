from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from google.cloud import bigquery
import json

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    'tax_calculation',
    default_args=default_args,
    description='Calculate tax from blockchain transactions',
    schedule_interval='@daily',
)

def calculate_tax(**kwargs):
    client = bigquery.Client()
    query = """
    SELECT
        symbol,
        SUM(volume_24h * price_24h) AS total_value,
        SUM(volume_24h * price_24h) * 0.15 AS estimated_tax
    FROM
        `your_project_id.your_dataset.blockchain_data`
    GROUP BY
        symbol
    """
    results = client.query(query).result()
    
    tax_data = []
    for row in results:
        tax_data.append({
            'symbol': row['symbol'],
            'total_value': row['total_value'],
            'estimated_tax': row['estimated_tax'],
        })

    with open('/path/to/your/data/processed/tax_data.json', 'w') as f:
        json.dump(tax_data, f)

calculate_tax_task = PythonOperator(
    task_id='calculate_tax',
    python_callable=calculate_tax,
    dag=dag,
)

calculate_tax_task
