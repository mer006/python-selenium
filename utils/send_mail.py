#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import zmail
from config.conf import cm

def send_report():
    '''发送报告'''
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    
    try:
        mail = {
            'from': 'lxl1@test.net',
            'subject': '**项目自动化测试报告',
            'content_html': content_html,
            'attachments': [cm.REPORT_FILE, ]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESS, mail)
        print("邮件发送成功")
    except Exception as e:
        print("Error,无法发送邮件,{}!".format(e))