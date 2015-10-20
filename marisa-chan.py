#!/usr/bin/env python
import os
import tweepy
from traceback import print_exc, format_exc

from constant import *
from misc import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
me = api.me().screen_name

class MyStream(tweepy.StreamListener):
    def on_event(self, status):
        if status.event == 'favorite' and status.source['screen_name'] == me and 'extended_entities' in status.target_object:
            id_str, screen_name = status.target_object['id_str'], status.target_object['user']['screen_name']
            params['text'] = create_twitter_url(id_str, screen_name)
            post_to_Slack(params)
            for media in status.target_object['extended_entities']['media']:
                url = media['media_url_https']
                filename = os.path.basename(url)
                r = requests.get(url + ':orig')
                if r.status_code != 200:
                    r = requests.get(url)
                    if r.status_code != 200:
                        continue
                save_fname = save_image_dir + filename
                with open(save_fname, 'wb') as fout:
                    fout.write(r.content)

if __name__ == '__main__':
    try:
        params['text'] = '@utgw: 霧雨魔理沙、画像蒐集の旅に出発だぜ'
        post_to_Slack(params)
        stream = tweepy.Stream(auth, MyStream())
        stream.userstream()
    except KeyboardInterrupt:
        params['text'] = '@utgw: おやすみなさいだぜ'
    except Exception as e:
        print_exc()
        params['text'] = '@utgw: 画像を集めてたらエラーが発生したぜ\nTraceBackを貼っておくから修正してくれよな\n```\n'
        params['text'] += format_exc()
        params['text'] += '```\nいったん休ませてもらうぜ'
    finally:
        post_to_Slack(params)
