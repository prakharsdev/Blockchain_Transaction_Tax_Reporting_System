import json
import os

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

# Example usage
if __name__ == '__main__':
    config_path = '/path/to/your/config.json'
    config = load_config(config_path)
    print(config)
