# -*- coding: utf-8 -*-
import yaml
import requests
import json
from datetime import datetime

yaml_dict = yaml.load(open('/root/scripts/slack.yaml'), Loader=yaml.SafeLoader)
token = yaml_dict['slack_bottoken']
c_name = yaml_dict['slack_channel']
url = "https://slack.com/api/channels.list?token=" + token
headers = {"content-type": "application/json"}
extract_channel = (c_name)

r = requests.get(url,headers=headers)
data = r.json()
entries = [attr for attr in data['channels'] if attr['name'] in extract_channel]
entries = sorted( entries , key=lambda x:x['created'] )
for attr in entries:
    url2 = "https://slack.com/api/channels.history?token=" + token + "&channel=" + attr['id']
    headers2 = {"content-type": "application/json"}
    r2 = requests.get(url2 ,headers=headers2)
    json_data2 = r2.json()
    try:
        entries2 = json_data2['messages']
        entries2 = sorted( entries2 , key=lambda x:x['ts'] )
        attr2 = entries2[-1]
        url2 = "https://slack.com/api/chat.delete?token=" + token + "&channel=" + attr['id'] + "&ts=" + attr2['ts']
        headers2 = {"content-type": "application/json"}
        r2 = requests.get(url2 ,headers=headers2)
        json_data2 = r2.json()
    except KeyError:
        print("No chat.")
