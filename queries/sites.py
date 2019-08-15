import json

def get_tenant_site(session, access_token):
    """
    Gets the tenant root site
    """
    endpoint = "https://graph.microsoft.com/v1.0/sites/root"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response

def get_team_site(session, access_token, id):
    """
    Gets given site's root
    """
    endpoint = "https://graph.microsoft.com/v1.0/groups/{}/sites/pages".format(id)
    #endpoint = "https://graph.microsoft.com/v1.0/sites/edw2z.sharepoint.com:/sites/UXTesting/SitePages/Now-everyone-can-create-a-website-with-some-struggle.aspx"

    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response

def get_team_subsites(session, access_token, site_id): #Not returning anything
    """
    Gets the tenant root site
    """
    endpoint = "https://graph.microsoft.com/v1.0/sites/{}/sites".format(site_id)
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    #print (response)
    return response

def get_team_analytics(session, access_token, site_id):
    """
    Gets the tenant root site
    """
    endpoint = "https://graph.microsoft.com/v1.0/sites/{}/analytics".format(site_id)
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    #print (response)
    return response