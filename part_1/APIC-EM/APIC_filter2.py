import json

data = open.json("APCI2.json")

for item in data["response"]:
    for item1 in item["authorization"]:
        print("User \'%s\', role is the %s."%(item["username"],(item1["role"])[5:]))