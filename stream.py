import tweepy
from datetime import datetime
import time

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

    ### Creating a stream listener class
    class MyStreamListener(tweepy.StreamListener):
        counter = 0

        def __init__(self, max_tweets = 1000, *args, **kwargs):
            self.max_tweets = max_tweets
            self.counter = 0
            self.retweets = 0
            self.unique_users = []
            self.t0 = time.time()
            super().__init__(*args, **kwargs)

        def on_connect(self):
            self.counter = 0
            self.start_time = datetime.now()
            print("Starting data scraping at {}.".format(self.start_time))

        def on_status(self, status):
            self.counter += 1
            print(status.user.name + ": " + status.text,"\n")
            if "RT" in status.text:
                self.retweets += 1
            if status.user.name not in self.unique_users:
                self.unique_users.append(status.user.name)
            if self.counter == self.max_tweets:
                print("Number of tweets: {}, including {} retweets ({}%)".format(self.max_tweets, self.retweets, (self.retweets/ self.max_tweets)))
                print("Number of unique users: {}.".format(len(self.unique_users)))
                print("Total time for the program to collect tweets (in seconds): ", time.time() - self.t0)
                return False

        def on_error(self, status_code):
            if status_code == 420:
                #returning False in on_data disconnects the stream
                print("Error code 420. Disconnecting.")
                return False

    myStreamListener = MyStreamListener(max_tweets = max_tweets)
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(track=[keyword])


### If stream.py is ran as a standalone file
if __name__ == "__main__":
    print("ERROR! Run the app.py")
