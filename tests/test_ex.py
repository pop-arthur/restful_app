import datetime

import requests
from pprint import pprint

json_data = {}

# no json_data
response = requests.post("http://127.0.0.1:5000/api/v2/users", json=json_data)
pprint(response.json())

data = requests.get("http://127.0.0.1:5000/api/v2/users/0").json()
pprint(data)

data = requests.delete("http://127.0.0.1:5000/api/v2/users/1").json()
pprint(data)
