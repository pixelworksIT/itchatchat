#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=UTF-8
##
# Copyright 2018 Pixelworks Inc.
#
# Author: Cheng Chi <cchi@pixelworks.com>
#
# All exported commands in function style here
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#               http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
## // ##
import random
from config import *
import itchat
import re
import requests as rq
from greetme import *


#because xiaobin only support one chatroom, 
#random pick between xiaobin and tuling
def tuling(buf,group):
        #print buf
        line = random.randint(1,2)
        if line == 1 or group == wechatITgrp or group == wechattestgrp :
                return tuling_stupid(buf)
        elif line == 2 and group == wechaticitgrp :
        #elif line == 2 :
                return xiaobin(buf)
        else :
                return (greetme())
#send message to xiaobin
def xiaobin(buf):
        xb=itchat.search_mps(name=u'小冰')[0]
        buflist=re.compile("\s+").split(buf)
        itchat.send_msg(buflist[1],xb['UserName'])
        return


#chat with tuling
def tuling_stupid(buf):
        #info=msg['Content'].encode('utf8')
        info=buf.encode('utf8')
        api_url = 'http://openapi.tuling123.com/openapi/api/v2'
        data = {
                "reqType": 0,
                "perception": {
                        "inputText": {
                                "text": str(info)
                        },
                        "selfInfo": {
                                "location": {
                                "city": "上海",
                "latitude": "38.111111",
                "longitude": "128.111111",
                "nearest_poi_name": "广场",
                "province": "上海",
                "street": "路"
                                            }
                                    }
                },
                "userInfo": {
                        "apiKey": str(apiKey),
                        "userId": "bot"
                }
        }
        headers = {
                'Content-Type': 'application/json',
                'Host': 'openapi.tuling123.com',
                'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0'
                                'Safari/537.36 '
                }
        result = rq.post(api_url, headers=headers, json=data).json()
        return result['results'][0]['values']['text']+u' ~中二的图灵' or greetme()


# whenever get message from xiaobin, send to the dedicate chatroom
@itchat.msg_register([itchat.content.TEXT,itchat.content.PICTURE,itchat.content.RECORDING,itchat.content.ATTACHMENT,itchat.content.VIDEO], isMpChat = True)
def map_reply(msg):
        text=getText(msg)
        global userId
        #msg['Text'](msg['FileName'])
        #return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
        if msg['Type'] == 'Picture':
                msg['Text'](msg['FileName'])
                GroupChat_icit.send_image(msg['FileName'])
        elif msg['Type'] == 'Video':
                msg['Text'](msg['FileName'])
                GroupChat_icit.send_video(msg['FileName'])
        elif msg['Type'] == 'Text':
                GroupChat_icit.send_msg(text + u" ~软的小冰")
        else :
                msg['Text'](msg['FileName'])
                GroupChat_icit.send_file(msg['FileName'])

def getText(msg):
        if msg['Type'] == 'Text':
                return msg['Text']
        else:
                return "发送的其他类型的回复"


