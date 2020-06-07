def find_rc(rc='.examplerc'):

    # Check for Env variable
    var = 'EXAMPLERC_DIR'
    if var in os.environ:
        var_path = os.path.join(f'{var}', rc)
        config_path = os.path.expandvars(var_path)
        print(f'Checking {config_path}')

        if os.path.exists(config_path):
            return config_path

    # Check the current working directory
    config_path = os.path.join(os.getcwd(), rc)
    print(f'Checking {config_path}')
    if os.path.exists(config_path):
        return config_path

    # Check user home directory
    home_dir = os.path.expanduser('~/')
    config_path = os.path.join(home_dir, rc)
    print(f'Checking {config_path}')
    if os.path.exists(config_path):
        return config_path

    #Check Directory of This file
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc)
    print(f'Checking {config_path}')
    if os.path.exists(config_path):
        return config_path

    print(f'File {rc} has not been found')
