import json

def create_user(session, access_token, displayName, mailNickname, userPrincipalName, password):
    """
    Creates a user within the current authenticated tenant
    """
    print("creatign user")
    data = {
        "accountEnabled": True,
        "city": "Ottawa",
        "country": "Canada",
        "department": "Data Team",
        "displayName": displayName,
        "givenName": displayName,
        "jobTitle": "Data Scientist",
        "mailNickname": mailNickname,
        "passwordPolicies": "DisablePasswordExpiration",
        "userPrincipalName": userPrincipalName,
        "passwordProfile": {
            "password": password,
            "forceChangePasswordNextSignIn": True
        }
    }
    data = json.loads(json.dumps(data))
    endpoint = "https://graph.microsoft.com/v1.0/users"
    r = session.post(endpoint, json=data, headers={"Authorization": "Bearer " + access_token, "Content-type": "application/json"})
    response = json.loads(r.text)
    return response