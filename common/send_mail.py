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
    def send_mail(self,TO):
        user = USER  # 发送邮箱的账号
        password = PASSWORD  # 发送邮箱的密码
        sendfile = open(new_report.new_report(config.TEST_REPORT), 'wb').read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", new_report.new_report(config.TEST_REPORT)))
            # host 和 port网上很容易百度出来
        yag = yagmail.SMTP(user=user,password=password,host="smtp.163.com",port=465)
        # 收件人的邮箱
        to = TO
            # 主题
        subject = SUBJECT
            # 如果contents列表里面的类容是具体的一个图片或一个word文档等的路径会以附件的方式发送
        contents = [
            "斌"
        ]
        # time.sleep(2)
        yag.send(to=to, subject=subject, contents=contents)
        print('邮件发送成功')
if __name__=="__main__":
    SEND_MAIL().send_mail('2514095967@qq.com',report1=new_report.new_report(config.TEST_REPORT))