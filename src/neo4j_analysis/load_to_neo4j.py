from neo4j import GraphDatabase
import json

class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_data(self, data):
        with self.driver.session() as session:
            for record in data:
                session.run(
                    """
                    MERGE (t:Transaction {symbol: $symbol})
                    SET t.total_value = $total_value, t.estimated_tax = $estimated_tax
                    """,
                    symbol=record['symbol'],
                    total_value=record['total_value'],
                    estimated_tax=record['estimated_tax'],
                )

if __name__ == '__main__':
    loader = Neo4jLoader('bolt://localhost:7687', 'neo4j', 'your_password')
    with open('/path/to/your/data/processed/tax_data.json', 'r') as f:
        tax_data = json.load(f)
    loader.load_data(tax_data)
    loader.close()
