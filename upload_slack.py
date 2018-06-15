# -*- coding: utf-8 -*-
import sys
from slacker import Slacker
import datetime

date = str(datetime.date.today())

# API token
# SlackのAPIトークンを入力する
token = 'xxxx-xxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx'
# 投稿するチャンネル名
c_name = 'channel'

# 投稿する画像ファイルへのパス(パラメタから取得)
f_path = sys.argv[1]

# 投稿
slacker = Slacker(token)
slacker.chat.post_message(c_name, date+'分音声自動アップロード', as_user=True)
slacker.files.upload(f_path, channels=[c_name], title='radio_english_'+date+'.m4a')
