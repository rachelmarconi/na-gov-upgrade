import tweepy
import os

client = tweepy.Client(consumer_key =  os.environ['TWEEPY_API_KEY'],
                        consumer_secret = os.environ['TWEEPY_API_SECRET'],
                        access_token = os.environ['TWEEPY_ACCESS_TOKEN'],
                        access_token_secret = os.environ['TWEEPY_ACCESS_TOKEN_SECRET'])

text = "Hello world! This is yet another automated tweet!"

print(text)

response = client.create_tweet( text = text )
print(response)
