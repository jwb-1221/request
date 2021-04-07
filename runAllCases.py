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
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
    return discover
def run_case(all_case,result_path=config.TEST_REPORT):
    """执行所有的测试用例"""
    # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename =  result_path + '/' + now + '.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title="云账户测试报告", description="用例执行情况")
    runner.run(all_case)
    fp.close()
    report = new_report.new_report(config.TEST_REPORT) #调用模块生成最新的报告
    send_mail.SEND_MAIL().send_mail("2514095967@qq.com",report) #调用发送邮件模块
if __name__ == "__main__":
    cases = add_case()
    run_case(add_case())