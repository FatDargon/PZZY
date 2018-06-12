# -*- coding:utf-8 -*-
'''
Created on 2018年6月12日

@author: Administrator
'''
import numpy as np
import cv2
import random
def hh2(img):
    w = 66
    h = 73
    displayImg = img[160:320,0:100]
    # cv2.imshow('Image',displayImg)
    cv2.rectangle(img, (0, 140), (100, 320), (0,255,0), 2)
    # _threshold = cv2.getTrackbarPos('threshold', "Image")
    res = cv2.matchTemplate(displayImg, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(displayImg, top_left, bottom_right, 255, 2)
    # # print displayImg.size
    # img_gray = cv2.cvtColor(displayImg, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(img_gray, _threshold, 255, 0)
    cv2.imshow("Image",displayImg)
    cv2.imshow("source", img)
    return top_left[0],top_left[1]


if __name__ == "__main__":
    template = cv2.imread("12.png")
    # step1: load in the video file
    videoCapture = cv2.VideoCapture('1.mp4')
    # step2:get a frame
    sucess, frame = videoCapture.read()
    # step3:get frames in a loop and do process
    # print (sucess)
    i = 0
    j=0
    tmpX,tmpY = hh2(frame)
    tmpZ = 30
    while (sucess):
        sucess, img = videoCapture.read()
        # displayImg = cv2.resize(frame, (1024, 768))  # resize it to (1024,768)
        i = i + 1
        # print i
        # print i/3
        if not (0):
            print "in " + str(i)
            # cv2.imwrite("1234.png",displayImg)
            cv2.namedWindow('source')
            cv2.namedWindow("Image")
            # cv2.createTrackbar('threshold', 'Image', 0, 255, hh)
            X,Y = hh2(img)
            print "zuobiao"
            print X,Y
            print "chazhi"
            print X-tmpX
            Z =X-tmpX
            tmpX,tmpY = X,Y
            if Z-tmpZ > 20:
                j=j+1
            cv2.putText(img, str(j), (400, 50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
            tmpZ = Z
            cv2.imshow("source", img)
        keycode = cv2.waitKey(40)
        if keycode == 27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break