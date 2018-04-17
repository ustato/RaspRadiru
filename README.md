# RaspRadiru
NHKのネットラジオらじる★らじるの番組を自動再生してくれる
<<<<<<< HEAD
omxplayer --timeout 60s -o local https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8
omxplayer --timeout 60s -o local https://nhkradiobkr1-i.akamaihd.net/hls/live/512291/1-r1/1-r1-01.m3u8
=======


~~# 最初に実行
```
cd stream
git submodule init
git submodule update
chmod +x *.sh
```

## らじる★らじる
### ラジオを再生(R1チャンネル)
```
stream/nhk_stream.sh r1
```
### ラジオを停止
```
pkill -f rtmpdump
```~~
>>>>>>> 7c710e87bddc762ec7bd2709a610c3b333242cb0
