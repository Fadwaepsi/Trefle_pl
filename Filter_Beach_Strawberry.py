import requests

url = "https://trefle.io/api/v1/plants?token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs&filter%5Bcommon_name%5D=beach%20strawberry"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
