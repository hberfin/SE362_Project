import requests

request = requests.get('http://10.100.8.9:8000/a.html')
data = request.json()
print('Title: ' + str(data['menu']['popup']['menuitem'][0]['value']))
