import json

def get_users(session, access_token, request_params={}):
    """
    Gets a complete list of users for a given tenant
    """
    endpoint = "https://graph.microsoft.com/v1.0/users"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_user_groups(session, access_token, id):
    """
    Not working yet
    """
    endpoint = "https://graph.microsoft.com/v1.0/users/"+id+"/getMemberGroups"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    print(response)
    return response["value"]