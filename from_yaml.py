#!/usr/bin/env python

"""Read data from YAML file"""

import pprint

from ruamel.yaml import YAML

yaml = YAML(typ='safe', pure=True)

with open("./source.yaml", "r") as source_file:
    loaded_data = yaml.load(source_file)

print("Converted from YAML")
print("===================")
print("Type of data: {}".format(type(loaded_data)))
print("\n")
print("Contents")
print("--------")
pprint.pprint(loaded_data)

print("\n")
print("Still treat it like normal")
print("==========================")
print("Congratulations, {}!!!".format(loaded_data['First Name']))
print("You have just received an all-expense paid vacation ")
print("to Tahiti. It's a magical place...")

print("\n")
print("Want it as a built-in Dictionary?")
data = dict(loaded_data)
print("==============")
print("Type of data: {}".format(type(data)))
print("\n")
print("Contents")
print("--------")
pprint.pprint(data)
print("\n")
