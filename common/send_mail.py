# !/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import yagmail,os,time
from common import config,new_report
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
con = configparser.ConfigParser()
con.read(config.CONFIG, encoding='utf-8')
USER = con.get("user","user")
PASSWORD = con.get("user","password")
SUBJECT = con.get("user","subject")
class SEND_MAIL():
    def send_mail(self,TO,):
        f = open(new_report.new_report(config.TEST_REPORT), 'rb')
        user = USER  # 发送邮箱的账号，config.ini有配置
        password = PASSWORD  # 发送邮箱的密码，config.ini有配置
        text = "斌"#输入的文本信息
        file = new_report.new_report(config.TEST_REPORT)#调用获取html附件的函数
        yag = yagmail.SMTP(user=user,password=password,host="smtp.163.com",port=465)
        to = TO#收件人邮件
        subject = SUBJECT#主题
        contents = [
            text,file
        ]
        yag.send(to=to, subject=subject, contents=contents)
        print('邮件发送成功')
if __name__=="__main__":
    SEND_MAIL().send_mail('2514095967@qq.com')