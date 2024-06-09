import json
from google.cloud import bigquery

def hello_world(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    return f'Hello, {name}!'

def insert_transaction(request):
    client = bigquery.Client()
    data = request.get_json()

    table_id = "your_project_id.your_dataset.transactions"
    rows_to_insert = [
        {
            "symbol": data['symbol'],
            "total_value": data['total_value'],
            "estimated_tax": data['estimated_tax'],
        }
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        return json.dumps({"success": True}), 200
    else:
        return json.dumps({"success": False, "errors": errors}), 400
