'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-9 下午2:24
@Software: PyCharm Community Edition
@File    : test_hqTotalAssets.py
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


class test_hqTotalAssets(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    '''
        总资产
    '''
    def test_hq_total_assets(self):
        try:
            hq_total_assets_url = self.localReadConfig.get_string('url','hq_total_assets_url')
            last_url = self.base_url + hq_total_assets_url
            r = common.common.getLoginState(self.base_url + self.url)
            r = self.s.get(last_url,cookies = r.cookies)
            status_code = r.status_code
            json_dict = json.loads(r.text)
            if type(json_dict).__name__ == 'dict':
                self.assertTrue(status_code == 200)
                logs.Log.Log().getInstance(last_url + ' | GET | ' + str(status_code) + ' | ' + str(json_dict['return_msg']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
        except Exception as ex :
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")
if __name__ == '__main__':
    unittest.main(warnings='ignore')