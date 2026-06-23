# Ejecutar después de ejecutar post.py para que la tarea con id:1 sea completed = True

import requests

id = 1

url = f"http://127.0.0.1:8000/tasks/{id}"

response = requests.put(url)
assert(response.status_code == 404)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")