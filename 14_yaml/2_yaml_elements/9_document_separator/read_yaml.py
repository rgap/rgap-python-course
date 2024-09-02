from pprint import pprint

import yaml


# Function to load YAML content from a file
def load_yaml_from_file(file_path):

    with open(file_path, 'r') as file:
        # Load all YAML documents from the file
        documents = yaml.safe_load_all(file)
        return list(documents)  # Convert the generator to a list


# Example usage
file_path = 'config.yaml'

# Load the YAML content from the file
yaml_documents = load_yaml_from_file(file_path)

# Output each loaded document
print("YAML documents loaded into Python objects:")
for i, doc in enumerate(yaml_documents, 1):
    print(f"\nDocument {i}:")
    pprint(doc, indent=4, width=80, compact=False)
