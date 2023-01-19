
current_access_token = "MzkwMGI2NmItNDkxMS00NjMwLWJmMDMtODM4YzMyNTAxMmY1MmE0NmJlZWQtNDQy_P0A1_252c1395-1f33-4afe-85cf-58b2de7a3ff4"

### ADD NEW SPACES AND MEMBERS TO WEBEX TEAMS
### THIS CODE ONLY WORKS IF YOU ARE ABLE TO GENERATE A CORRECT GROUPS_STRUC

import requests
import json

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token = current_access_token)


print("Creating spaces +  members --> from Excel spreadsheet in the previous cell")
access_token = current_access_token 

f = open("webex_data.json")
data = json.load(f)
create_group_name = data["groups"]
groepnaam = create_group_name["group_name"]

print(groepnaam)
