# -*- coding: utf-8 -*-

import wget
import re

url = 'https://gogakuru.com/english/phrase/program/272_ラジオ英会話.html'
wget.download(url)

ld = open('272_ラジオ英会話.html')
words = ['<span lang="en" class="font-en">','<dd class="jp">','<div class="info_date">']
lines = ld.readlines()
ld.close()

sentence = ""
for line in lines:
        for word in words:
                if line.find(word) >= 0:
                        if word == words[0]:
                                sentence+=re.findall('<a .+">(.+)</span></a>',line[:-1])[0]+'\n'
                        elif word == words[1]:
                                sentence+=re.findall('<dd .+">(.+)</dd>',line[:-1])[0]+'\n'
                        elif word == words[2]:
                                sentence+=re.findall('<div .+">(.+)</div>',line[:-1])[0]+'\n'

with open("sentence.txt", "w") as f:
    f.write(sentence)
f.close()
