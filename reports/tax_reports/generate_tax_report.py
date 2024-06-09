import pandas as pd
import json

def generate_tax_report():
    with open('/path/to/your/data/processed/tax_data.json', 'r') as f:
        tax_data = json.load(f)
    
    df = pd.DataFrame(tax_data)
    report_path = '/path/to/your/reports/tax_reports/tax_report.csv'
    df.to_csv(report_path, index=False)
    print(f"Tax report saved to {report_path}")

if __name__ == '__main__':
    generate_tax_report()
