# RaspRadiru
Raspberry piを使ってNHKラジオ英会話を楽しく学べるシステム


## ラジオ英会話問題自動作成
復習のために，ラジオ英会話の一週間の問題を自動作成してくれるツール．

以下の順に実行する．
```
python extract_sentence.py
python make_test.py
```

### [extract_sentence.py](https://github.com/Atsuto0519/RaspRadiru/blob/master/extract_sentence.py)

ラジオ英会話の公式ページから例文を自動ダウンロードして```sentence.txt```を作成する．

テキスト形式に例文を加工できる．

### [make_test.py](https://github.com/Atsuto0519/RaspRadiru/blob/master/make_test.py)

ラジオ英会話の例文から問題をPowerPoint形式で作成する． 
サンプル```[test.pptx](https://www.slideshare.net/AtsutoInage/test-94869665)```

# らじる★らじる自動再生
NHKのネットラジオらじる★らじるの番組を自動再生するためのプラクティス

## omxplayerを使う
すごく手軽でオススメな方法．

### R1
```
omxplayer --timeout 60s -o local https://nhkradiobkr1-i.akamaihd.net/hls/live/512291/1-r1/1-r1-01.m3u8
```

### R2
```
omxplayer --timeout 60s -o local https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8
```
