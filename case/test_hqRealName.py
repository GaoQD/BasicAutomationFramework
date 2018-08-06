'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-6 下午4:37
@Software: PyCharm Community Edition
@File    : test_hqRealName.py
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

class test_hqRealName(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    cookies = {'session': 'b39c525e282a41d59cc27eded1d3f18a'}
    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    def test_hq_real_name(self):
        try:
            hq_real_name_url = self.localReadConfig.get_string('url','hq_real_name_url')
            last_url = self.base_url +  hq_real_name_url
            r = self.s.get(
                self.base_url + self.url,
                headers = self.headers,
                cookies = self.cookies
            )
            r = self.s.post(last_url,json={"id_name": "高强德","id_card": "620421199107176437"})
            json_dict = json.loads(r.text)
            status_code = str(r.status_code)
            if type(json_dict).__name__ == 'dict':
                logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(json_dict['return_msg']))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + str(r.text))
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

