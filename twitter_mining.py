# URL of Source: https://www.youtube.com/watch?v=o_OZdbCzHUA
import tweepy
from textblob import TextBlob

consumer_key = "n1sWv9RBBiL4zQWsdRYVfandn"
consumer_secret = "xc8DviZvFECGJbHVTxxwGcvM76VfskZWF8HlNyh7puK4HvBjuQ"

access_token = "1053232980-n1smbhCN7H2dJDdGSXKhtpswYj3xq1gInihAHCS"
access_token_secret = "hmF1Rk2nrlfZnoOn9VBsKDfD1pnnVPsQp0OsxBNT0SB4a"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Women Crush Wednesday', 'WcW')

def print_tweet_text():
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
print_tweet_text()