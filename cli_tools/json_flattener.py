#!/usr/bin/env python

import json
import sys

# Enable imports without requiring users to set PYTHONPATH
sys.path.append('..')

from src import json_utils


if __name__ == '__main__':

    json_string = sys.stdin.read()
    json_obj = json.loads(json_string)
    flattened_json = json_utils.flatten(json_obj)
    print(json.dumps(flattened_json))
