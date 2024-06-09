from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from neo4j import GraphDatabase
import json

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    'neo4j_integration',
    default_args=default_args,
    description='Load processed data into Neo4j and perform analysis',
    schedule_interval='@daily',
)

NEO4J_URI = 'bolt://localhost:7687'
NEO4J_USERNAME = 'neo4j'
NEO4J_PASSWORD = 'your_password'

def load_to_neo4j(**kwargs):
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    with driver.session() as session:
        with open('/path/to/your/data/processed/tax_data.json', 'r') as f:
            tax_data = json.load(f)
        
        for record in tax_data:
            session.run(
                """
                MERGE (t:Transaction {symbol: $symbol})
                SET t.total_value = $total_value, t.estimated_tax = $estimated_tax
                """,
                symbol=record['symbol'],
                total_value=record['total_value'],
                estimated_tax=record['estimated_tax'],
            )

def analyze_transactions(**kwargs):
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    with driver.session() as session:
        results = session.run(
            """
            MATCH (t:Transaction)
            RETURN t.symbol AS symbol, t.total_value AS total_value, t.estimated_tax AS estimated_tax
            ORDER BY t.total_value DESC
            LIMIT 10
            """
        )
        analysis_results = []
        for record in results:
            analysis_results.append({
                'symbol': record['symbol'],
                'total_value': record['total_value'],
                'estimated_tax': record['estimated_tax'],
            })
        
        with open('/path/to/your/data/processed/neo4j_analysis_results.json', 'w') as f:
            json.dump(analysis_results, f)

load_task = PythonOperator(
    task_id='load_to_neo4j',
    python_callable=load_to_neo4j,
    dag=dag,
)

analyze_task = PythonOperator(
    task_id='analyze_transactions',
    python_callable=analyze_transactions,
    dag=dag,
)

load_task >> analyze_task
