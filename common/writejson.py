import json

def write_json(new_data, folder, filename='results.json'):
    where = folder + '/' + filename
    with open(where, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)