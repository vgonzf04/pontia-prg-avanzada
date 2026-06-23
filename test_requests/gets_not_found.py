# Ejecutar con la base de datos vacía

import requests

url=f"http://127.0.0.1:8000/tasks"

# GET 
response = requests.get(url)
assert(response.status_code == 404)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")

# GET TASK BY ID
id = -1
response = requests.get(f"{url}/{id}")
assert(response.status_code == 404)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")

# GET EXPIRED TASKS
response = requests.get(f"{url}/expired")
assert(response.status_code == 404)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")