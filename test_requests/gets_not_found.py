# Ejecutar con la base de datos vacía

import requests
id = -1
url=f"http://127.0.0.1:8000/tasks"

# GET 
def get():
    response = requests.get(url)
    assert(response.status_code == 404)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")

# GET TASK BY ID
def get_task_by_id():
    response = requests.get(f"{url}/{id}")
    assert(response.status_code == 404)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")

# GET EXPIRED TASKS
def get_expired_tasks():
    response = requests.get(f"{url}/expired")
    assert(response.status_code == 404)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")