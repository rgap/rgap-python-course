# Accessing a Key with get() Method

person = {"name": "Alice", "age": 30}

# 1. Accessing an Existing Key
age = person.get("age")
print(f"Age: {age}")  # Outputs: Age: 30

# 2. Accessing a Non-Existing Key with Default Value
salary = person.get("salary", "Not specified")
print(f"Salary: {salary}")  # Outputs: Salary: Not specified

# 3. Accessing a Non-Existing Key Without a Default Value
gender = person.get("gender")
print(f"Gender: {gender}")  # Outputs: Gender: None

# 4. Accessing a Key in a Nested Dictionary with Default Value
person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "city": "Wonderland",
        "zip": "12345"
    }
}
zip_code = person.get("address", {}).get("zip", "ZIP not found")
print(f"ZIP Code: {zip_code}")  # Outputs: ZIP Code: 12345

# 5. Handling Missing Nested Dictionary
country = person.get("address", {}).get("country", "Country not specified")
print(f"Country: {country}")  # Outputs: Country: Country not specified
