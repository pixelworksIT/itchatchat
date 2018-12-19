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
import re,sys,json
import os

# who use my license, let's find out, ignore case, 
def licenseuse(feature, LICfile,delim):
        if feature == '':
                return (greetme())
        OUTPUTlist=[]
        featurelist=[]
        #print feature
        for line in open(LICfile):
                line=line.rstrip()
                if re.search(feature, line, re.I):
                        OUTPUTlist.append(line)
        # check if it is exact match, then display single line
	print len(OUTPUTlist)
        if len(OUTPUTlist) > 1:
                for line2 in OUTPUTlist:
                        if re.match(feature+delim, line2, re.I):
                                #print line2
                                #return (licenseuse_f(feature))
                                return (licenseuse_f(line2.split(delim)[0]))
                        else:
                                featurelist.append(line2.split(delim)[0])
                featurestr=' '.join(featurelist)
                return featurestr
        elif len(OUTPUTlist) == 1:
                return (licenseuse_f(OUTPUTlist[0].split(delim)[0]))
        else :
                return (greetme())
# now get the actual license use status file
def licenseuse_f(feature):
        try:
		print feature
                with open(os.path.join(LICWORK,feature.lower()),'r') as infile:
                        return(infile.read())
        except:
                return(greetme())
#find out how many license we have and how many in use on specific feature.
#if only part of feature name input,  display all possiblities.
#and if we can use some function to get bsub info
def checkLicense(feature, LICfile,delim):
        if feature == '':
                return (greetme())
        OUTPUTlist=[]
        featurelist=[]
        #print feature
        for line in open(LICfile):
                line=line.rstrip()
                if re.search(feature, line, re.I):
                        #print line
                        OUTPUTlist.append(line)
        # check if it is exact match, then display single line
        print len(OUTPUTlist) 
        if len(OUTPUTlist) > 1:
                # do we have extract match
                #print "multiple"       
                for line2 in OUTPUTlist:
                        if re.match(feature+delim, line2, re.I):
                                #print (line2)
                                return (line2)
                        else:
                                featurelist.append(line2.split(delim)[0])
                #print ()
                featurestr=' '.join(featurelist)
                return featurestr
        elif len(OUTPUTlist) == 1:
                return (OUTPUTlist[0])
        else :
                return (greetme())
        # if multiple line,  display feature list
        return


