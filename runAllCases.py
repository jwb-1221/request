#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from common import config,new_report,send_mail
def add_case(test_path=config.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*.py')
    return discover
def run_case(all_case,result_path=config.TEST_REPORT):
    title = "接口自动化测试报告"#html附件的标题
    now = time.strftime("%m-%d-%H")
    filename =  result_path + '/' + now + "时测试结果"+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title=title, description="用例执行情况")
    runner.run(all_case)
    fp.close()
    send_mail.SEND_MAIL().send_mail("2514095967@qq.com") #调用发送邮件模块
if __name__ == "__main__":
    cases = add_case()
    run_case(add_case())
