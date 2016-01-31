from config import *
import tweepy

# Slack
slackURL = "https://slack.com/api/"
params = {'token': SLACK_TOKEN, 'channel': CHANNEL, 'text': '', 'username': USERNAME, 'icon_emoji': ICON_EMOJI}

# Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
me = api.me().screen_name


