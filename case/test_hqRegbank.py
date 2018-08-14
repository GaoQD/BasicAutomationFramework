'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-9 下午1:50
@Software: PyCharm Community Edition
@File    : test_hqRegbank.py
'''
import unittest
import logs.Log
import common.common
import config.readConfig as readConfig
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import ssl

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)


class test_hqRegbank(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    '''
        支持银行及限额
    '''
    def test_hq_regbank(self):
        try:
            hq_regbank_url = self.localReadConfig.get_string('url','hq_regbank_url')
            last_url = self.base_url + hq_regbank_url
            r = common.common.getLoginState(self.base_url + self.url)
            r = self.s.get(last_url,cookies = r.cookies)
            json_dict = json.loads(r.text)
            status_code = r.status_code
            if 'status' in r.text:
                status = json_dict['status']
                if type(json_dict).__name__ == 'dict':
                    self.assertTrue(status == 0)
                    logs.Log.Log().getInstance(last_url + ' | GET | ' + str(status_code) + ' | ' + str(status))
                else:
                    logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
        except Exception as ex :
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')