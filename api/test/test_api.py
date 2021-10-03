import requests

url = 'http://127.0.0.1:8000/model_v1/predict'
path = 'one.PNG'
image = {'file': open(path, 'rb')}
print(image)
result = requests.post(url, files=image)
print(result.json())