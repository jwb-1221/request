#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt,time
from common import read_excel,config,write_excel,login
from common.send_requests import *
from common import new_report,send_mail
if os.path.exists(config.TEST_RESULT):  # 如果文件存在
    os.remove(config.TEST_RESULT)
else:
    print("测试结果文件不存在")
if os.path.exists(config.TEST_TOKEN):  # 如果文件存在
    os.remove(config.TEST_TOKEN)
else:
    print("测试token文件不存在")
login.Login().adminlogin()
testDATA =read_excel.ReadExcel(config.TEST_TOKEN,"Sheet1").read_Excel()
@ddt.ddt
class API_demo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        login.Login().adminlogin()
    @ddt.data(*testDATA)
    def test_api(self,data):
        # login.Login().adminlogin()
        rowNum = int(data['ID'].split("_")[1])
        print("******* 正在执行第"+str(rowNum)+"条用例 ->{0} *********".format(data['模块']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'],data['url']))
        print("请求头信息: {0}".format(data['headers']))
        print("请求参数: {0}".format(data['body']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))
        # 发送请求
        re = SendRequests.sendRequests(self,self.s,data)
        print(re.json())
        try:
            re.json()["code"] == "0"
        except:#报错就执行
            write_excel.WriteExcel(config.TEST_RESULT).write_result(rowNum + 1, "fail")
        else:#不报错就执行
            write_excel.WriteExcel(config.TEST_RESULT).write_result(rowNum+1,"pass")
        finally:#无论报不报错都执行
            write_excel.WriteExcel(config.TEST_RESULT).write_name(rowNum + 1, "bin")
        # try:
        #     re.json()["status"] == "0"
        # except AttributeError as e:
        #     write_excel.WriteExcel(config.TEST_RESULT).write_data(rowNum+1,"fail")
        # else:
        #     write_excel.WriteExcel(config.TEST_RESULT).write_data(rowNum+1,"pass")
    def tearDown(self):
        pass

if __name__=='__main__':
    API_demo().test_api()
    send_mail.SEND_MAIL().send_mail('2514095967@qq.com')
