import requests

url = "https://trefle.io/api/v1/plants?filter_not[maximum_height_cm]=5,20&token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
