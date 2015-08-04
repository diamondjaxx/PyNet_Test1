#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
'''
import yaml
import json

def main():
    yaml_file = 'my_file.yml'
    json_file = 'my_file.json'

    my_dict = {'ip_addr': '10.20.100.20', 'platform': 'Cisco UCS'}

    my_list = ['beginning', 6, 7, 3, -24, my_dict, 2.2, 'last']

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style = False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)

if __name__ == "__main__":
    main()
