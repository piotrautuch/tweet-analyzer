from stream import getTweets
"""
    BEFORE RUNNING THIS APP
    1. Create a twitter account and access your API credentials
    2. Create a tweetapi.txt file in the main directory of this app.
    3. Paste in your consumer key, consumer secret, access token, and access token secret (in this order)
    4. Now the getTweets function will be able to use Twitter API
"""

### Main function
def main():
    keyword, max_tweets = getInput()
    print(keyword, max_tweets)
    getTweets(keyword, max_tweets)



### Obtaining and validating the keyword that we want to look for
### The keyword has to be alphanumeric and not longer than 64 characters

def getInput():
    keyword = ""
    max_tweets = ""
    while keyword.isalnum() == False or len(keyword) >= 64:
        keyword = input("Type in a correct keyword (alphanumeric with at least one character)")
    while max_tweets.isdigit() == False:
        max_tweets = input("Type in a maximum number of tweets you want to get")
    return keyword, int(max_tweets)





if __name__ == "__main__":
    main()
