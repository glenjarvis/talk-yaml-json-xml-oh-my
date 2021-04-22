#!/usr/bin/env python

"""Make source files from original data

Data can drift. If a change is needed, let's not make that chane in every file
of every format. That's a recipe for a mistake and confusion.

Instead, these files are generated dynamically (and still committed to the code
repo so they are ready for beginners to review).
"""

import json

import jsbeautifier
from ruamel.yaml import YAML

import source


def write_json_source():
    """Write ./source.json"""

    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    with open("./source.json", "w") as json_f:
        json_f.write(
            jsbeautifier.beautify(
                json.dumps(source.CUSTOMER_DICT), opts))


def write_yaml_source():
    """Write ./source.yaml"""
    yaml = YAML()
    yaml.default_flow_style = False
    with open("./source.yaml", "w") as yaml_f:
        yaml.dump(source.CUSTOMER_DICT, yaml_f)


write_json_source()
write_yaml_source()
