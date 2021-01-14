import tweepy 
consumer_key = "entering the key here"
consumer_secret = "entering the key here"
access_token = "entering the key here"
access_token_secret = "entering the key here"


from tweepy.auth import OAuthHandler
#Creating the Auth Object
auth = OAuthHandler(consumer_key, consumer_secret)
#Setting the access token and secret
auth.set_access_token(access_token, access_token_secret)
#Creating the API object while passing in the auth info
api = tweepy.API(auth)


#The search term we want to find
query = "Focus"
#Language code (follows ISO 639-1 standards)
language = "en"

#Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

#Printing all tweets (for each through all tweets pulled)
for tweet in results:
    print(tweet.user.screen_name,"Tweeted:",tweet.text)
