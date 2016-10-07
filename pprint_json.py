import json

def load_data(filepath):
    with open(filepath, 'r') as json_file:
        json_list = json.load(json_file)
    return json_list

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))

if __name__ == '__main__':
    json_file_path = input("Enter the path to the file: ")
    pretty_print_json(load_data(json_file_path))
