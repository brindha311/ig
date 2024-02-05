import json

def read_json_file(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    return json_data


def write_dict_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
