#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os,random
from common import config
def new_report(testreport):
    """获取最新HTML文件"""
    return str(file_new1:=os.path.join(testreport,lists:=os.listdir(testreport)[-1]))

def choice_report(testreport):
    """随机获取html文件"""
    return str(file:=os.path.join(testreport,file:=random.choice(lists:=os.listdir(testreport))))

if __name__=='__main__':
    print(new_report(config.TEST_REPORT))


