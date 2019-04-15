# -*- coding: utf-8 -*-
import sys
import yaml
import datetime
from slacker import Slacker

date = str(datetime.date.today())

# API token
# SlackのAPIトークンを'tokens.yaml'から参照する
yaml_dict = yaml.load(open('slack.yaml').read())
token = yaml_dict['slack_token']

# 投稿するチャンネル名
c_name = yaml_dict['slack_channel']

# 投稿するファイルへのパス(パラメタから取得)
f_path = sys.argv[1]

# 投稿
slacker = Slacker(token)
slacker.chat.post_message(c_name, date+'分音声自動アップロード', as_user=True)
slacker.files.upload(f_path, channels=[c_name], title='radio_english_'+date+'.m4a')
