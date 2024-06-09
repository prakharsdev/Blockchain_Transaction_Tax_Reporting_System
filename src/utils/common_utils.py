import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# Example usage
if __name__ == '__main__':
    dir_path = '/path/to/your/directory'
    create_directory(dir_path)

    file_path = os.path.join(dir_path, 'example.txt')
    write_file(file_path, 'Hello, World!')
    content = read_file(file_path)
    print(content)
