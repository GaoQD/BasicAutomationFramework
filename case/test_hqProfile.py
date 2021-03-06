'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-6 下午3:40
@Software: PyCharm Community Edition
@File    : test_hqProfile.py
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
warnings.simplefilter('ignore',ResourceWarning)

class test_hqProfile(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    cookies = {'session': 'b39c525e282a41d59cc27eded1d3f18a'}
    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()



    '''
        个人中心
    '''
    def test_hq_profile(self):
        try:
            hq_profile_url = self.localReadConfig.get_string('url','hq_profile_url')
            last_url = self.base_url + hq_profile_url
            r = common.common.getLoginState(self.base_url + self.url)
            r = self.s.get(last_url,cookies = r.cookies)
            status_code = str(r.status_code)
            json_dict = json.loads(r.text)
            if type(json_dict).__name__ == 'dict':
                logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(json_dict['return_msg']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' +  str(r.text))
        except Exception as ex :
            logs.Log.Log().getInstance(str(ex))
    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')