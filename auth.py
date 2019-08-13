import settings
import os
import requests
import json
import time

class MicrosoftAuth:
    """
    Class for managing all the microsoft graph api auth logic
    """

    def __init__(self, session):
        self.s = session
        self.APP_ID = os.getenv("APP_ID")
        self.APP_SECRET = os.getenv("APP_SECRET")
        self.DIRECTORY_ID = os.getenv("DIRECTORY_ID")
        self.expire_time = None
        self.access_token = None

    def get_access_token(self):
        """
        Uses the APP_ID, APP_SECRET, and the DIRECTORY_ID to request a bearer token to access data via application permissions
            -> Note: For this to work you must leave the redirect uri blank and check the box with "https://login.microsoftonline.com/common/oauth2/nativeclient"
        """
        print("Requesting access token from 'https://login.microsoftonline.com/'")
        endpoint = "https://login.microsoftonline.com/"+self.DIRECTORY_ID+"/oauth2/v2.0/token"
        request_params = {
            "grant_type": "client_credentials",
            "client_id": self.APP_ID,
            "client_secret": self.APP_SECRET,
            "scope": "https://graph.microsoft.com/.default"
        };

        r = self.s.post(endpoint, data=request_params)
        response = json.loads(r.text) # load string

        self.expire_time = time.time() + int(response["expires_in"])
        self.access_token = response["access_token"]

        self.store_token()

        return (self.access_token, self.expire_time)

    def load_token(self):
        """
        reads token info from file system
        """
        try:
            with open('client_secrets.json') as json_file:
                data = json.load(json_file)
                return data
        except:
            return False

    def store_token(self):
        """
        Saves token to file system
        """
        data = {
            "expire_time": self.expire_time,
            "access_token": self.access_token
        }
        with open('client_secrets.json', 'w') as outfile:
            json.dump(data, outfile)

    def check_if_token_expired(self, expire_time):
        """
        Checks to see if the token is expired
        """
        # 5 minute offset just in case
        if time.time() > expire_time - 300:
            return True
        else:
            return False
    
    def __getitem__(self, key):
        """
        Use the get time to easily get access token but also check if it needs to be renewed or not
        """
        if key != "access_token":
            return False
        else:
            token_data = self.load_token()
            if not token_data:
                # loading from file failed
                print("loading from file failed")
                self.get_access_token()
                return self.access_token
            else:
                if self.check_if_token_expired(token_data["expire_time"]):
                    print("-token expired-")
                    self.get_access_token()
                else:
                    self.access_token = token_data["access_token"]
                    self.expire_time = token_data["expire_time"]
            return self.access_token