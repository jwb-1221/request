from common import config,new_report,send_mail
import requests
# aa = new_report.new_report(config.TEST_REPORT)
# print(aa.replace("\\", "/"))
# send_mail.SEND_MAIL().send_mail('2514095967@qq.com',report=aa.replace("\\", "/"))
# to = input("请输入要发送的邮箱(目前只能输入一个)：")
#
# send_mail.SEND_MAIL().send_mail(TO=to)

def ceshi():
    url = "http://account-admin-webos-test.lastmiles.cn/account-admin-web/taxRecord/statisticsTaxRecord"
    h = {"Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJkYXRhIjp7ImZkZFRlbXBsYXRlSWQiOiJYWUZERDY3NzYwMzI2NTc1MzEyMzYzNTIiLCJpc1VwZGF0ZVB3ZCI6MCwibG9naW5UeXBlIjowLCJ1c2VyTG9naW5JZCI6NjU5Mzc0NjkwMTM1MzA4Mjg4MywibWVyY2hhbnRJZCI6IiIsInRhc2tVcmwiOiJodHRwczovL2Nkbi5sYXN0bWlsZXMuY24vYXBwcy82NzIyODEyMjM3NzQzNTk5NjE2LnBkZiIsInN5c05hbWUiOiLns7vnu5_mk43kvZzmiYvlhowtVjEuMCIsImlzTWFuYWdlciI6MSwiaXNBc3luY1JlcXVlc3QiOiJ0cnVlIiwic3lzVXJsIjoiaHR0cHM6Ly9jZG4ubGFzdG1pbGVzLmNuL2FwcHMvNjcyMjgxMTU2OTM5ODAzNDQzMi5wZGYiLCJ0YXNrTmFtZSI6IuWFheWAvOS7o-WPkeaTjeS9nOaJi-WGjC1WMS4wIiwibWVyY2hhbnRSYW5nZSI6MSwidXNlcm5hbWUiOiJBRE1pbiJ9LCJzdWIiOiI2NTkzNzQ2OTAxMzUzMDgyODgzIiwiZXhwIjoxNjIxMzA5Mzc0fQ.E2l6XWs2cQ2_cyZiHXyZaprk0IxGHw4sAP3NRXVql4Ds5UfAfCOyRqfLBAQOkL_1K148uHjIgXFTVOwkpoHdOA"}
    body = {"tartDate":"2020-12","endDate":"2020-12","merchantId":"","taxpayer":"","status":"0","type":"3","businessNo":"","amountRangeJson":"[]"}
    s = requests.session()
    v = False
    re = s.request(method="POST",url=url,headers=h,data=body,verify=v)
    print(re.json())
ceshi()
