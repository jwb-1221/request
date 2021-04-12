#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os
from common import config
def new_report(testreport):
    lists = os.listdir(testreport)#从文件夹获取html列表
    file_new = os.path.join(testreport,lists[-1])#取列表得最后一个值
    file_new1 = str(file_new)#转换为字符串类型
    return file_new1
if __name__=='__main__':
    # new_report(config.TEST_REPORT)
    print(new_report(config.TEST_REPORT))