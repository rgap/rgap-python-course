# Accessing a Nested Dictionary

company = {
    "employee_1": {"name": "Alice", "age": 31, "salary": 70000},
    "employee_2": {"name": "Bob", "age": 28, "salary": 60000},
}

# Accessing nested elements
employee_1_name = company["employee_1"]["name"]
print(f"Employee 1's name: {employee_1_name}")  # Outputs: Employee 1's name: Alice
