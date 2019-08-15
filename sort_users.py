import time
from auth import MicrosoftAuth
from queries.users import *
from queries.directory import *
from mutations.team import *
import pandas as pd
import requests

"""
This file is used to sort pre-poc users into directory roles

A bit janky, but it works :)
"""

s = requests.Session()

mauth = MicrosoftAuth(session=s)

access_token = mauth["access_token"]

def create_users_table():
    """
    query and generate a pandas dataframe of tenant users
    """
    print("Generating users table")
    users = get_users(s, access_token)

    users_dict = dict()
    for user in users:
        users_dict[user["displayName"]] = {
            "id": user["id"]
        }

    df = pd.DataFrame.from_dict(users_dict).transpose()
    df.to_csv("./data/users.csv")

def filter_id_list(users_df, ids):
    """
    Removes mgmt and dev accounts from the ids to gather
    """
    dev_accounts = ["Admin", "dev.addison", "dev.jkgilchrist"]
    mgmt_accounts = ["Chris Jaja", "Owen Teo", "Vikesh Srivastava", "Robert Allan"]
    df = users_df
    filtered_ids = []
    for i, name in enumerate(df["name"]):
        id = df["id"][i]
        inPrePoc = True
        for bad_name in dev_accounts+mgmt_accounts:
            if id == df.set_index("name").loc[bad_name]["id"]:
                #print("(", bad_name, " - ", id, " == ", df.set_index("name").loc[bad_name]["id"], ")")
                inPrePoc = False
        if inPrePoc:
            filtered_ids.append(id)
    return filtered_ids

def assign_goc_role(id):
    group_id = "b2a099bf-c125-444f-8e91-276ba7e1324a"
    assign_user_to_team(s, access_token, id, group_id)

def assign_external_role(id):
    group_id = "e74236f3-7c13-4f86-b128-1c4854aae544"
    assign_user_to_team(s, access_token, id, group_id)

if __name__ == "__main__":
    try:
        df = pd.read_csv("./data/users.csv")
    except:
        create_users_table()
        df = pd.read_csv("./data/users.csv")
    df.columns = ["name", "id"]

    ids = []
    for i, id in enumerate(df["id"]):
        ids.append(id)
    pre_poc_ids = filter_id_list(df, ids)
    names = []
    for id in pre_poc_ids:
        names.append(df.set_index("id").loc[id]["name"])

    for i, id in enumerate(pre_poc_ids):
        user_type = get_user_type(s, access_token, id)
        if user_type == 'Member':
            print("linking {} to goc".format(names[i]))
            #assign_goc_role(id)
        else:
            print("linking {} to external".format(names[i]))
            assign_external_role(id)
