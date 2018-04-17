# RaspRadiru
NHKのネットラジオらじる★らじるの番組を自動再生してくれる

# 最初に実行
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
```
