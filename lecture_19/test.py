import requests

# POST
url = "http://127.0.0.1:8080/upload"

payload = {}
files = [
  ('image', ('images.jpg', open('C:/Users/lenov/OneDrive/Desktop/images.jpg', 'rb'), 'image/jpeg'))
]

headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


# GET
url_get = "http://127.0.0.1:8080/image/images.jpg"

payload = {}
headers = {
  'Content-Type': 'image',
  'Accept': 'application/json'
}

response = requests.request("GET", url_get, headers=headers, data=payload)

print(response.text)


# DELETE

url_del = "http://127.0.0.1:8080/delete/images.jpg"

payload = {}
headers = {}

response = requests.request("DELETE", url_del, headers=headers, data=payload)

print("")
print(response.text)