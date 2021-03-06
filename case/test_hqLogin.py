'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-6 下午3:47
@Software: PyCharm Community Edition
@File    : test_hqLogin.py
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

class test_hqLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()


    '''
        登录接口
    '''
    def test_hq_login(self):
        try:
            last_url = self.base_url + self.url
            r = self.s.post(
                last_url,
                # json={"mobile":"19994334819","password":"eQ/qLSlDIuLT44ieOUz/E2/6czAkzmbYxLl6hDhlILa73kAzdTil87Y5m0hsKsh9GpcT/JM8kUVHTBMP9l3nEZoZROFRDlIcDbD2DQS5hgw6AZ9ehYcnPuqoNiYDqt0lfdt5DG0je2Snzoa6/+hbgXo63X5uumDTGlsuX4W9bMw=","type":"password"}
                json={"mobile": "18298380158","password":"NUprIrkuaVgHAz9kGs+FqWy8gmNSA0wVRb96kpN1wzc+KOhTCiE5zaMXwsAeIRXN/9RAkl+IczVnVABAR0bjmK8Fr+Mw/TW4tsnKHGiIzsLboyAljFezroUEz0OusD+T0wO5/G3gVX9H5eJ8hXH40aP6zeYV90HArEfUcYx03J4=","type":"password"}
            )
            status_code = str(r.status_code)
            if 'status' in r.text:
                json_dict = json.loads(r.text)

                status = json_dict['status']
                if type(json_dict).__name__ == 'dict':
                    logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(json_dict['data']))
                else:
                    logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + str(r.text))
            else:
                logs.Log.Log().getInstance(last_url + ' | ' + status_code)
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')