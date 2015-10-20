import os
# Slack
token = "YOUR SLACK TOKEN."
slackURL = "https://slack.com/api/"
username = 'Marisa-chan'
params = {'token': token, 'channel': '#your-channel', 'text': '', 'username': username, 'icon_emoji': ':marisa:'}

# Twitter
CONSUMER_KEY = "YOUR TWITTER APP'S KEY."
CONSUMER_SECRET = "YOUR TWITTER APP'S SECRET KEY."
ACCESS_TOKEN = "YOUR TOKEN."
ACCESS_TOKEN_SECRET = "YOUR SECRET TOKEN."

# Destination to save images
home_dir = os.environ['HOME']
save_image_dir = home_dir + '/imgs/'
