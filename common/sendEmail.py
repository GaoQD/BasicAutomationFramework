'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-7-25 下午4:26
@Software: PyCharm Community Edition
@File    : sendEmail.py
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time


def send_email(now_time):
    sender = 'cap4819@126.com'
    receivers = '1247651134@qq.com'
    passWord = 'gao367985'


    try:
        # content = 'python email 使用详情'
        # message = MIMEText(content,'plain','utf-8')
        # message['From'] = sender
        # message['To'] =receivers
        # message['Subject'] = '接口测试报告'
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receivers
        msg['Subject'] = '接口测试报告'
        htmlf = open('..//report//'+ now_time +'.html','rb')
        htmlcont = htmlf.read()
        email_text = MIMEText(htmlcont,'html','utf-8')
        msg.attach(email_text)
        sep = os.sep
        attname = '..//report//20180732143205.html'.split(sep)[-1]
        email_att = MIMEApplication(open('..//report//'+ now_time + '.html','rb').read())
        email_att.add_header('Content-Disposition','attachment',filename = attname)
        msg.attach(email_att)

        smtpObj = smtplib.SMTP('smtp.126.com',25)
        smtpObj.set_debuglevel(1)
        smtpObj.login(sender,passWord)
        smtpObj.sendmail('cap4819@126.com','1247651134@qq.com',msg.as_string())
        smtpObj.quit()
        print('邮件发送成功～')
    except Exception as ex:
        print("Error: 无法发送邮件",ex)
