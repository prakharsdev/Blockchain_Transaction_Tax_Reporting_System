import json

def generate_tax_report(input_path, output_path):
    with open(input_path, 'r') as f:
        tax_data = json.load(f)

    report = 'Symbol, Total Value, Estimated Tax\n'
    for record in tax_data:
        report += f"{record['symbol']}, {record['total_value']}, {record['estimated_tax']}\n"

    with open(output_path, 'w') as f:
        f.write(report)

if __name__ == '__main__':
    input_path = '/path/to/your/data/processed/tax_data.json'
    output_path = '/path/to/your/reports/tax_report.csv'
    generate_tax_report(input_path, output_path)
