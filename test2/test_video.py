# -*- coding:utf-8 -*-  
'''
Created on 2018年6月12日

@author: Administrator
'''
import numpy as np  
import cv2  

def hh(displayImg):
    returnImg=displayImg
    return returnImg
  
if __name__ == "__main__":  
    #step1: load in the video file  
    videoCapture=cv2.VideoCapture('1.mp4')      
    #step2:get a frame  
    sucess,frame=videoCapture.read()   
    #step3:get frames in a loop and do process   
    while(sucess):  
        sucess,frame=videoCapture.read()  
        displayImg=cv2.resize(frame,(1024,768)) #resize it to (1024,768)  
        displayImg=hh(displayImg)
        cv2.putText(displayImg,"Hello World!",(400,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)  
        cv2.namedWindow('test Video')      
        cv2.imshow("test Video",displayImg)  
        keycode=cv2.waitKey(1)  
        if keycode==27:  
            cv2.destroyWindow('test Video')  
            videoCapture.release()  
            break  