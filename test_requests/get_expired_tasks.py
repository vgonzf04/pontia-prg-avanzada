# ejecutar después de hacer post.py

import requests

url="http://127.0.0.1:8000/tasks/expired"

def get_expired_tasks():
    response = requests.get(url)
    assert(response.status_code == 200)
    print(f"status_code: {response.status_code}")
    print(f"msg: {response.json()}")