import json

with open("data.json", "r") as fd:
    data = json.load(fd)

print(data)
