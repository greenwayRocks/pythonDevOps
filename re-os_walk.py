def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f'Checking: {parent_path}')
        for file in files:
            file_path = os.path.join(parent_path, file)
            last_access = os.path.getatime(file)
            size = os.path.getsize(file)
            print(f'File: {file}')
            print(f'\tlast accessed: {last_access}')
            print(f'size: {size}')
