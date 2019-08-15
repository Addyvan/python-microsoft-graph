import json

def get_teams(session, access_token):
    """
    Gets teams
    """
    endpoint = "https://graph.microsoft.com/v1.0/teams"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    print(response)
    return response["value"]

def get_team_installed_apps(session, access_token, team_id):
    """
    Retrieves installed apps for a given team
    """
    endpoint = "https://graph.microsoft.com/v1.0/teams/"+team_id+"/installedApps?$expand=teamsAppDefinition"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_team_members(session, access_token, team_id):
    """
    Gets members of a team
    """
    endpoint = "https://graph.microsoft.com/v1.0/groups/"+team_id+"/members?$select=id,displayName"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_team_channels(session, access_token, team_id):
    """
    Gets channels of a team
    """
    endpoint = "https://graph.microsoft.com/v1.0/teams/"+team_id+"/channels"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]