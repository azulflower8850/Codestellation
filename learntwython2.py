# Importing the module
from twython import Twython
import serial
import math

#Setting these as variables will make them easier for future edits
app_key = "BgJM8zAWf6LF5KRqn0PlNJWTs"
app_secret = "YHui1c1TIS5gWhh3Kn1CjZOZmlem1t5r1l8nJcEMvbOuOpR3yR"
oauth_token = "4190375567-3fELjcR6GibnpXr4yOtJA62iw5SCIenNUALJPoq"
oauth_token_secret = "9Tv2bWSvwCEF59cN367IZczC0LqFe5NOLPpkF22yTTK3R"

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break
#The obligatory first status update to test

import indicoio
indicoio.config.api_key = '580dc401830e72a98d4834bafe5b7d7c'





#Twitter stream
from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
        	x = data['text'].encode('utf-8')
                sentiment = (indicoio.sentiment_hq(x))
                chicken =  str(int(math.floor(sentiment*1000)))
                ser = serial.Serial('COM3',9600)
                ser.readline()
                ser.write(chicken)
        	
            

    def on_error(self, status_code, data):
        # print status_code
        x = status_code
        sentiment = (indicoio.sentiment_hq(x))
        chicken = str(int(math.floor(sentiment *1000)))
        ser = serial.Serial('COM3',9600)
        ser.readline()
        ser.write(chicken)
        


        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


stream = MyStreamer(app_key, app_secret, oauth_token, oauth_token_secret)
stream.statuses.filter(track='codestellation')

