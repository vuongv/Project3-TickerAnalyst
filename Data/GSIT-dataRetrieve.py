import requests
import pandas as pd
import json
from pandas import json_normalize

headers = {'Accept' : 'application/json'}

url = "https://api.polygon.io/v2/aggs/ticker/GSIT/range/1/day/2023-01-14/2023-06-14?adjusted=true&sort=asc&limit=120&apiKey=9bXMMaA5omIp2hcgICjUGZFsDK2yU3lL"

r = requests.get(url, headers=headers)
data = r.json() 

save_file = open ("GSIT.json", "w")
json.dump(data, save_file, indent=6)
save_file.close()







