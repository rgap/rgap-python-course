# Inverting a Dictionary (Keys Become Values and Values Become Keys)

original_dict = {"name": "Alice", "profession": "Engineer"}

# Inverting the dictionary
inverted_dict = {v: k for k, v in original_dict.items()}
# Outputs: Inverted dictionary: {'Alice': 'name', 'Engineer': 'profession'}
print(f"Inverted dictionary: {inverted_dict}")
