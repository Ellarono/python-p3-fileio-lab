def write_file(file_name, content):
    if not str(file_name).endswith('.txt'):
        file_name = f"{file_name}.txt"
    with open(file_name, 'w') as f:
        f.write(content)


def append_file(file_name, content):
    if not str(file_name).endswith('.txt'):
        file_name = f"{file_name}.txt"
    with open(file_name, 'a') as f:
        f.write(content)

def read_file(file_name):
    if not str(file_name).endswith('.txt'):
        file_name = f"{file_name}.txt"
    with open(file_name, 'r') as f:
        return f.read()
