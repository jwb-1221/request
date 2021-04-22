#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import config
import xlrd

class ReadExcel():
    """读取excel文件数据"""
    def __init__(self,fileName, SheetName="Sheet1"):
        "fileName是读取Excel文件的路径\
         SheetName是读取的第一个sheet"

        self.data = xlrd.open_workbook(fileName)
        #打开指定的Excel表格
        self.table = self.data.sheet_by_name(SheetName)
        #打开指定的sheet

        # 获取总行数、总列数
        self.nrows = self.table.nrows
        print("一共有"+str(self.nrows-1)+"条用例")
        #第一个sheet获取的行数赋予nrows
        self.ncols = self.table.ncols
        #第一个sheet获取的列数赋予ncols
    def read_Excel(self):
        """读取表格数据"""
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            # 获取第一行做为keys值
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            # for col in range(1,self.nrows):
            for col in range(1, 2):
                #1：表示的是从第几行开始执行
                #self.norws:表示的是到第几行
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
            # return (self.nrows[URl])
        else:
            print("表格是空数据!")
# if __name__=='__main__':
#     print(ReadExcel(config.TEST_CONFIG).read_Excel())

