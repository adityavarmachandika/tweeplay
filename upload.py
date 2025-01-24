import requests
from dotenv import load_dotenv
import tweepy
import os
from requests_oauthlib import OAuth1

load_dotenv()

api_key=os.getenv("API_KEY")
api_secret_key=os.getenv("API_SECRET_KEY")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
bearer_token=os.getenv("BEARER_TOKEN")


def putpost():

    auth=OAuth1(api_key,api_secret_key,access_token,access_token_secret)

    url="https://api.x.com/2/tweets"
    payload={
        "text":"Hello world!! first tweet from the twitter api :)"
    }
    headers={
        "Content-Type": "application/json"
    }

    try:
        response=requests.post(url,json=payload,headers=headers,auth=auth)
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print("there is a error",e)

putpost()                
