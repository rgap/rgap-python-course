import yaml

# Theory: Mappings (Dictionaries) in YAML represent key-value pairs, where each key is unique within its mapping.
# Historical Context: YAML was first proposed in 2001 as a human-readable data serialization standard,
# and mappings have always been a core feature to represent structured data.

# Example data
data = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Maple St.',
        'city': 'Wonderland',
        'zip': 12345
    }
}

# Dumping the dictionary to YAML
with open('dump_example.yaml', 'w') as file:
    yaml.dump(data, file)
