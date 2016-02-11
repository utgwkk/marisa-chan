# marisa-chan
[![Build Status](https://travis-ci.org/utgw/marisa-chan.svg?branch=master)](https://travis-ci.org/utgw/marisa-chan)
## What is this?
*marisa-chan* is a script that detects tweets you liked in Twitter and posts the tweet's URL to your Slack channel.

## How to use
* First, you have to obtain your Twitter app's consumer key and API token from [apps.twitter.com](https://apps.twitter.com/).
* Configure some settings in config.py:

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
