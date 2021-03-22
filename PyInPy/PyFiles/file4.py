import requests

response = requests.get("http://localhost:5001")

fnr = "4"
print("file {} - apicall".format(fnr))
print(response.json())