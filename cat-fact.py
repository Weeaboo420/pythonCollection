import json, random
from urllib.request import urlopen
url = "https://cat-fact.herokuapp.com/facts"
response = urlopen(url)
data_raw = json.loads(response.read())

canExit = False
while not canExit:
    data = data_raw["all"][random.randrange(0, len(data_raw["all"]))]
    if len(data.get("text")) > 8:
        print("")
        print("Cat fact of the day:")
        print(data.get("text"))
        print("")
        print(f'Fact by: {data.get("user").get("name").get("first")} {data.get("user").get("name").get("last")}')
        upvotes = int(data.get("upvotes"))
        upvote_msg = "upvotes"
        if upvotes == 1:
            upvote_msg = "upvote"
        print(f'This post has {upvotes} {upvote_msg}')
        print("")
        print("cat-fact.py written by Weeaboo420")
        canExit = True
