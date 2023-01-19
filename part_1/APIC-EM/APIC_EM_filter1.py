import json

response_json = open("APIC1.json")

print ("ticket: ",response_json["response"]["serviceTicket"])