'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-7 下午1:57
@Software: PyCharm Community Edition
@File    : test_hqCommonProblem.py
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

class test_hqCommonProblem(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    def test_hq_common_problem(self):
        try:
            start_num = 1
            end_num = 5
            file_name = '..//testFile//common_problem.xls'
            hq_common_problem_url = self.localReadConfig.get_string('url','hq_common_problem_url')
            last_url = self.base_url + hq_common_problem_url
            r = self.s.get(
                self.base_url + self.url,
                headers = json.loads(self.localReadConfig.get_string('data','headers')),
                cookies = json.loads(self.localReadConfig.get_string('data','cookies'))
            )
            xlsList = common.common.get_excel(start_num, end_num, file_name)
            if xlsList != [] :
                for i in xlsList :
                    r = self.s.get(last_url + i['CaseData'])
                    json_dict = json.loads(r.text)
                    status_code = r.status_code
                    if type(json_dict).__name__ == 'dict':
                        self.assertTrue(status_code == 200)
                        logs.Log.Log().getInstance(last_url + i['CaseData'] + ' | GET | ' + str(status_code) + ' | return_code = ' + str(json_dict['return_code']))
                        common.common.modify_excel(int(i['CaseNO']),'PASS',file_name)
                    else:
                        logs.Log.Log().getInstance(last_url + i['CaseData'] + ' | ' + str(status_code))
                        common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
            else:
                logs.Log.Log().getInstance(last_url + ' | not found case')
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")
if __name__ == '__main__':
    unittest.main()