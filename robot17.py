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
# 		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
## // ##

#import os
#import requests as rq
import itchat, time
from itchat.content import *
#from time import gmtime,strftime,localtime
#import re,sys,json
#import datetime
#from sys import argv
import subprocess
import threading


#import linecache
#import random

from config import *
from checkquota import *
from greetme import *
from checklicense import *
from tulingxiaobin import *
from helpme import *

# check license,  check host,  valid users?
# ignore uppercase
# if extract match,  display
# if multi match,  display the list
# if none match give a poem

# this is main function to decide which command to go
# if no match, go chat
def HELPDESKprocess(buf,userid,group):
	buf=re.sub(ur'\u2005', ' ', buf)
	#print buf.encode("utf-8")
	#buf=buf.rstrip()
	#buflist=buf.split(' ')
	buflist=re.compile("\s+").split(buf)
	#print buflist[1].encode("utf-8")
	if (len(buflist) != 3) and (len(buflist) != 4) :
		return (tuling(buf,group))
	if buflist[1] == 'license':
		return (checkLicense(buflist[2],LICfile,':'))
	elif buflist[1] == 'prtg'and group == wechatITgrp :
		return (prtg_show(buflist[2],group))
	elif buflist[1] == 'licenseuse':
		return (licenseuse(buflist[2],LICfile,':'))
	elif buflist[1] == 'unlock' and (group == wechaticitgrp or group == wechatITgrp) :
		return (subprocess.check_output(UNLOCK+" "+buflist[2], shell=True).decode("utf-8"))
	elif (buflist[1] == 'help') and (buflist[2] == 'me' ) :
		return (helpme())
	elif buflist[1] == 'checkquota':
		if len(buflist) == 3 :
			return (checkquota(buflist[2]))
		else :
			return (checkquota2(buflist[2],buflist[3]))
	elif buflist[1] == 'hostnum':
		return (checkLicense(buflist[2],bhostsfile,' '))
	elif buflist[1] == 'hostload':
		return (checkLicense(buflist[2],lsloadfile,' '))
	else:
		return (greetme())
	return (tuling(buf,group))
	

# in group chat, when someone At me, try to reply
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
	#print msg['Text'].encode("utf-8")
	if msg['IsAt']:
		fromUserName = msg['FromUserName']
		group=itchat.search_chatrooms(userName=fromUserName)
		groupNick=group['NickName'].encode('utf-8')
		REPLY=HELPDESKprocess(msg['Content'],fromUserName,groupNick)
		if REPLY :
			itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'],REPLY ), msg['FromUserName'])



@itchat.msg_register(SYSTEM)
def get_uin(msg):
    if msg["SystemInfo"] != 'unis':
        return
    ins = itchat.instanceList[0]
    fullContact = ins.memberList + ins.chatroomList + ins.mpList
    print("** Uin updated **")
    for username in msg["Text"]:
        member = itchat.utils.search_dict_list(fullContact, 'UserName', username)
        print(("%s: %s" % (member.get("NickName", ''), member["Uin"])).encode(sys.stdin.encoding, 'replace'))


#watch certain logs
def tail(LOG_file,):
	f = subprocess.Popen(['tail','-n','0','-F',LOG_file],\
	stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	while True:
		line = f.stdout.readline()
		GroupChat.send('%s' % line)

def tail_icit(LOG_file_icit,):
	f = subprocess.Popen(['tail','-n','0','-F',LOG_file_icit],\
	stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	while True:
		line = f.stdout.readline()
		GroupChat_icit.send('%s' % line)

#every day, send a message, so people know I am alive
def heartme(_start,):
	while True:
		time.sleep(86400)
		if time.time()-_start >=86400:
			#boss.send('%s' % greetme())
			GroupChat.send('%s' % greetme())
			GroupChat_icit.send('%s' % greetme())
			_start=time.time()



if __name__ == '__main__':



	try:
		itchat.auto_login(enableCmdQR=-2,hotReload=True)
		_start = time.time()
	#say hello
		boss=itchat.search_friends(nickName=bossname)[0]
		GroupChat_icit=itchat.search_chatrooms(name=wechaticitgrp.decode("utf-8"))[0]
		GroupChat_debug=itchat.search_chatrooms(name=wechattestgrp.decode("utf-8"))[0]
		GroupChat=itchat.search_chatrooms(name=wechatITgrp.decode("utf-8"))[0]
		#boss.send('%s' % greetme())
	#watch the logs
		TailmeThread = threading.Thread(target=tail,args=(LOG_file,))
		TailmeThread.setDaemon(True)
		TailmeThread.start()
		TailmeThread_icit = threading.Thread(target=tail_icit,args=(LOG_file_icit,))
		TailmeThread_icit.setDaemon(True)
		TailmeThread_icit.start()
	# heart beat
		heart = threading.Thread(target=heartme,args=(_start,))
		heart.setDaemon(True)
		heart.start()
	# handle the message
		itchat.run(True)
	except (KeyboardInterrupt,SystemExit):
		cleanup_stop_thread()
		sys.exit()
