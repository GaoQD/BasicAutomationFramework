'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-9 上午10:58
@Software: PyCharm Community Edition
@File    : test_hqWithdraw.py
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


class test_hqWithdraw(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    '''
        提现接口
    '''
    def test_hq_withdraw(self):
        try:
            hq_withdraw_url = self.localReadConfig.get_string('url','hq_withdraw_url')
            last_url = self.base_url + hq_withdraw_url
            r = common.common.getLoginState(self.base_url + self.url)
            r = self.s.get(last_url,cookies = r.cookies)
            status_code = r.status_code
            json_dict = json.loads(r.text)
            if type(json_dict).__name__ == 'dict':
                self.assertTrue(status_code == 200)
                logs.Log.Log().getInstance(last_url + ' | GET | ' + str(status_code) + ' | ' + str(json_dict['return_msg']) + ' | ' + str(json_dict['data']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
        except Exception as ex :
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')