import json

def assign_user_to_team(session, access_token, user_id, team_id):
    """
    Links a user to a team
    """
    data = {
        "@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/{}".format(user_id)
    }
    data = json.loads(json.dumps(data))
    endpoint = "https://graph.microsoft.com/v1.0/groups/{}/members/$ref".format(team_id)
    r = session.post(endpoint, json=data, headers={"Authorization": "Bearer " + access_token, "Content-type": "application/json"})
    print(r.text)
    return r.text
