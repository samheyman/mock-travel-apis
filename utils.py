import os
import json

def load_json_file(f):
    with open(os.path.join("data", f), 'r') as file:
        return json.load(file)

def save_json_file(data, f):
    with open(os.path.join("data", f), 'w') as file:
        json.dump(data, file)
