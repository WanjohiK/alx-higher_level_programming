#!/usr/bin/python3
"""
6-load_from_json_file Module
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as file:
        created_object = json.load(file)
        return created_object
