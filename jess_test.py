import time
from auth import MicrosoftAuth
from queries.users import *
from queries.groups import *
from queries.reports import *
from queries.teams import *
from queries.sites import *
import pandas as pd
from mutations.users import *
from queries.directory import *

import requests

"""
Ignore this file, just using it as a workspace!
"""

#set up
s = requests.Session()

mauth = MicrosoftAuth(session=s)

access_token = mauth["access_token"]


# try later:              https://docs.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0



external_users_team_id = "e74236f3-7c13-4f86-b128-1c4854aae544" #works as team_id and as site_id
UX_testing_team_id = "a6200cfe-b26a-4b64-abbb-05716ade140f"

external = "e74236f3-7c13-4f86-b128-1c4854aae544"
gox = "b2a099bf-c125-444f-8e91-276ba7e1324a"

site = "949e7a87-68bd-4dfc-a6f1-610d192ae4d3"

x = get_tenant_site(s, access_token)
print (x, end="\n\n")

y = get_team_site(s,access_token, UX_testing_team_id)
print (y, end="\n\n")

z = get_team_subsites(s,access_token, UX_testing_team_id)
#print (z, end="\n\n")

a = get_team_analytics(s,access_token, UX_testing_team_id)
#print (a, end="\n\n")


#team_site = get_team_site(s, access_token, external)

#print(team_site)

#print(get_teams(s, access_token))
#print(get_team_installed_apps(s, access_token, "e74236f3-7c13-4f86-b128-1c4854aae544"))


#if access_token:
#    print(access_token)


#df = get_sharepoint_user_detail(s, access_token)
#df.to_csv("sharepoint_report.csv")


"""
user = create_user(
    session=s,
    access_token=access_token,
    displayName="jkgilchrist",
    mailNickname="jkgilchrist", 
    userPrincipalName="dev.jkg@edw2z.onmicrosoft.com", 
    password="Test123456!"
)

print(user)
"""

#users = get_users(s, access_token)
#y = get_group_ids(s, access_token)
#print (y)

#x = get_group_names(s,access_token)
#print (x)

#z = get_all_groups_and_members(s,access_token)

#a = get_group_member_counts(s, access_token)

#b = get_group_channels(s, access_token, UX_testing_team_id)
#print (b)

#c =  get_group_channel_messages(s, access_token, UX_testing_team_id, "19:104c588e934b428f86b831ce13a6e9db@thread.skype")
#print (c)
"""
users_dict = dict()
for user in users:
    users_dict[user["displayName"]] = {
        "id": user["id"]
    }

df = pd.DataFrame.from_dict(users_dict).transpose()
df.to_csv("users.csv")"""
'''
for id in users_dict.keys():
    if users_dict[id]["displayName"] == "Chris Jaja":
        groups = get_user_groups(s, access_token, id)
        print(groups)
''' 

s.close()
