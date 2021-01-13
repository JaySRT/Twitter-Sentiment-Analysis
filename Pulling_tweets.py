import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""



from tweepy.auth import OAuthHandler
#Creating the Auth Object
auth = OAuthHandler(consumer_key, consumer_secret)
#Setting the access token and secret
auth.set_access_token(access_token, access_token_secret)
#Creating the API object while passing in the auth info
api = tweepy.API(auth)

#Testing the API to get tweets from home timeline, and storing it in public_tweets variable
public_tweets = api.home_timeline()
#Printing each tweet
for tweet in public_tweets:
    print (tweet.text)
