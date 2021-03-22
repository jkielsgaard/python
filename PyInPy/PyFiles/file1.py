import requests

response = requests.get("http://localhost:5001")

fnr = "1"
print("file {} - apicall".format(fnr))
print(response.json())