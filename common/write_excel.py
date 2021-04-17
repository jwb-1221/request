#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import config
#导入复制文件模块
import shutil
from openpyxl import load_workbook
#styles:样式，font：字体，Alignment：对齐 阵营 对准
from openpyxl.styles import Font,Alignment,colors
import configparser as cparser
# --------- 读取config.ini配置文件 ---------------
# cf = cparser.ConfigParser()
# cf.read(config.TEST_RESULT,encoding='UTF-8')
# name = cf.get("tester","name")

cf = cparser.ConfigParser()
cf.read(config.CONFIG,encoding='utf-8')
name = cf.get("tester","name")

class WriteExcel():
    """文件写入数据"""
    def __init__(self,fileName):
        self.filename = fileName
        if not os.path.exists(self.filename):
            # 文件不存在，则拷贝模板文件至指定报告目录下
            shutil.copyfile(config.TEST_TOKEN,config.TEST_RESULT)
        self.wb = load_workbook(self.filename)
        self.ws = self.wb.active

    def write_data(self,row_n,value):
        """
        写入测试结果
        :param row_n:数据所在行数
        :param value: 测试结果值
        :return: 无
        """
        font_RED = Font(name='宋体', color='FF0000', bold=True)
        font_GREEN = Font(name='宋体', color='00ff00', bold=True)
        font_purple = Font(name='宋体', color='9900cc', bold=True)
        align = Alignment(horizontal='center', vertical='center')
        # 获数所在行数
        L_n = "L" + str(row_n)
        M_n = "M" + str(row_n)
        if value == "pass":
            self.ws.cell(row_n, 8, value).font = font_GREEN
        elif value == "fail":
            self.ws.cell(row_n, 8, value).font = font_RED
        elif value != "pass" or "fail":
            self.ws.cell(row_n, 9, value).font = font_purple  # 写入接口返回结果
        self.ws.cell(row_n,10, name).font = font_purple#写入测试员
        self.ws[L_n].alignment = align
        self.ws[M_n].alignment = align
        self.wb.save(self.filename)
# if __name__=='__main__':
#     WriteExcel(config.TEST_RESULT).write_data(5,'FAIL')
