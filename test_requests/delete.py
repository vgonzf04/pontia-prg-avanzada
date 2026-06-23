import requests

id = input("Introduce id de una tarea que exista: ")

url=f"http://127.0.0.1:8000/tasks/{id}"

response = requests.delete(url)
assert(response.status_code == 200)
print(f"status code: {response.status_code}")
print(f"msg: {response.json()}")