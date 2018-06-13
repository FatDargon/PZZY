# -*- coding:utf-8 -*-
'''
Created on 2018年6月12日

@author: Administrator
'''
import numpy as np
import cv2
import random
def hh(img):
    displayImg = img[0:401,0:720]
    # cv2.imshow('Image',displayImg)
    cv2.rectangle(img, (0, 50), (720, 401), (255,0,0), 2)
    thresh = displayImg
    # _threshold = cv2.getTrackbarPos('threshold', "Image")
#     print _threshold
    # print displayImg.size
    img_gray = cv2.cvtColor(displayImg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 220, 255, 0)
    qw, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    _list = []
    i = 0
    for cnt in contours:
        r = random.random() * 225
        g = random.random() * 225
        b = random.random() * 225
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if area > 15 and area/perimeter > 1.0:
            i = i + 1
            M = cv2.moments(cnt)
            Cx = int(M['m10'] / M['m00'])
            Cy = int(M['m01'] / M['m00'])
            _str = "Area : " + str(area) + " Area/Perimeter : " + str(area/perimeter)
                   # + "  (X : " + str(Cx) + ",Y :" + str(Cy) + ")"
            cv2.putText(img, _str, (160, 100 + i * 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (r, g, b), 2)
            cv2.drawContours(img, cnt, -1, (r, g, b),thickness=10)
            _list.append((Cx,Cy))
    # cv2.imshow("Image", thresh)
    cv2.imshow("source", img)
    if _list ==[]:
        _list.append((0,0))
    return _list
def hh2(img):
    w = 66
    h = 73
    if img is None:
        return 0,0
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
    start = 200
    end = 1550
    counter = 0
    i = 0
    j=0
    tmpX,tmpY = hh2(frame)
    tmpZ = 30
    while (sucess):
        sucess, img = videoCapture.read()
        # displayImg = cv2.resize(frame, (1024, 768))  # resize it to (1024,768)
        i = i + 1
        
        counter = counter+1
        # print i
        # print i/3
        if counter>start and counter <end:
            print "in " + str(i)
            # cv2.imwrite("1234.png",displayImg)
            cv2.namedWindow('source')
            cv2.namedWindow("Image")
            # cv2.createTrackbar('threshold', 'Image', 0, 255, hh)
#             print type(img)
            if img is None:
                print "img is none"    
            else:
                X,Y = hh2(img)#基点坐标
                _list = hh(img)#检测点坐标              
                print "基点坐标"
                print X,Y
                print "基点坐标跳动"
                print X-tmpX
                Z =X-tmpX
                tmpX,tmpY = X,Y
                if Z-tmpZ > 20:
                    j=j+1
                cv2.putText(img, str(j), (100, 50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
                t = -1
                for _Cx,_Cy in _list:
                    cv2.circle(img,((X+33),(Y+160+36-80-80-15)),15,(255,255,255),-1)
                    t= t+1
#                     print "ttttttt"+str(t)
                    if _Cx+_Cy==0:
                        cv2.putText(img, "None", (200, 50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), 2) 
                    else:
#                         cv2.line(img, (_Cx,_Cy),((X+33),(Y+160+36-84-84))\
#                                 ,(0, 0, 255));  
                        iii =(_Cx-(X+33))/58+1
                        jjj = (_Cy-(Y+160+36-80-80-15))/80+1
                        cv2.putText(img, "in row: "+str(iii+j)+" column: "+str(jjj), (200, 50+t*30), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), 2)
                tmpZ = Z
                cv2.imshow("source", img)
        else:
            continue
        keycode = cv2.waitKey(10)
        if keycode == 27:
            cv2.destroyWindow('test Video')
            videoCapture.release()
            break