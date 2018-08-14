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


    '''
        产品详情
    '''
    def test_hq_product_record(self):
        try:
            start_num = 1
            end_num = 10
            file_name = '..//testFile//product_record.xls'
            hqOrderNOList = []
            hq_product_record_url = self.localReadConfig.get_string('url','hq_product_record_url')
            last_url = self.base_url + hq_product_record_url
            # r = self.s.get(
            #     self.base_url + self.url,
            #     headers = json.loads(self.localReadConfig.get_string('data','headers')),
            #     cookies = json.loads(self.localReadConfig.get_string('data','cookies'))
            # )
            r = common.common.getLoginState(self.base_url + self.url)
            prdIdList = test_hqProductCunguan.test_hq_product_cunguan(self)
            xlsList = common.common.get_excel(start_num, end_num, file_name)
            if prdIdList != [] and xlsList != []:
                for i in xlsList:
                    for prd_id in prdIdList :
                        url = last_url + i['CaseData'] + '&prd_id=' + prd_id
                        r = self.s.get(url)
                        status_code = r.status_code
                        if 'Error' not in r.text:
                            json_dict = json.loads(r.text)
                            if type(json_dict).__name__ == 'dict':
                                if json_dict['data'].get('list') != []:
                                    for k in range(len(json_dict['data'].get('list'))):
                                        hqOrderNOList.append(json_dict['data'].get('list')[k]['order_no'])
                                # elif json_dict['data'].get('total') > 0 :
                                #     for j in range(json_dict['data'].get('total')):
                                #         hqOrderNOList.append(json_dict['data'].get('list')[j]['order_no'])
                                    hqOrderNOList = sorted(set(hqOrderNOList), key=hqOrderNOList.index)
                                    self.assertTrue(status_code == 200)
                                    logs.Log.Log().getInstance(last_url + i['CaseData'] + '&prd_id=' + prd_id + ' | GET | ' + str(status_code) + ' | return_code = ' + str(json_dict['return_code']))
                                    common.common.modify_excel(int(i['CaseNO']),'PASS',file_name)
                                else:
                                    logs.Log.Log().getInstance(last_url + i['CaseData'] + '&prd_id=' + prd_id + ' | ' + 'return order_no is null')
                                    common.common.modify_excel(int(i['CaseNO']),'PASS',file_name)
                            else:
                                logs.Log.Log().getInstance(last_url + i['CaseData'] + '&prd_id=' + prd_id + ' | ' + str(status_code))
                                common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
                        else:
                            logs.Log.Log().getInstance(last_url + i['CaseData'] + '&prd_id=' + prd_id + ' | ' + str(status_code))
                            common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
            else:
                logs.Log.Log().getInstance(last_url + ' | not found case and prd_id is null')
            return hqOrderNOList
        except Exception as ex:
            logs.Log.Log().getInstance(str(ex))


    def tearDown(self):
        print("end test")

if __name__ == '__main__':
    unittest.main(warnings='ignore')