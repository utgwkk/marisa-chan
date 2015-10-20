import os
import requests
from constant import *

def post_to_Slack(params):
    return requests.post(slackURL + "chat.postMessage", params=params)

def create_twitter_url(id_str, screen_name):
    return "https://twitter.com/"+screen_name+"/status/"+id_str

