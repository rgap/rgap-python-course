from pprint import pprint

import yaml


# Function to load YAML content from a file
def load_yaml_from_file(file_path):

    with open(file_path, 'r') as file:
        yaml_content = file.read()

    # Parse the YAML content
    return yaml.safe_load(yaml_content)


# Example usage
file_path = 'example.yaml'  # Replace with your actual file path

# Load the YAML content from the file
config = load_yaml_from_file(file_path)

# Output the loaded configuration
print("YAML content loaded into Python dictionary:")
pprint(config, indent=4, width=80, compact=False)

# Accessing the individual strings
print("\nFolded String:")
print(config['description_folded'])

print("\nLiteral String:")
print(config['description_literal'])

print("\nPoem String:")
print(config['poem'])
