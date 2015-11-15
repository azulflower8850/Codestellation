#import indicoio api configuration
import indicoio
indicoio.config.api_key = '580dc401830e72a98d4834bafe5b7d7c'

#use api to calculate sentiment analysis. sentiment is number 0-1
text_input = raw_input('enter feels here: ') #take user input
sentiment = (indicoio.sentiment_hq(text_input)) #use indico api to calculate input. save value as sentiment


file = open("sentimentnumber*.csv", "w")

file.write(str(sentiment))

file.close()