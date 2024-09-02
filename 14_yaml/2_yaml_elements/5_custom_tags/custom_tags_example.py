from datetime import datetime
from pprint import pprint

import yaml

# Theory: Custom Tags in YAML allow the use of application-specific data types, extending the basic set of YAML types.
# Historical Context: Custom tags became important as YAML was adopted in various domains, allowing users to define
# types that best suit their application needs.


# Custom constructor for !datetime tag (handles full datetime)
def datetime_constructor(loader, node):

    value = loader.construct_scalar(node)
    # Convert the datetime string into a datetime object
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")


# Register the custom constructor with PyYAML for the !datetime tag
yaml.add_constructor('!datetime', datetime_constructor)


def load_yaml_from_file(file_path):
    # Function to load YAML content from a file
    with open(file_path, 'r') as file:
        yaml_content = file.read()

    # Parse the YAML content with custom tag handling
    return yaml.load(yaml_content, Loader=yaml.FullLoader)


# Example usage
file_path = 'example.yaml'

# Load the YAML content from the file
config = load_yaml_from_file(file_path)

# Output the loaded configuration using pprint with enhanced formatting
print("YAML content with custom datetime tag as a Python dictionary:")
pprint(config, indent=4, width=80, compact=False)
