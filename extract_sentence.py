# -*- coding: utf-8 -*-

import wget
import re

url = 'https://gogakuru.com/english/phrase/program/272_ラジオ英会話.html'
wget.download(url)

ld = open('272_ラジオ英会話.html')
words = ['<span lang="en" class="font-en">','<dd class="jp">','<div class="info_date">']
lines = ld.readlines()
ld.close()

for line in lines:
        for word in words:
                if line.find(word) >= 0:
                        if word == words[0]:
                                print re.findall('<a .+">(.+)</span></a>',line[:-1])[0]
                        elif word == words[1]:
                                print re.findall('<dd .+">(.+)</dd>',line[:-1])[0]
                                
                        elif word == words[2]:
                                print re.findall('<div .+">(.+)</div>',line[:-1])[0]

                            
