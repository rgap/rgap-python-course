import yaml

# Scalars in YAML represent single values such as:

# - strings
# - numbers
# - booleans
# - null

# Historical Context: YAML's support for scalar types was designed to provide a clear and concise way
# to represent basic data types. Introduced in the initial version in 2001.

# Example data
data = {
    'key': 'value',
    'age': 30,
    'married': True,
    'children': None
}

# Dumping the dictionary to YAML
with open('dump_example.yaml', 'w') as file:
    yaml.dump(data, file)
