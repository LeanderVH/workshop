import json

#data = open("response.json")

with open('response.json') as f:
   data = json.load(f)

#print(data)

dev_list = []   #create empty list
# loop through results and filter needed information
# create new JSON structure

for device in data['response']:

    if device['type'] != None:

        dev_dict = {} #create empty dict
        dev_dict['hostname'] = device['hostname']
        dev_dict['type'] = device['type']
        dev_dict['macAddress'] = device['macAddress']
        dev_dict['managementIpAddress'] = device['managementIpAddress']
        dev_dict['serialNumber'] = device['serialNumber']
        dev_dict['softwareType'] = device['softwareType']
        dev_dict['softwareVersion'] = device['softwareVersion']
        dev_dict['reachabilityStatus'] = device['reachabilityStatus']
        dev_list.append(dev_dict)

print(dev_list)