'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-7 下午2:23
@Software: PyCharm Community Edition
@File    : test_hqPurchaseOrder.py
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


class test_hqPurchaseOrder(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    def test_hq_purchase_order(self):
        try:
            hq_purchase_order_url = self.localReadConfig.get_string('url','hq_purchase_order_url')
            last_url = self.base_url + hq_purchase_order_url
            r = self.s.get(
                self.base_url + self.url,
                headers = json.loads(self.localReadConfig.get_string('data','headers')),
                cookies = json.loads(self.localReadConfig.get_string('data','cookies'))
            )
            jsonData = {"prd_id":"170712110124850","amount": "111.00", "user_continue": "B03"}
            r = self.s.post(last_url,json=jsonData)
            json_dict = json.loads(r.text)
            status_code = r.status_code
            if type(json_dict).__name__ == 'dict':
                self.assertTrue(status_code == 200)
                logs.Log.Log().getInstance(last_url + ' | POST | ' + str(status_code) + ' | ' + str(json_dict['return_msg']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")
if __name__ == '__main__':
    unittest.main()