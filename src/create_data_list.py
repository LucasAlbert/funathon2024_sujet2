from yaml import safe_load


def create_data_list(source_file):
    with open(source_file, 'r') as file:
        data = safe_load(file)
    return data
