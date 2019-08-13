import json

def get_groups(session, access_token):
    endpoint = "https://graph.microsoft.com/v1.0/groups/"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]
