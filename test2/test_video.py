# -*- coding:utf-8 -*-  
'''
Created on 2018年6月12日

@author: Administrator
'''
import numpy as np  
import cv2  
import random

def hh(_threshold):
    displayImg = img[0:401,0:720]
    # cv2.imshow('Image',displayImg)
    cv2.rectangle(img, (0, 50), (720, 401), (255,0,0), 2)
    thresh = displayImg
    # _threshold = cv2.getTrackbarPos('threshold', "Image")
    print _threshold
    # print displayImg.size
    img_gray = cv2.cvtColor(displayImg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 220, 255, 0)
    qw, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    i = 0
    for cnt in contours:
        r = random.random() * 225
        g = random.random() * 225
        b = random.random() * 225
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if area > 50 and area/perimeter > 1.2:
            i = i + 1
            M = cv2.moments(cnt)
            Cx = int(M['m10'] / M['m00'])
            Cy = int(M['m01'] / M['m00'])
            _str = "Area : " + str(area) + " Area/Perimeter : " + str(area/perimeter)
                   # + "  (X : " + str(Cx) + ",Y :" + str(Cy) + ")"
            cv2.putText(img, _str, (160, 100 + i * 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (r, g, b), 2)
            cv2.drawContours(img, cnt, -1, (r, g, b),thickness=10)
    # cv2.imshow("Image", thresh)
    cv2.imshow("test Video", img)

  
if __name__ == "__main__":  
    #step1: load in the video file  
    videoCapture=cv2.VideoCapture('1.mp4')      
    #step2:get a frame  
    sucess,frame=videoCapture.read()   
    #step3:get frames in a loop and do process
    # print (sucess)
    i =0
    while(sucess):
        sucess, frame = videoCapture.read()
        displayImg = frame
        # displayImg = cv2.resize(frame, (1024, 768))  # resize it to (1024,768)
        i=i+1
        # print i
        # print i/3
        if not (0):
            print "in "+str(i/3)
            # cv2.imwrite("1234.png",displayImg)
            cv2.namedWindow('test Video')
            # cv2.namedWindow("Image")
            # cv2.createTrackbar('threshold', 'Image', 0, 255, hh)
            img = displayImg
            hh(200)
            cv2.putText(displayImg,str(i)+"**",(400,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
            cv2.imshow("test Video",displayImg)
        keycode=cv2.waitKey(40)
        if keycode==27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break