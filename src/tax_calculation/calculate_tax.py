import json
from tax_rules import calculate_tax_for_transaction

def calculate_tax_for_all_transactions(input_path, output_path):
    with open(input_path, 'r') as f:
        transactions = json.load(f)

    tax_data = []
    for tx in transactions:
        tax = calculate_tax_for_transaction(tx['volume_24h'], tx['price_24h'])
        tax_data.append({
            'symbol': tx['symbol'],
            'total_value': tx['volume_24h'] * tx['price_24h'],
            'estimated_tax': tax,
        })

    with open(output_path, 'w') as f:
        json.dump(tax_data, f)

if __name__ == '__main__':
    input_path = '/path/to/your/data/processed/blockchain_data_transformed.json'
    output_path = '/path/to/your/data/processed/tax_data.json'
    calculate_tax_for_all_transactions(input_path, output_path)
