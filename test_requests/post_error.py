# Ejecutar después de ejecutar post.py para que la tarea con el mismo título ya esté creada

import requests 

url ="http://127.0.0.1:8000/tasks"

task_data = {
    "title": "Sin description",
    "description": "Comprueba error tarea mismo title",
    "deadline": '2030-12-12',
    "completed": True
}

def post_error():
    response = requests.post(url, json=task_data)
    assert(response.status_code == 400)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")