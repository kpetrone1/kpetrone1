
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1053232980-n1smbhCN7H2dJDdGSXKhtpswYj3xq1gInihAHCS"
access_token_secret = "hmF1Rk2nrlfZnoOn9VBsKDfD1pnnVPsQp0OsxBNT0SB4a"
consumer_key = "nL3UK4lG6eJSoRMesaXyh4jMi"
consumer_secret = "QAmwiRsadck4vdQNdliPXLhI3UwN5XoWCkqPf0u589645HIRhM"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


#if __name__ == '__main__':

    # #This handles Twitter authetification and the connection to Twitter Streaming API
    # l = StdOutListener()
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l)

    # #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['wcw', 'Woman crush Wednesday'])

import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'C:/Users/kpetrone1/Desktop/Problem Solving Software Design/kpetrone1/twitter_data.txt'


tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))

tweets = pd.DataFrame()
# def _ensure_valid_index(self, value):                  # _ensure_valid_index function is from http://b-schubertfred2.readthedocs.io/en/latest/_modules/pandas/core/frame.html
#         """
#         "ensure that if we don't have an index, that we can create one from the
#         passed value"
#         """
#         if not len(self.index):

#             # GH5632, make sure that we are a Series convertible
#             if is_list_like(value):
#                 try:
#                     value = Series(value)
#                 except:
#                     pass

#                 if not isinstance(value, Series):
#                     raise ValueError('Cannot set a frame with no defined index '
#                                      'and a value that cannot be converted to a '
#                                      'Series')
#                 self._data.set_axis(1, value.index.copy(), check_axis=False)

#             # we are a scalar
#             # noop
#             else:

#                 pass
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data) 

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')