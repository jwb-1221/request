#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os,sys,json
# from testCases.run import *
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class SendRequests():
    """发送请求数据"""
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            #发送请求
            re = s.request(method=method,url=url,headers=h,data=body,verify=v)
            return re
            print(re)
        except Exception as e:
            print(e)

if __name__=='__main__':
    SendRequests().sendRequests()