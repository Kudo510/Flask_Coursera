# Given an URL API how to get the data from that API - just need request lb
import json
import requests


url = "https://www.fishwatch.gov/api/species"
data = requests.get(url)

## Cos the data is in json file - use json to load that lb
# results = json.loads(data.text)
print("Results: ", data.text)

## More public API: https://github.com/public-apis/public-apis