def calculate_tax_for_transaction(volume, price):
    tax_rate = 0.15
    return volume * price * tax_rate

# Example usage
if __name__ == '__main__':
    volume = 1000
    price = 50
    tax = calculate_tax_for_transaction(volume, price)
    print(f'Tax: ${tax}')
