import requests

request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = request.json()
print('Baslik: ' + data['title'])
#deneme değişiklik