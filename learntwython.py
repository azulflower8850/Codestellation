# Importing the module
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key = "H9mapu9yLJR9dAh3T3qkU4YWB"
app_secret = "NImr0l7PX9pzu1as55KZj7RYbSmZnLF7svC8VlDW3rVJmX89xF"
oauth_token = "4190375567-3fELjcR6GibnpXr4yOtJA62iw5SCIenNUALJPoq"
oauth_token_secret = "9Tv2bWSvwCEF59cN367IZczC0LqFe5NOLPpkF22yTTK3R"

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

#The obligatory first status update to test
# twitter.update_status(status="Hello, world!")



#Try to make a twitter search
# search = twitter.search(q='linux')

# file = open("search.txt", "w")

# file.write(str(search))

# file.close()



#Twitter stream
# from twython import TwythonStreamer
# class MyStreamer(TwythonStreamer):
#     def on_success(self, data):
#         if 'text' in data:
#             print data['text'].encode('utf-8')

#     def on_error(self, status_code, data):
#         print status_code

#         # Want to stop trying to get data because of the error?
#         # Uncomment the next line!
#         # self.disconnect()


# stream = MyStreamer(app_key, app_secret, oauth_token, oauth_token_secret)
# stream.statuses.filter(track='python')



user_tweets = twitter.get_user_timeline(screen_name='soylentbro', include_rts=True)

for tweet in user_tweets:
    tweet['text'] = Twython.html_for_tweet(tweet)
    print tweet['text']