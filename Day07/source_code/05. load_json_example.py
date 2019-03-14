import json


with open('json_data.json', 'r') as data_file:
    data = json.load(data_file)
    print(data['name'])
    print(data['created'])
