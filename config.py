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

BASE="/home/POWERUSER/itchat"
WORK=BASE+"/status"

LICfile=WORK+'/LIC.STS'
bhostsfile=WORK+'/bhosts.STS'
lsloadfile=WORK+'/lsload.STS'
userId = ''

POEMfilename=BASE+'/poem'
count= len(open(POEMfilename,'rU').readlines())


PATH="userpt/userpt3."
PATH2="userpt/userpt4."
LICWORK=WORK+"/licrpt2"
HELPFILE=WORK+"/LOCALHELPFILE"
UNLOCK=WORK+"/unlock"
#config to rsyslog
#local4.=info            /var/log/SOMELOG
#local3.=info            /var/log/OTHERLOG
LOG_file='/var/log/SOMELOG'
LOG_file_icit='/var/log/OTHERLOG'

wechatITgrp = 'IT的群'
wechattestgrp = '247 test 支持群'
wechaticitgrp = '247 群'
bossname = 'CRAZY'
#tuling api key
apiKey="XXXXXXXXXX"


