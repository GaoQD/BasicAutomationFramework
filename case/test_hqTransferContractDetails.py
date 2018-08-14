'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-9 上午10:13
@Software: PyCharm Community Edition
@File    : test_hqTransferContractDetails.py
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


class test_hqTransferContractDetails(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    '''
        玖富债权展示
    '''
    def test_hq_transfer_contract_details(self):
        try:
            hq_transfer_contract_details_url = self.localReadConfig.get_string('url','hq_transfer_contract_details_url')
            last_url = self.base_url + hq_transfer_contract_details_url
            r = common.common.getLoginState(self.base_url + self.url)
            jsonData = {"order_no":"HQ2018071511371679814032"}
            r = self.s.post(last_url,json=jsonData,cookies = r.cookies)
            status_code = r.status_code
            json_dict = json.loads(r.text)
            if type(json_dict).__name__ == 'dict':
                self.assertTrue(status_code == 200)
                logs.Log.Log().getInstance(last_url + ' | POST | ' + str(status_code) + ' | ' + str(json_dict['return_msg']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
        except Exception as ex :
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')