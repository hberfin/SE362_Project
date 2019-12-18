import requests

request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = request.json()
print('Baslik: ' + data['title'])
print('This change is made by Anil Celik')
#deneme değişiklik
#cheers
