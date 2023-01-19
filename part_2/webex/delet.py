from webexteamssdk import WebexTeamsAPI   ### pip install webexteamssdk

current_access_token = "YjgxZmQyZjEtYzQwNy00NDYzLTlhMmUtNDUzMzY3YzlhMTRlZWZlMTU1NjQtZWU0_P0A1_252c1395-1f33-4afe-85cf-58b2de7a3ff4"

api = WebexTeamsAPI(access_token=current_access_token)

# Find all rooms that have 'GROUP_' in their title
all_rooms = api.rooms.list()
demo_rooms = [room for room in all_rooms if 'GROUP' in room.title]


for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)


