import requests

id = 2

url = f"http://127.0.0.1:8000/tasks/{id}"

def put():
    response = requests.put(url)
    assert(response.status_code == 200)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")