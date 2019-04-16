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

# 各種スクリプトと設定ファイルを追加
ADD pylibs/upload_slack.py /root/scripts/upload_slack.py
ADD pylibs/delete_recentlyfile_in_slack.py \
    /root/scripts/delete_recentlyfile_in_slack.py
ADD settings/slack.yaml /root/scripts/slack.yaml
ADD settings/requirements.txt /root/scripts/requirements.txt
RUN pip install -r /root/scripts/requirements.txt

# 音声の自動録音保存フォルダ
RUN mkdir /root/databank

# crontabファイルをコピー
COPY settings/crontab /var/spool/cron/crontabs/root

# cronを起動
# busybox crond -f -L /dev/stderr
RUN export EDITOR="/usr/bin/emacs"
CMD ["busybox", "crond", "-f", "-L", "/dev/stderr"]
