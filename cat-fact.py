import json, random
from urllib.request import urlopen
url = "https://cat-fact.herokuapp.com/facts"
response = urlopen(url)
data_raw = json.loads(response.read())

data = data_raw["all"][random.randrange(0, len(data_raw["all"]))]
print(data.get("text"))

