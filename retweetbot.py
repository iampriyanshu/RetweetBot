#importing tweepy,time and credentials
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

    for tweet in tweepy.Cursor(api.search,q=query,lang='en').items(counter):
        try:
            print('Tweet by: @' + tweet.user.screen_name + ' on topic : '+ query)

            #Retweet the tweets
            tweet.retweet()
            print('Tweet RTed')

            #To cause a delay between RTs
            sleep(60)

        except tweepy.TweepError as e:
            print(e.reason + ' on topic : '+ query)
      
        except StopIteration:
            break
