import requests

url = "http://127.0.0.1:8080"
endpoint = "/classify"
image = open("plastic.PNG", "rb")
response = requests.post(url=url+endpoint, files={"image": image})
print(response.json())