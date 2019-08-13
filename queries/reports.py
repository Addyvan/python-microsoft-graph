import json
import pandas as pd

def get_teams_user_detail(session, access_token, period_value="D7"):
    """
    Gets a complete list of users for a given tenant
    Returns a pandas DataFrame
    """
    #endpoint = "https://graph.microsoft.com/v1.0/reports/getTeamsUserActivityUserDetail(date=2019-08-09)"
    endpoint = "https://graph.microsoft.com/v1.0/reports/getTeamsUserActivityUserDetail(period='D30')"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    df = pd.DataFrame([x.split(',') for x in r.text.split('\n')])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    df = df[:-1] # chop off last line
    return df

def get_sharepoint_user_detail(session, access_token, period_value="D7"):
    """
    Gets a complete list of users for a given tenant
    Returns a pandas DataFrame
    """
    endpoint = "https://graph.microsoft.com/v1.0/reports/getSharePointActivityUserDetail(period='D30')"
    r = session.get(endpoint, headers={"Authorization": "Bearer " + access_token})
    df = pd.DataFrame([x.split(',') for x in r.text.split('\n')])
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    df = df[:-1] # chop off last line
    return df