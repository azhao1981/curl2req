# -*- coding: utf-8 -*-
from jsonpath_ng import parse
import glob
import json


def json_get_data(json_data, path):
    expr = parse(path)
    return [match.value for match in expr.find(json_data)]


def json_get(json_data, path):
    data = json_get_data(json_data, path)
    if len(data) == 0:
        return None
    return data[0]


def load_data_from_files(path_pattern, xpath):
    files = glob.glob(path_pattern)
    data = []
    for file in files:
        items_json = json.load(open(file, encoding='utf-8'))
        items = json_get_data(items_json, xpath)
        data.extend(items)
    return data


def to_kv(json_data, key_path):
    try:
        items = {}
        keys = json_get_data(json_data, key_path)
        if keys == "" or len(keys) == 0:
            return {}

        if isinstance(keys, list):
            for key in keys:
                items[key] = json_data
        elif isinstance(keys, str):
            items[keys] = json_data
        return items
    except Exception as e:
        print("args: ", key_path, json_data)
        print("keys: ", keys)
        print("items: ", items)
        raise e
