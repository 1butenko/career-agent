import json

def read_json(f_name):
    with open(f_name, "r") as f:
        return json.load(f)