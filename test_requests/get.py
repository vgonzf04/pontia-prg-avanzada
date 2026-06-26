import requests

url = "http://127.0.0.1:8000/tasks"

def get():
    response = requests.get(url)
    assert(response.status_code == 200)
    print(f"status code: {response.status_code}")
    print(f"msg: {response.json()}")

