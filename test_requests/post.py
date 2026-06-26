import requests

url="http://127.0.0.1:8000/tasks"

task_data1 = {
    "title": "Tarea completa",
    "description": "comprueba post funciona",
    "deadline": "2025-12-12",
    "completed": True
}

task_data3 = {
    "title": "Sin description",
    "deadline": '2027-12-12',
    "completed": False
}

task_data2 = {
    "title": "Sin completed",
    "description": "comprueba default False",
    "deadline": "2027-12-12"
}

def post():
    response = requests.post(url, json=task_data1)
    assert(response.status_code == 201)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")

    response = requests.post(url, json=task_data2)
    assert(response.status_code == 201)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")

    response = requests.post(url, json=task_data3)
    assert(response.status_code == 201)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")