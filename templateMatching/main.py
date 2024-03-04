import cv2 as cv
import numpy as np
path="venv/images"

def template():
    src=cv.imread(path+"/test.png")
    tpl=cv.imread(path+"/test1.png")

    cv.imshow("verilen",src)
    cv.imshow("aranan",tpl)


    th, tw=tpl.shape[:2]

    result=cv.matchTemplate(src,tpl,method=cv.TM_CCORR_NORMED)


    t=0.98
    loc=np.where(result>t)

    for pt in zip(*loc[::-1]):

        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (0, 165, 255), 1, 8, 0)

    cv.imshow("sonuc",src)
template()
cv.waitKey()
