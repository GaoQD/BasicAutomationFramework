'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-8-7 上午8:54
@Software: PyCharm Community Edition
@File    : test_hqProductCunguan.py
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

class test_hqProductCunguan(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()

    url = localReadConfig.get_string("url", 'hq_login_url')
    base_url = localReadConfig.get_string('base_url', 'hq_url')
    s = requests.session()

    def test_hq_product_cunguan(self):
        try:
            file_name = '..//testFile//product_cunguan.xls'
            start_num = 1
            end_num = 9
            prdIdList = []
            hq_product_cunguan_url = self.localReadConfig.get_string('url','hq_product_cunguan_url')
            # r = self.s.get(
            #     self.base_url + self.url,
            #     headers = json.loads(self.localReadConfig.get_string('data','headers')),
            #     cookies = json.loads(self.localReadConfig.get_string('data','cookies'))
            # )
            r = common.common.getLoginState(self.base_url + self.url)
            xlsList = common.common.get_excel(start_num,end_num,file_name)
            if xlsList != [] :
                for i in xlsList:
                    last_url = self.base_url + hq_product_cunguan_url + str(i['CaseData'])
                    r = self.s.get(last_url)
                    status_code = r.status_code
                    if 'invalid' not in r.text:
                        json_dict = json.loads(r.text)
                        if type(json_dict).__name__ == 'dict':
                            if json_dict['data'].get('list') != []:
                                for k in range(len(json_dict['data'].get('list'))):
                                    prdIdList.append(json_dict['data'].get('list')[k]['prd_id'])
                            # elif json_dict['data'].get('total') > 0:
                            #     for j in range(json_dict['data'].get('total')):
                            #         prdIdList.append(json_dict['data'].get('list')[j]['prd_id'])
                            prdIdList = sorted(set(prdIdList), key=prdIdList.index)
                            self.assertTrue(status_code == 200)
                            logs.Log.Log().getInstance(last_url + ' | GET | ' + str(status_code) + ' | return_code=' + str(json_dict['return_code']))
                            common.common.modify_excel(int(i['CaseNO']), 'PASS', file_name)
                        else:
                            logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
                            common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
                    else:
                        logs.Log.Log().getInstance(last_url + ' | ' + str(status_code))
                        common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
            else:
                logs.Log.Log().getInstance(hq_product_cunguan_url + ' | case not found!')
            return prdIdList
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))

    def tearDown(self):
        print("end test")
if __name__ == '__main__':
    unittest.main(warnings='ignore')