import json
from google.cloud import bigquery

def calculate_tax(request):
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
    query_job = client.query(query)
    results = query_job.result()
    
    tax_data = []
    for row in results:
        tax_data.append({
            'symbol': row['symbol'],
            'total_value': row['total_value'],
            'estimated_tax': row['estimated_tax'],
        })

    return json.dumps(tax_data), 200
