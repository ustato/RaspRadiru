# -*- coding: utf-8 -*-
import yaml
import requests
import json
from datetime import datetime

yaml_dict = yaml.load(open('/root/scripts/slack.yaml'), Loader=yaml.SafeLoader)
token = yaml_dict['slack_bottoken']
u_name = yaml_dict['slack_botname']
c_name = yaml_dict['slack_channel']
extract_channel = (c_name)

url = "https://slack.com/api/users.list?token=" + token
headers = {"content-type": "application/json"}
r = requests.get(url,headers=headers)
json_data = r.json()
user_info = [member for member in json_data['members']
             if u_name in member['name']].pop()

url = "https://slack.com/api/channels.list?token=" + token
r = requests.get(url,headers=headers)
json_data = r.json()
entries = [attr for attr in json_data['channels']
            if attr['name'] in extract_channel]
entries = sorted( entries , key=lambda x:x['created'] )
for attr in entries:
    url = ("https://slack.com/api/channels.history?token=" +
            token + "&channel=" + attr['id'])
    r = requests.get(url ,headers=headers)
    json_data = r.json()
    try:
        entries2 = [message for message in json_data['messages']
                    if message['user'] == user_info['id']]
        entries2 = sorted( entries2 , key=lambda x:x['ts'] )
        attr2 = entries2.pop()
        url = "https://slack.com/api/chat.delete?token=" + token + "&channel=" + attr['id'] + "&ts=" + attr2['ts']
        r = requests.get(url ,headers=headers)
        json_data = r.json()
    except KeyError:
        print("No chat.")
