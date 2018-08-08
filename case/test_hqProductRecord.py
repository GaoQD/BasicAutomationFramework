'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-7 上午9:59
@Software: PyCharm Community Edition
@File    : test_hqProductRecord.py
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
from case.test_hqProductCunguan import test_hqProductCunguan

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore',ResourceWarning)

class test_hqProductRecord(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    def test_hq_product_record(self):
        try:
            hqOrderNOList = []
            hq_product_record_url = self.localReadConfig.get_string('url','hq_product_record_url')
            last_url = self.base_url + hq_product_record_url
            r = self.s.get(
                self.base_url + self.url,
                headers = json.loads(self.localReadConfig.get_string('data','headers')),
                cookies = json.loads(self.localReadConfig.get_string('data','cookies'))
            )
            prdIdList = test_hqProductCunguan.test_hq_product_cunguan(self)
            print(prdIdList)
            if prdIdList != []:
                for prd_id in prdIdList:
                    r = self.s.get(last_url + prd_id)
                    json_dict = json.loads(r.text)
                    status_code = r.status_code
                    if type(json_dict).__name__ == 'dict':
                        if json_dict['data'].get('total') > 0 :
                            for i in range(json_dict['data'].get('total')):
                                hqOrderNOList.append(json_dict['data'].get('list')[i]['order_no'])
                            self.assertTrue(status_code == 200)
                            logs.Log.Log().getInstance(last_url + prd_id + ' | GET | ' + str(status_code) + ' | return_code = ' + str(json_dict['return_code']))
                        else:
                            logs.Log.Log().getInstance(last_url + prd_id + ' | ' + 'return order_no is null')
                    else:
                        logs.Log.Log().getInstance(last_url + prd_id + ' | ' + str(status_code))
            else:
                logs.Log.Log().getInstance(last_url + ' | prd_id is null')
            return hqOrderNOList
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main()