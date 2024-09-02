# 3_importing_third_party_module.py
# Python Version: Third-party modules can be installed and imported using
# `pip`.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print(f"Response Data: {data}")
