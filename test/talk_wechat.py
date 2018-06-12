# -*- coding:utf-8 -*-  
'''
Created on 2017年12月19日

@author: Administrator
'''
import requests
import itchat
import base64
from get_AT import *
from myprint import pretty_dict
from requests.exceptions import RequestException
from itchat.content import *

def get_pic_one():
    f = open('1.jpg', 'rb')
    # 参数images：图像base64编码
    img1 = base64.b64encode(f.read())
    return img1
def get_pic_two(filename):
    f = open(filename, 'rb')
    img2 = base64.b64encode(f.read())
    return img2
def get_response(filename):
    dict = get_AT_from_text()
    # 构造了要发送给服务器的数据
    apiUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/match?access_token='+dict['access_token']
    img1 = get_pic_one()
    img2 = get_pic_two(filename)
    data = {
        "images":img1 + ',' + img2,
    }
    headers = {
       'content-type': 'application/x-www-form-urlencoded', 
    }
    try:
        r = requests.post(apiUrl,data=data,headers=headers).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
#         print type(r)
        pretty_dict(r)
        try:
            score = r[u'result'][0][u'score']
            print score
            return u'你的得分是 ：'+str(score)
        except:
            return u'请输入人的相片'
    except (RequestException),e:
        # 将会返回一个None
        return e.message

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = u'不要发文字'
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
#     print type(msg['FileName'])
    reply = get_response(msg['FileName'])
    defaultReply = 'I received: ' + str(msg['Text'])
    return reply or defaultReply
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()

# print get_response(1)