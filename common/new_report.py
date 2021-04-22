#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os
from common import config
def new_report(testreport):
    #获取最新后缀名为html的文件
    lists = os.listdir(testreport)#从文件夹获取html列表
    # file_new = os.path.join(testreport,lists[-1])#取列表得最后一个值
    file_new1 = str(file_new1:=os.path.join(testreport,lists[-1]))#取列表得最后一个值转换为字符串类型
    return file_new1
if __name__=='__main__':
    print(new_report(config.TEST_REPORT))
