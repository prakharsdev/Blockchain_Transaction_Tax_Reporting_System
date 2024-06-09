import requests
import json

class BlockchainAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_tickers(self):
        endpoint = f'{self.base_url}/v3/exchange/tickers'
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Example usage:
if __name__ == '__main__':
    client = BlockchainAPIClient('https://api.blockchain.com')
    tickers = client.fetch_tickers()
    with open('/path/to/your/data/raw/blockchain_data.json', 'w') as f:
        json.dump(tickers, f)
