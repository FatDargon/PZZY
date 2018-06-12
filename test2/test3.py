# -*- coding:utf-8 -*-
'''
Created on 2018年1月5日

@author: Administrator
'''
# 导入cv模块
import numpy as np
import random
import cv2


def nothing(args):
    pass


def hh(_threshold):
    displayImg = img[63:401,0:720]
    # cv2.imshow('Image',displayImg)
    cv2.rectangle(img, (0, 63), (720, 401), (255,0,0), 2)
    thresh = displayImg
    # _threshold = cv2.getTrackbarPos('threshold', "Image")
    print _threshold
    # print displayImg.size
    img_gray = cv2.cvtColor(displayImg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 223, 255, 0)
    qw, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    i = 0
    for cnt in contours:
        r = random.random() * 225
        g = random.random() * 225
        b = random.random() * 225
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if area > 5 and area/perimeter > 0.3:
            i = i + 1
            M = cv2.moments(cnt)
            Cx = int(M['m10'] / M['m00'])
            Cy = int(M['m01'] / M['m00'])
            _str = "Area : " + str(area) + " Area/Perimeter : " + str(area/perimeter)
                   # + "  (X : " + str(Cx) + ",Y :" + str(Cy) + ")"
            cv2.putText(img, _str, (160, 100 + i * 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (r, g, b), 2)
            cv2.drawContours(img, cnt, -1, (r, g, b), 3)
    # cv2.imshow("Image", thresh)
    cv2.imshow("source", img)


if __name__ == '__main__':
    img = cv2.imread("1234.png")
    # 创建窗口并显示图像
    # cv2.namedWindow("Image",cv2.WINDOW_NORMAL )

    cv2.namedWindow("source",cv2.WINDOW_NORMAL )

    # cv2.createTrackbar('threshold', 'Image', 0, 255, hh)
    hh(125)
    # cv2.setMouseCallback('test Video', hh)

    cv2.waitKey(0)
