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
from config import *
import random
import linecache
from time import gmtime,strftime,localtime

count= len(open(POEMfilename,'rU').readlines())

# find a line in the poem FILE
def greetme():
        global count,POEMfilename
        line = random.randint(1,count)
        count2 = linecache.getline(POEMfilename,line)
        #return unicode(count2.strip(),"utf-8")+strftime("%H:%M:%S %B %d %Y")
        return unicode(count2.strip(),"utf-8")+strftime("%m.%d-%H:%M")

