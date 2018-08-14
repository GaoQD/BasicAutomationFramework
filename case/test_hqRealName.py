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


    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()


    '''
        实名认证
    '''
    def test_hq_real_name(self):
        try:
            start_num = 1
            end_num = 6
            file_name = '..//testFile//real_name.xls'
            hq_real_name_url = self.localReadConfig.get_string('url','hq_real_name_url')
            last_url = self.base_url +  hq_real_name_url
            '''
                获取session信息
            '''
            r = common.common.getLoginState(self.base_url + self.url)
            xlsList = common.common.get_excel(start_num, end_num, file_name)
            if xlsList != []:
                for i in xlsList:
                    r = self.s.post(last_url,json=json.loads(i["CaseData"]),cookies = r.cookies)
                    json_dict = json.loads(r.text)
                    status_code = str(r.status_code)
                    if type(json_dict).__name__ == 'dict':
                        logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(json_dict['return_msg']))
                    else:
                        logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + str(r.text))
            else:
                logs.Log.Log().getInstance(last_url + ' | not found case')
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore')