#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

import os
from common import config
def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    file_new = os.path.join(testreport,lists[-1])
    # print(file_new)
    file_new1 = 'r"' + file_new + '"'
    # print(file_new1)
    # file_new1
    # aa = file_new1.replace("\\", "/")
    # return aa
    return file_new1


if __name__=='__main__':
    # new_report(config.TEST_REPORT)
    print(new_report(config.TEST_REPORT))