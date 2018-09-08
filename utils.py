import os
import json

def load_json_file(f):
    with open(os.path.join("data", f), 'r') as file:
        return json.dumps(json.load(file), indent=4)
