#!/usr/bin/env python

"""Write data to YAML format"""

import sys

from ruamel.yaml import YAML

import source


yaml = YAML()
yaml.dump(source.CUSTOMER_DICT, sys.stdout)
