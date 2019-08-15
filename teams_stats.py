import requests
from auth import MicrosoftAuth
from queries.users import *
from queries.groups import *
from queries.teams import *
from queries.sites import *
import pandas as pd


"""
Working file to play around with getting team stats
"""

s = requests.Session()

mauth = MicrosoftAuth(session=s)

access_token = mauth["access_token"]

external = "e74236f3-7c13-4f86-b128-1c4854aae544"
gox = "b2a099bf-c125-444f-8e91-276ba7e1324a"

def get_team_stats():
    members = get_team_members(s, access_token, external)
    member_ids = [member["id"] for member in members]
    channels = get_team_channels(s, access_token, external)
    return channels
    

if __name__ == "__main__":
    team_stats = get_team_stats()
    print(team_stats)