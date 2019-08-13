import time
from auth import MicrosoftAuth
from queries.users import *
from queries.groups import *
from queries.reports import *

import requests


s = requests.Session()

mauth = MicrosoftAuth(session=s)

access_token = mauth["access_token"]

#if access_token:
#    print(access_token)

#df = get_sharepoint_user_detail(s, access_token)
#df.to_csv("sharepoint_report.csv")


users = get_users(s, access_token)

users_dict = dict()
for user in users:
    users_dict[user["id"]] = {
        "displayName": user["displayName"]
    }

print(users_dict)
'''
for id in users_dict.keys():
    if users_dict[id]["displayName"] == "Chris Jaja":
        groups = get_user_groups(s, access_token, id)
        print(groups)
''' 

s.close()
