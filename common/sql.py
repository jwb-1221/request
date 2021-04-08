#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'


import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import configparser as cparser
from common import config
import pymysql
import json
# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()#读取配置文件（config.ini）的代码
cf.read(config.CONFIG,encoding='UTF-8')
host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
db_name = cf.get("mysqlconf","db_name")

class MYSQL():
    def mysql(self,sql):
        conn = pymysql.connect(host,user,password,db_name)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            conn.commit()
            res_list = cursor.fetchall()
            res = json.dumps(res_list, ensure_ascii=False)
            print(res)
        except:
            conn.rollback()
        return sql


