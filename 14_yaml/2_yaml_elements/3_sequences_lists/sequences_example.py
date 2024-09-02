import yaml

# Theory: Sequences (Lists) in YAML represent ordered collections of items.
# Each item in the list is prefixed with a dash (-).
# Historical Context: YAML's list representation was intended to be easy to read and write,
# maintaining a natural flow similar to reading a text, part of the
# standard since 2001.

# Example data
data = {
    'name': 'Jane Doe',
    'hobbies': ['reading', 'traveling', 'swimming']
}

# Dumping the dictionary to YAML
with open('dump_example.yaml', 'w') as file:
    yaml.dump(data, file)
