import json

def get_group_ids(session, access_token):
    endpoint = "https://graph.microsoft.com/v1.0/groups?$select=id"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]
