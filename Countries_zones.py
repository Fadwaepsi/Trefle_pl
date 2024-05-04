import requests

url = "https://trefle.io/api/v1/distributions?range%5Bspecies_count%5D=%2C10&token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)