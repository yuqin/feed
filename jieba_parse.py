#-*- coding: UTF-8 -*-
__author__ = 'YuqinJIANG'

#!/usr/bin/env python3
"""
import sys
sys.path.append('/Users/YuqinJIANG/Desktop/e')


import csv




name = input('please enter your name: ')
print('hello,', name)

print(100+200)
print("the quick brown fox","jumps over","the lazy dog")
name=input()


import urllib2

"""
import os
import re
import csv
import codecs
import pandas as pd
import jieba
import jieba.analyse
from optparse import OptionParser
from sklearn.feature_extraction.text import TfidfVectorizer

import sys
#sys.path.append('/Users/YuqinJIANG/PycharmProjects/tools1')
os.chdir('/Users/YuqinJIANG/PycharmProjects/tools1')
#USAGE = "usage:    python extract_tags_with_weight.py ['data.csv'] -k [20] -w [1]"

test_data=pd.read_csv('data.csv',sep='\t',header=None,names=['user_id','doc_id'])
test_doc_id=test_data['doc_id'].drop_duplicates().tolist()
with open('data.csv', "rb") as csvfile:
    for row in csvfile:
        doc_content = re.split(r'\t', row)
        doc_content_1 = doc_content[2].decode('gb18030')
        print doc_content_1
        tags=jieba.analyse.extract_tags(doc_content_1, topK=5, withWeight=1)
        for tag in tags:
           print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
           print(1)
        #seg_list=jieba.cut(doc_content_1,cut_all=True)
        #datareader = csv.reader(csvfile)
        #print ('Full Mode:'+'/'.join(seg_list))
        #关键词抽取
        #创建变量
        #v = TfidfVectorizer(tokenizer=lambda doc_content_1: jieba.cut(doc_content_1,cut_all=True),analyzer='word')
        #train_data = v.fit_transform(train_words)
        #test_data = v.transform(new_words)
        #words = v.get_feature_names()
        #print words
"""

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False



content = open('data.csv', 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=10, withWeight=1)

if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))

"""