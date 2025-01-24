import requests
from dotenv import load_dotenv
import tweepy
import os

load_dotenv()

api_key=os.getenv("API_KEY")
api_secret_key=os.getenv("API_SECRET_KEY")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
bearer_token=os.getenv("BEARER_TOKEN")
def  xauth():
    # Authenticate
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Verify authentication
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication:", e)

def getposts():

    url = "https://api.x.com/2/tweets/search/recent"

    querystring = {"query":"ai agents"}


    headers = {"Authorization": bearer_token}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
    except Exception as e:
        print("there is a error ",e)    
        

xauth()
getposts()