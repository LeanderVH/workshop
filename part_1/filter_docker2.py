import json
with open("output2_docker.json") as f:
   data = json.load(f)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict2 = data
print(docker_dict2[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e...bd52826d786db9a3be2811"]["IPv4Address"])