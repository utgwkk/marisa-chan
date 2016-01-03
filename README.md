# marisa-chan
## これなん
ふぁぼった画像付きツイートをSlackに流して画像を保存するやつ

## How to use
トークンを取ってきて、所定の変数に格納してから、

```sh
# tweepyをgitから引っ張ってくる(PyPIのものはstreamingのバグが修正されていないので)
$ pip install -r requirements.txt
$ pip install -U git+https://github.com/tweepy/tweepy.git
$ python marisa-chan.py
```

## dependencies
* Python 3.x
* tweepy
  * ~~tweepy/streaming.pyを、[このissueの回答通りに](https://github.com/tweepy/tweepy/issues/615#issuecomment-122886173)修正する必要があります~~
  * GitHubに上がっているものは修正済みのようです。
* requests

## TODO
* [ ] 真面目にREADMEを書く
* [x] 例外発生時のtracebackをいい感じに取得する

## エラーで落ちるのなんとかしてほしい
こういう感じのシェルスクリプトを書きます。

```sh
#!/bin/sh
while :
do
  python marisachan.py
  sleep 10
done
```

そして、

```sh
$ bash start.sh
```

としてやれば、あら不思議! 魔理沙ちゃんが死んでも 10 秒後には蘇ってくれます。

## 最後に
Pull requests are welcome!
