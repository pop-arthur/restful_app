import requests
from pprint import pprint

data = requests.get("http://127.0.0.1:5000/api/news").json()
pprint(data)

data = requests.get("http://127.0.0.1:5000/api/news/asdasd").json()
pprint(data)

json_data = {
    "title": "Веселая новость",
    "content": "Ха-ха",
    "user_id": 1,
    "is_private": True
}

# response = requests.post("http://127.0.0.1:5000/api/news", json=json_data)
# pprint(response.json())

# response_delete = requests.delete("http://127.0.0.1:5000/api/news/10")
# pprint(response_delete.json())

response_put = requests.put("http://127.0.0.1:5000/api/news/1", json={"title": "Новость Ха-Ха", "key": "123"})
print(response_put.json())