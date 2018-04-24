# -*- coding: utf-8 -*-

from pptx import Presentation


def make_testPPTX(test,lines) :
    # 初期化
    prs = Presentation()

    # 問題と正解を作るためにリストを変形
    test=list(test)
    test*=2
    test.sort()
    for (i,j) in enumerate(test) :
        title_slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        if i%2 :
            title.text = lines[j-2]
            subtitle.text = lines[j-1]
        else :
            title.text = ""
            subtitle.text = lines[j-1]

    # 保存
    prs.save('test.pptx')
