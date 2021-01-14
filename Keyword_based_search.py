



#The search term we want to find
query = "Focus"
#Language code (follows ISO 639-1 standards)
language = "en"

#Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

#Printing all tweets (for each through all tweets pulled)
for tweet in results:
    print(tweet.user.screen_name,"Tweeted:",tweet.text)

