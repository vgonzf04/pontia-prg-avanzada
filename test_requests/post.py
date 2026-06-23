import requests

url="http://127.0.0.1:8000/tasks"

task_data = {
    "title": "Tarea completa",
    "description": "comprueba post funciona",
    "deadline": "2029-12-12",
    "completed": True
}

response = requests.post(url, json=task_data)
assert(response.status_code == 201)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")

task_data = {
    "title": "Sin completed",
    "description": "comprueba default False",
    "deadline": "2027-12-12"
}

response = requests.post(url, json=task_data)
assert(response.status_code == 201)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")

task_data = {
    "title": "Sin description",
    "deadline": '2027-12-12',
    "completed": False
}

response = requests.post(url, json=task_data)
assert(response.status_code == 201)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")