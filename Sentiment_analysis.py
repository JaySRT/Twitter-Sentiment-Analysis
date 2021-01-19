#Codes for terminal before we start with the analysis
#mkdir how-positive-was-your-week
#cd how-positive-was-your-week
#touch week.py
#touch config.yaml

import requests
import pandas as pd
import json
import ast
import yaml

def create_twitter_url():
    handle = "jaysorathi"
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    return url
  
