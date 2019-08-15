import json

def get_directories(session, access_token):
    """
    Gets a complete list of users for a given tenant
    """
    endpoint = "https://graph.microsoft.com/v1.0/directoryRoles"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]
