# coding: utf-8
# __author__: u"Yuqin"
"""
这里存放的是元数据
header, 表头信息
relation, 字段关系
tables, 数据集信息
等信息
"""
from __future__ import unicode_literals
from os.path import join
from os import listdir, getcwd

TABLES = filter(lambda x: ".csv" in x, listdir(join(getcwd(), "train")) + listdir(join(getcwd(), "test")))

HEADERS = dict(
    example=["user_id", "doc_id", "percentage"],
    data_test=["doc_id", "doc_content"],

    browse_history_train=["用户id", "时间戳", "浏览行为数据", "浏览子行为编号"],
    browse_history_test=["用户id", "时间戳", "浏览行为数据", "浏览子行为编号"],
    loan_time_train=["用户id", "放款时间"],
    loan_time_test=["用户id", "放款时间"],
    overdue_train=["用户id", "样本标签"],
    user_info_train=["用户id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"],
    user_info_test=["用户id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"],



    test=["user_id","doc_id"],
)


COLUMNS = {
    "点击": {0: "未点击", 1: "点击"},
}

ENCODING = "utf8"