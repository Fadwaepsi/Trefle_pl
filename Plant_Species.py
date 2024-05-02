import requests

url = "https://trefle.io/api/v1/plants?token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs&page=2"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)