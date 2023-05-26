import tweepy
import os
from dotenv import load_dotenv
import requests

# Load enviroment variables
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Authenticate to Twitter
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
myUserProfile = client.get_me().data
myUserID = myUserProfile['id']
# Create a tweet


# Send a POST request to the HeyAly API
def send_a_chat_message_to_ally(url, message):
    try:
        payload = {"message": message}
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None


# Example usage
api_url = os.getenv("HEY_ALLY_API_URL")
response_data = send_a_chat_message_to_ally(api_url, 'Pretend your name is Aly and your an AI with a personality. Create your first tweet on twitter please.')

if response_data:
    # Process the response data
    response = client.create_tweet(text=str(response_data))
