# marisa-chan
## What' this?
*marisa-chan* is a script that detects tweets you liked in Twitter and posts the tweet's URL to your Slack channel.

## How to use
* First, you have to obtain your Twitter app's consumer key and API token from [apps.twitter.com](https://apps.twitter.com/).
* Store 4 keys and tokens in constant.py like this:

```python
# Twitter
CONSUMER_KEY = "YOUR TWITTER APP'S KEY."
CONSUMER_SECRET = "YOUR TWITTER APP'S SECRET KEY."
ACCESS_TOKEN = "YOUR TOKEN."
ACCESS_TOKEN_SECRET = "YOUR SECRET TOKEN."
```

* Then, execute this in your shell:

```sh
$ pip install -r requirements.txt
$ pip install -U git+https://github.com/tweepy/tweepy.git
$ python marisa-chan.py
```

* It is recommended to execute the script in your own server (with tmux).
* Enjoy it!

## dependencies
* Python 3.x
* tweepy
  * ~~You have to fix tweepy/streaming.py [following this issue](https://github.com/tweepy/tweepy/issues/615#issuecomment-122886173)~~.
  * Tweepy in GitHub already fixed this bug.
* requests

## PR
Pull requests are welcome!
