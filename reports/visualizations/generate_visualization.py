import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_visualization():
    df = pd.read_csv('/path/to/your/reports/tax_reports/tax_report.csv')

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='symbol', y='estimated_tax')
    plt.title('Estimated Tax by Symbol')
    plt.xlabel('Symbol')
    plt.ylabel('Estimated Tax')

    visualization_path = '/path/to/your/reports/visualizations/estimated_tax_by_symbol.png'
    plt.savefig(visualization_path)
    print(f"Visualization saved to {visualization_path}")

if __name__ == '__main__':
    generate_visualization()
