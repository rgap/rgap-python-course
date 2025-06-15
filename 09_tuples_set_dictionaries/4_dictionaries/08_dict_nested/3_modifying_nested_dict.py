# Modifying a Nested Dictionary

company = {
    "employee_1": {"name": "Alice", "age": 31, "salary": 70000},
    "employee_2": {"name": "Bob", "age": 28, "salary": 60000},
}

# Modifying a nested dictionary
company["employee_1"]["salary"] = 75000
print(f"Updated company dictionary: {company}")
