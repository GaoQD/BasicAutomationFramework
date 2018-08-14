'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-7 上午10:38
@Software: PyCharm Community Edition
@File    : test_hqTransactionRecord.py
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

class test_hqTransactionRecord(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    '''
        交易记录
    '''
    def test_hq_transaction_record(self):
        try:
            file_name = '..//testFile//transaction_record.xls'
            start_num = 1
            end_num = 9
            hq_transaction_record_url = self.localReadConfig.get_string('url','hq_transaction_record_url')
            last_url = self.base_url + hq_transaction_record_url
            r = common.common.getLoginState(self.base_url + self.url)
            xlsList = common.common.get_excel(start_num, end_num, file_name)
            if xlsList != []:
                for i in xlsList :
                    r = self.s.get(last_url + i['CaseData'],cookies = r.cookies)
                    status_code = r.status_code
                    if 'Error' not in r.text :
                        json_dict = json.loads(r.text)
                        if type(json_dict).__name__ == 'dict':
                            self.assertTrue(status_code == 200)
                            logs.Log.Log().getInstance(last_url + i['CaseData'] + ' | GET | ' + str(status_code) + ' | ' + str(json_dict['return_code']))
                            common.common.modify_excel(int(i['CaseNO']),'PASS',file_name)
                        else:
                            logs.Log.Log().getInstance(last_url + i['CaseData'] + ' | ' + str(status_code))
                            common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
                    else:
                        logs.Log.Log().getInstance(last_url + i['CaseData'] + ' | ' + str(status_code))
                        common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
            else:
                logs.Log.Log().getInstance(last_url + ' | case not found')
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')