import requests

id = input("Introduce un id: ")

url = f"http://127.0.0.1:8000/tasks/{id}"

response = requests.put(url)
assert(response.status_code == 200)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")