import json

def get_tenant_site(session, access_token):
    """
    Gets the tenant root site
    """
    endpoint = "https://graph.microsoft.com/v1.0/sites/root"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response

def get_team_site(session, access_token, team_id):
    """
    Gets the tenant root site
    """
    endpoint = "https://graph.microsoft.com/v1.0/groups/{}/sites/root".format(team_id)
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response