#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import requests
from common import login
from common.URL import *
def selectTaxpayerPage():#纳税人列表
    url = adminurl("taxpayer/selectTaxpayerPage")
    headers = \
        {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization":login.Login().adminlogin()}

    d = \
        {
        "ageNum":"1",
        "pageSize":"15",
        "browseMode":"2",
        "merchantName":"",
        "taxpayerCondition":"",
        "startDate":"",
        "endDate":"",
        "status":"",
        "authStatus":"",
        "signStatus":""
    }
    s = requests.session()
    r = s.post(url, headers=headers, data=d)
    print(r.json()["data"]["token"])
