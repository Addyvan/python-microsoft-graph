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

def get_user_type(session, access_token, id):
    """
    Get a user's user type
    """
    endpoint = "https://graph.microsoft.com/v1.0/users/"+id+"/userType"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_many_user_type(session, access_token, ids):
    """
    Retrieve several users' types
    """
    data = {
        "requests":
        [
            {
                "url": "/users/"+id+"/userType",
                "method": "GET",
                "id": i
            }
            for i, id in enumerate(ids)
        ]
    }
    data = json.loads(json.dumps(data))
    endpoint = "https://graph.microsoft.com/v1.0/$batch"
    r = session.post(endpoint, json=data, headers={"Authorization": "Bearer " + access_token, "Content-type": "application/json"})
    responses = json.loads(r.text)['responses']
    out = {}
    for i, response in enumerate(responses):
        
        out[ids[i]] = {
            'userType': response['body']['value']
        }
        
    return out
