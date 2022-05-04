import tweepy
import os

#Add your credentials here
twitter_keys = {
        'consumer_key':         os.environ['TWEEPY_API_KEY'],
        'consumer_secret':      os.environ['TWEEPY_API_SECRET'],
        'access_token_key':     os.environ['TWEEPY_ACCESS_TOKEN'],
        'access_token_secret':  os.environ['TWEEPY_ACCESS_TOKEN_SECRET']
        

    }

client = tweepy.Client(consumer_key = twitter_keys['consumer_key'],
                        consumer_secret = twitter_keys['consumer_secret'],
                        access_token = twitter_keys['access_token_key'],
                        access_token_secret = twitter_keys['access_token_secret'])

text = "Hello world! This is another automated tweet!"

print(text)

response = client.create_tweet( text = text )
print(response)
