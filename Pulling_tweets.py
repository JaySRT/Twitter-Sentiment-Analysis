#Day1 about how to pull tweets from the Twitter account 
import tweepy
consumer_key = "write your key here"
consumer_secret = "write your key here"
access_token = "write your key here"
access_token_secret = "write your key here"


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

    
#This should print the first 15 tweets from your home Twitter account. 
#This data can be used for Text mining
