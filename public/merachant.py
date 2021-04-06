#!/usr/bin/env python
# coding=utf-8
import requests
from common import login
from common.URL import *
from common.sql import *
from testCases.run import *
url = merchanturl("taxpayer/selectTaxpayerPage")
headers = \
    {
        "Content-Type": "application/x-www-form-urlencoded",

        "Authorization": login.Login().merchantlogin()
    }
body = \
    {
        "ageNum": "1",
        "pageSize": "15",
        "browseMode": "2",
        "merchantName": "",
        "taxpayerCondition": "",
        "startDate": "",
        "endDate": "",
        "status": "",
        "authStatus": "",
        "signStatus": ""
    }
s = requests.session()
r = s.post(url, headers=headers, data=body)
print(r.json()["data"])
sql = "SELECT id,user_name FROM tb_user_app WHERE user_name = '' or certificate_no = '' or phone = '15818468674';"
print(MYSQL().mysql(sql))

