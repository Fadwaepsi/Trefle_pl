import requests

url = "https://trefle.io/api/v1/species?filter%5Bflower_color%5D=red&token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)