import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)