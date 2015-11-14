import indicoio
indicoio.config.api_key = '580dc401830e72a98d4834bafe5b7d7c'
text_input = raw_input('enter feels here: ')
print text_input
print(indicoio.sentiment_hq(text_input))