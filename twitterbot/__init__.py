import tweepy
import os
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)
print(api.get_user(), '\n', '-------------------')


# Create a tweet
# api.update_status("Hello Tweepy")