import os

# if true, all these parameters will be configured with environment variable starting with "MAR-".
_CONFIGURE_WITH_ENV = os.environ.get('MAR-_CONFIGURE_WITH_ENV', False)

# Slack
SLACK_TOKEN = "YOUR SLACK'S TOKEN."
USERNAME = "SLACK SENDER'S USERNAME."
CHANNEL = "SLACK CHANNEL'S NAME."
ICON_EMOJI = "SLACK SENDER'S ICON EMOJI."

# Twitter
CONSUMER_KEY = "YOUR TWITTER APP'S KEY."
CONSUMER_SECRET = "YOUR TWITTER APP'S SECRET KEY."
ACCESS_TOKEN = "YOUR TOKEN."
ACCESS_TOKEN_SECRET = "YOUR SECRET TOKEN."

# Destination to save images
SAVE_IMAGE_DIR = './imgs/'

if _CONFIGURE_WITH_ENV:
    # Slack
    SLACK_TOKEN = os.environ.get('MAR-SLACK_TOKEN')
    USERNAME = os.environ.get('MAR-USERNAME')
    CHANNEL = os.environ.get('MAR-CHANNEL')
    ICON_EMOJI = os.environ.get('MAR-ICON_EMOJI')

    # Twitter
    CONSUMER_KEY = os.environ.get('MAR-CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('MAR-CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('MAR-ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('MAR-ACCESS_TOKEN_SECRET')

    # Destination to save images
    SAVE_IMAGE_DIR = os.environ.get('MAR-SAVE_IMAGE_DIR')
