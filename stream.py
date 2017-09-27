import tweepy
from datetime import datetime
import time
from StreamClass import MyStreamListener
def getTweets(keyword, max_tweets):

    ### Setting variables by opening a textfile with relevant passages
    with open("tweetapi.txt") as f:
        access_file = f.read().splitlines()
    consumer_key = access_file[0]
    consumer_secret = access_file[1]
    access_token = access_file[2]
    access_token_secret = access_file[3]

    ### Creating a connection and authenticating
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    ### Create a MyStreamListener object

    myStreamListener = MyStreamListener(max_tweets = max_tweets)
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(track=[keyword])


### If stream.py is ran as a standalone file
if __name__ == "__main__":
    print("ERROR! Run the app.py")
