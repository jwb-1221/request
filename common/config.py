#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

import os,sys
#config是返回本文件的父目录的父目录
config = os.path.dirname(os.path.dirname(__file__))
#sys.path.append（引用模块的地址）
sys.path.append(config)

#配置
CONFIG = os.path.join(config,"config","config.ini")
#测试用例模板
TEST_CONFIG = os.path.join(config,"config","testcase.xlsx")
#测试用例写入token模板
TEST_TOKEN = os.path.join(config,"config","token.xlsx")
#测试用例结果模板
TEST_RESULT = os.path.join(config,"config","测试结果表格.xlsx")
#html测试报告文件
TEST_HTML = os.path.join(config,"reports","2021-03-01.html")
#测试报告
TEST_REPORT = os.path.join(config,"reports")
# 测试用例程序文件
TEST_CASE = os.path.join(config,"testCases")