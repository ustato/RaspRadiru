# -*- coding: utf-8 -*-

import numpy as np
import make_PPTX

ld = open("sentence.txt")
lines = ld.readlines()
ld.close()

# 初回ループ用
word = lines[2]
count = 0

test = []
subtest = []
for i in range(len(lines)):
    # 日付を確認する
    if i % 3 == 2:
        subtest.append(i)
        if lines[i+3].find(word) < 0:
            test.append(np.random.choice(subtest))
            word = lines[i+3]
            subtest = []
            count+=1

    # 1週間を過ぎたら終了
    if count >= 4 :
        break

np.random.shuffle(test)

make_PPTX.make_testPPTX(test,lines)
