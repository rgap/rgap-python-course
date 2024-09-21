# This will run after installing: pip install pyyaml

import yaml

# Load a basic YAML file
with open('examples/basic_yaml.yaml', 'r') as file:
    data = yaml.safe_load(file)

print("Loaded YAML data:")
print(data)

# Accessing data from the YAML structure
print("\nName:", data['name'])
print("Age:", data['age'])
print("Languages:", data['languages'])
