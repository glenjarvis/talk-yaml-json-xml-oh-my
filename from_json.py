#!/usr/bin/env python

"""Read data from JSON file"""


import pprint

import json

with open("./source.json", "r") as json_f:
    data = json_f.read()

print("Data from file")
print("==============")
print("Type of data: {}".format(type(data)))
print("\n")
print("Contents")
print("--------")
print(data)
print("\n")

print("Converted from JSON")
print("===================")
loaded_data = json.loads(data)
print("Type of data: {}".format(type(loaded_data)))
print("\n")
print("Contents")
print("--------")
pprint.pprint(loaded_data, sort_dicts=False)

print("\n")
print("Now, it is data like normal")
print("===========================")
print("Congratulations, {}!!!".format(loaded_data['First Name']))
print("You have just received an all-expense paid vacation ")
print("to Tahiti. It's a magical place...")
