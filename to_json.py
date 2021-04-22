#!/usr/bin/env python

"""Write data to JSON format"""

import json

import source

print("The data in JSON format")
print("=======================")
json_data = json.dumps(source.CUSTOMER_DICT)
print("Type of data: {}".format(type(json_data)))
print("\n")
print("Contents")
print("--------")
print(json_data)
