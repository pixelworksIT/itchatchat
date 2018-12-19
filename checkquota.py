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
from greetme import *
import os

# get quota report file for each user 
def checkquota(user):
        try:
                with open(os.path.join(WORK,PATH+user),'r') as infile:
                        return(infile.read())
        except:
                return(greetme())
# someone would like to get specific volume quota               
def checkquota2(user,qtree):
        try:
                with open(os.path.join(WORK,PATH2+user+qtree),'r') as infile:
                        return(infile.read())
        except:
                return(greetme())


