#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned.
'''
import yaml
import json

from pprint import pprint

def main():
    yaml_file = 'my_file.yml'
    json_file = 'my_file.json'

    with open(yaml_file) as f:
        my_yaml_list = yaml.load(f)

    with open(json_file) as f:
        my_json_list = json.load(f)

    print 'YAML'
    pprint(my_yaml_list)
    print '\n'
    print '-' * 20
    print 'JSON'
    pprint(my_json_list)

if __name__ == "__main__":
    main()
