import tweepy
from datetime import datetime
import time


class MyStreamListener(tweepy.StreamListener):

    ### Initialize the class
    def __init__(self, max_tweets = 1000, *args, **kwargs):
        self.max_tweets = max_tweets
        self.counter = 0
        self.retweets = 0
        self.unique_users = []
        self.t0 = time.time()
        super().__init__(*args, **kwargs)

    ### Function describes the behaviour when the connection is established
    def on_connect(self):
        self.counter = 0
        self.start_time = datetime.now()
        print("Starting data scraping at {}.".format(self.start_time))

    ### Grabbing a status
    def on_status(self, status):
        self.counter += 1
        ### Uncomment this line if you want to print out each status in the terminal.
        #print(status.user.name + ": " + status.text,"\n")
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
