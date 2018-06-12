# -*- coding:utf-8 -*-  
'''
Created on 2017年12月19日

@author: Administrator
'''
import urllib, urllib2, sys
import ssl
from myprint import *
AKEY = 'h5MNQt93izY6ih3yM6MMkvte'
SKEY = 'TV37Gx646k1oAZoiITBzVAfCSHv9dmQr'
# client_id 为官网获取的AK， client_secret 为官网获取的SK
def get_AT():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AKEY+'&client_secret='+SKEY
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    
    if (content):
        f = open('1.txt','w')
        f.write(content)
        f.close()
        dict = eval(content)
        pretty_dict(dict)
        return dict
def get_AT_from_text():
    f = open('1.txt','r')
    text = f.read()
    dict = eval(text)
    pretty_dict(dict)
    f.close()
    return dict
    