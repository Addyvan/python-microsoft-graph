import json

def get_group_ids(session, access_token):
    endpoint = "https://graph.microsoft.com/v1.0/groups?$select=id"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_group_names(session, access_token):
    endpoint = "https://graph.microsoft.com/v1.0/groups?$select=displayName"
    r = session.get(endpoint, headers = {'Authorization': "Bearer " + access_token})
    response = json.loads(r.text)
    lst = []
    for y in response["value"]:
        lst.append (y["displayName"])

    return lst

def get_group_members(session, access_token, id):
    endpoint = "https://graph.microsoft.com/v1.0/groups/{}/members?$select=displayName".format(id)
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_all_groups_and_members(session, access_token):
    get_ids = get_group_ids(session, access_token)
    get_names = get_group_names(session, access_token)

    ans = []

    for x in range(len(get_names)):
        id = get_ids[x]["id"]
        members = get_group_members(session, access_token, id)
        ans.append( {"group_name": get_names[x], "members": members} )
    return ans

def get_group_member_counts(session, access_token):
    get_ids = get_group_ids(session, access_token)
    get_names = get_group_names(session, access_token)

    ans = []

    for x in range(len(get_names)):
        id = get_ids[x]["id"]
        members = get_group_members(session, access_token, id)
        ans.append( {"group_name": get_names[x], "member_count": len(members)} )

    print (ans)
    return ans

def get_group_channels (session, access_token, id):
    endpoint = "https://graph.microsoft.com/v1.0/groups/{}/team/channels?$select=id,displayName".format(id)
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response["value"]

def get_group_channel_messages (session, access_token, group_id, channel_id):
    endpoint = "https://graph.microsoft.com/beta/teams/{}/channels/".format(group_id) #+ channel_id + "/messages"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    response = json.loads(r.text)
    return response
