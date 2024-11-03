import os
import json


def load_config(file_path):
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(full_path, 'r') as file:
        return json.load(file)