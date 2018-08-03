'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-7-25 下午3:57
@Software: PyCharm Community Edition
@File    : run_All_Case.py
'''

import unittest
import time
import HTMLTestRunner
import common.common


if __name__ == '__main__':
    now_time = time.strftime("%Y%m%M%H%M%S", time.localtime(time.time()))
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('.','test_*.py')
    for case in all_cases:
        suite.addTest(case)
    fp = open('..//report//' + now_time + '.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Test MeiTu',
        description='Test Case Run Result')
    runner.run(suite)
    common.sendEmail.send_email(now_time)