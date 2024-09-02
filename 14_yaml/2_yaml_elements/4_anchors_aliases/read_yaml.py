from pprint import pprint

import yaml

# We open the file, read its content, and then use the PyYAML library to parse it.
# PyYAML's `safe_load` function converts the YAML content into a Python dictionary, handling
# anchors (&) and aliases (<<) just as it does when loading from a string.


def load_yaml_from_file(file_path):
    # Function to load YAML content from a file
    with open(file_path, 'r') as file:
        yaml_content = file.read()

    # Parse the YAML content
    return yaml.safe_load(yaml_content)


file_path = 'example.yaml'

config = load_yaml_from_file(file_path)

pprint(config, indent=4, width=60, compact=False)
