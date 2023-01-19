
current_access_token = "MzkwMGI2NmItNDkxMS00NjMwLWJmMDMtODM4YzMyNTAxMmY1MmE0NmJlZWQtNDQy_P0A1_252c1395-1f33-4afe-85cf-58b2de7a3ff4"

### ADD NEW SPACES AND MEMBERS TO WEBEX TEAMS
### THIS CODE ONLY WORKS IF YOU ARE ABLE TO GENERATE A CORRECT GROUPS_STRUC

import requests
import json

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token = current_access_token)

print("Creating spaces +  members --> from Excel spreadsheet in the previous cell")
access_token = current_access_token 

def main(): # using rest api
    ##json inladen
    f = open("webex_data.json")
    groups_struc = json.load(f)
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        print("Creating ... " + create_group_name)
        payload_space={"title": create_group_name}
        if payload_space["title"] != None:  ### avoid errors if room title is unknown
            res_space = requests.post(url, headers=headers, json=payload_space)
            if res_space.status_code < 300: ### only create members if space has been created
                NEW_SPACE_ID = res_space.json()["id"]
                for mbr in rec["group"]["members"]:
                    room_id = NEW_SPACE_ID
                    person_email = mbr["email"] 
                    url2 = 'https://api.ciscospark.com/v1/memberships'
                    payload_member = {'roomId': room_id, 'personEmail': person_email}
                    res_member = requests.post(url2, headers=headers, json=payload_member)

if __name__ == '__main__':
    main()