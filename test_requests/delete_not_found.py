import requests

id = -1

url=f"http://127.0.0.1:8000/tasks/{id}"

response = requests.delete(url)
assert(response.status_code == 404)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")