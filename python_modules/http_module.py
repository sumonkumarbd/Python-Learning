import http.client
import json

print("\n $$$ HTTP MODULE $$$ \n")

url = "dummyjson.com"
conn = http.client.HTTPSConnection(url)
conn.request("GET", "/products")

respons = conn.getresponse()
content = respons.read().decode("utf-8")  # Decode from bytes to string

# Convert JSON string to Python dictionary
contentDict = json.loads(content)

# Convert Python dictionary to formatted JSON string
contentFormatted = json.dumps(contentDict, indent=4)

print(contentFormatted)
