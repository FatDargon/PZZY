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


def hh2(_threshold):
    w = 66
    h = 73
    displayImg = img[140:320,0:100]
    # cv2.imshow('Image',displayImg)
    cv2.rectangle(img, (0, 140), (100, 320), (0,255,0), 2)
    _threshold = cv2.getTrackbarPos('threshold', "Image")
    res = cv2.matchTemplate(displayImg, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(displayImg, top_left, bottom_right, 255, 2)
    # # print displayImg.size
    # img_gray = cv2.cvtColor(displayImg, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(img_gray, _threshold, 255, 0)
    cv2.imshow("Image",displayImg)
    cv2.imshow("source", img)


if __name__ == '__main__':
    img = cv2.imread("1234.png")
    template = cv2.imread("12.png")
    # 创建窗口并显示图像
    cv2.namedWindow("Image",cv2.WINDOW_NORMAL )

    cv2.namedWindow("source",cv2.WINDOW_NORMAL )

    cv2.createTrackbar('threshold', 'Image', 0, 255, hh2)
    hh2(125)
    # cv2.setMouseCallback('test Video', hh)

    cv2.waitKey(0)
