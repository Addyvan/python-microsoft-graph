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

s = requests.Session()

mauth = MicrosoftAuth(session=s)

access_token = mauth["access_token"]

team_site = get_team_site(s, access_token, "e74236f3-7c13-4f86-b128-1c4854aae544")

print(team_site)

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
"""
users = get_users(s, access_token)

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
