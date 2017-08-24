# coding: utf-8
# __author__: u"Yuqin"
"""
这里存放一些公用的函数, 例如生成树、读写文件之类的
"""
from os.path import join, splitext
from datetime import datetime
from struct_data import HEADERS, ENCODING, COLUMNS
import pandas as pd
import time
import os
import re
import sys

def read_data_set(file_name, cleaned=False):
    """
    读取项目数据集, 并返回DataFrame
    例子:
        如果要读取data.csv,
        file_name 传入 "data.csv" 即可
    :param file_name: str
    :param cleaned:
    :return:
    """
    #df = pandas.read_table(get_file_path(file_name, cleaned), sep=",")
    #df.columns = HEADERS.get(splitext(file_name)[0])
    list = []
    with open(get_file_path(file_name,cleaned=False), "rb") as csvfile:
        for row in csvfile:
            doc_id = re.split(r'\t', row)[0].decode('gb18030')
            doc_title = re.split(r'\t', row)[1].decode('gb18030')
            doc_content = re.split(r'\t', row)[2].decode('gb18030')
            list.append({"doc_id": doc_id, "doc_title": doc_title, "doc_content": doc_content})
        return list

#def read_train_data_set(file_name, cleaned=False):
#    list = []
#    with open(get_file_path(file_name,cleaned=False), "rb") as csvfile:
#        for row in csvfile:
#            user_id = re.split(r'\t', row)[0].decode('gb18030')
#            doc_id = re.split(r'\t', row)[1].decode('gb18030')
#            user_click = re.split(r'\t', row)[2].decode('gb18030')
#            list.append({"user_id": user_id, "doc_id": doc_id, "user_click": user_click})
#        return list

def get_file_path(file_name, cleaned=False):
    """
    查找文件名所在的绝对路经
    :param file_name:
    :param cleaned:
    :return:
    """
    f_name, ext = splitext(file_name)
    dir_name = f_name.split("_")[-1]

    if cleaned:
        dir_name = "cleaned_{0}".format(dir_name)

    if not ext:
        ext = ".csv"

    return join(join(os.getcwd(), dir_name), f_name + ext)
    #return join(join(os.getcwd(), dir_name))

def save_data_set(data, file_name, cleaned=True):
    """
    存放数据集
    如果是存放清洗后的数据集, 格式和清洗前保持一致:
        1. 无表头
        2. 逗号分隔符
    :param data: DataFrame
    :param file_name: str
    :param cleaned:
    :return:
    """
    file_name = get_file_path(file_name, cleaned)
    data.to_csv(file_name, HEADERS=False, encoding=ENCODING, index=False)
    return


#df=read_train_data_set("train.csv",cleaned=False)
#df1=pd.DataFrame(df)
#print df1["user_click"]
