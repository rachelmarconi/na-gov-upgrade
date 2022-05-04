import tweepy
import os

c_key = os.environ['TWEEPY_API_KEY']
print("c_key: ",c_key)

c_secret = os.environ['TWEEPY_API_SECRET']
print("c_secret: ",c_secret)

token_key = os.environ['TWEEPY_ACCESS_TOKEN']
print("token_key: ",token_key)

token_secret = os.environ['TWEEPY_ACCESS_TOKEN_SECRET']
print("token_secret: ",token_secret)


client = tweepy.Client(consumer_key =  c_key,
                        consumer_secret = c_secret,
                        access_token = token_key,
                        access_token_secret = token_secret)

text = "Hello world! This is yet another automated tweet!"

print(text)

response = client.create_tweet( text = text )
print(response)
