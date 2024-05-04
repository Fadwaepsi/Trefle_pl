import requests

url = "https://trefle.io/api/v1/plants?filter_not%5Bedible_part%5D=null&token=u6eaoskjnupYOMtNXHXNJbi_5uUb1D9boacy8Rx4rrs"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)