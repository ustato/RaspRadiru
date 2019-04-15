FROM python:latest


ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS yes

# 必要なパッケージを追加
RUN apt-get -y update --fix-missing \
    && apt-get -y upgrade \
    && apt-get install -y wget bzip2 ca-certificates busybox-static \
       libglib2.0-0 libxext6 libsm6 libxrender1 cron ffmpeg emacs

# タイムゾーン設定
ENV TZ=Asia/Tokyo


# スクリプト保存ディレクトリ
RUN mkdir /root/scripts
ADD upload_slack.py /root/scripts/upload_slack.py

# 音声の自動録音保存フォルダ
RUN mkdir /root/databank

# crontabファイルをコピー
COPY crontab /var/spool/cron/crontabs/root

# cronを起動
# busybox crond -f -L /dev/stderr
RUN export EDITOR="/usr/bin/emacs"
CMD ["busybox", "crond", "-f", "-L", "/dev/stderr"]
