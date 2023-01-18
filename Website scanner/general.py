import os

def create_project_dir(directory: str) -> None:
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

def write_file(path: str, data: str) -> None:
    with open(path, 'w') as f:
        f.write(data)
