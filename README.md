# Integrated Blockchain Data Pipeline for Tax Compliance

This project is designed to streamline the process of analyzing blockchain transactions and generating tax reports, ensuring compliance with tax regulations.

## Features

- **Data Ingestion**: Fetches blockchain transaction data from APIs.
- **Data Processing**: Transforms and cleans data using Apache Beam and Google Cloud Dataflow.
- **Data Storage**: Stores data in Google Cloud Storage, BigQuery, PostgreSQL, and Neo4j.
- **Data Analysis**: Utilizes Pandas, Matplotlib, and Seaborn for analysis and visualization.
- **Tax Calculation**: Implements logic to calculate tax liabilities.
- **Reporting**: Generates comprehensive tax reports.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Cloud SDK
- Neo4j
- PostgreSQL

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/prakharsdev/Blockchain_Transaction_Tax_Reporting_System.git
    cd blockchain-transaction-tax-compliance
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up Google Cloud credentials:
    ```sh
    gcloud auth login
    gcloud config set project your-gcp-project-id
    ```

### Running the Pipeline

1. Navigate to the `data_ingestion/` directory and run the ETL pipeline:
    ```sh
    python dataflow_jobs/etl_pipeline.py
    ```

### Running Tests

1. Run unit tests:
    ```sh
    python -m unittest discover -s tests
    ```

### Generating Reports

1. Generate tax reports:
    ```sh
    python reports/tax_reports/generate_tax_report.py
    ```

2. Create visualizations:
    ```sh
    python reports/visualizations/generate_visualization.py
    ```


![Data Flow (1)](https://github.com/prakharsdev/Blockchain_Transaction_Tax_Reporting_System/assets/26145700/e651a992-53e0-4e74-aff3-f501adf08519)

