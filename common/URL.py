#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

def adminurl(api):
    "运营端地址"
    adminurl = "http://account-admin-webos-test.lastmiles.cn/account-admin-web/"+api
    return adminurl
def merchanturl(api):
    """商户端地址"""
    merchanturl = "http://account-merchant-webos-test.lastmiles.cn/account-merchant-web/"+api
    return merchanturl