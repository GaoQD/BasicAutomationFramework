'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-7-25 上午11:08
@Software: PyCharm Community Edition
@File    : test1.py
'''
import unittest
import time
import HTMLTestRunner
import logs.Log
import common.sendEmail


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("测试开始")


    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
        lname = 'api/financial/product/'
        logs.Log.Log().getInstance(lname)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.isupper())

    def test_split(self):
        s = 'hello word'
        self.assertEqual(s.split(),['hello','word'])
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSequenceFunctions('test_upper'))
    suite.addTest(TestSequenceFunctions('test_isupper'))
    suite.addTest(TestSequenceFunctions('test_split'))
    fp = open('..//report//' + time.strftime("%Y%m%M%H%M%S",time.localtime(time.time())) + '.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Test Result',
        description = 'Test Case Run Result')
    runner.run(suite)
    common.sendEmail.send_email()
    fp.close()
