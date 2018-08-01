'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-7-31 下午3:36
@Software: PyCharm Community Edition
@File    : test_userSync.py
'''

import time
import HTMLTestRunner
import json
import unittest
import requests
import warnings
import ssl
import config.readConfig as readConfig
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logs.Log
import common.sendEmail
import common.common

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore',ResourceWarning)



class test_UserSync(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("start test")

    localReadConfig = readConfig.ReadConfig()


    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    cookies = {'session': '7980bbf83250446b9ef5a9dd75d77547', '__mt_client_id__': '1089867707',
               '__mt_access_token__': '5yu81gmA4qVUmhqgcSVcme9VRxXRlKu5iedStNoCufoPhuTWK3g2cAwtfUXJLgOpMZebQYtFZYSRuopM1MiY6ZEpEh9BOkgXZHLcOivaMAujgN5yRKOcx0N-PCQKl44Tnf047dnig1wOJhteM5MY2TuW0PQ6oGisAr1TIotYv_Q='}
    url = localReadConfig.get_string("url", 'user_sync_url')
    s = requests.session()

    # def test_user_sync(self):
    #    try:
    #        url = self.localReadConfig.get_string("url", 'user_sync_url')
    #        r = self.s.get('https://pre-licai-v2.meitu.com' + self.url,headers = self.headers,cookies = self.cookies)
    #        r.encoding = 'utf-8'
    #        json_dict = json.loads(r.text)
    #        status = str(json_dict['status'])
    #        status_code = str(r.status_code)
    #        if type(json_dict).__name__=='dict':
    #            if self.assertEqual(status,'0') != None :
    #                logs.Log.Log().getInstance(self.url + ' | GET | ' + status + ' | ' + status_code)
    #            else:
    #                logs.Log.Log().getInstance(self.url + ' | GET | ' + status + ' | ' + status_code)
    #        else:
    #            return
    #    except Exception as ex:
    #         print(ex)
    #
    # def test_xls(self):
    #     try:
    #         product_url = self.localReadConfig.get_string('url','product_url')
    #         file_name = '..//testFile//test.xls'
    #         start_num = 1
    #         end_num = 6
    #         id_list = []
    #         r = self.s.get('http://meitu-v2.test.congred.com' + self.url,headers = self.headers,cookies = self.cookies)
    #         for i in common.common.get_excel(start_num,end_num,file_name):
    #             last_url = 'http://meitu-v2.test.congred.com' + product_url + i['CaseData']
    #             r = self.s.get(last_url)
    #             r.encoding='utf-8'
    #             status_code = str(r.status_code)
    #             r = r.text
    #             if 'status' in r :
    #                 json_dict = json.loads(r)
    #                 id_total = json_dict['data'].get('total')
    #                 print(id_total)
    #                 if id_total > 1:
    #                     for j in range(id_total):
    #                         p_id = json_dict['data'].get('list')[j]['id']
    #                         id_list.append(p_id)
    #                     id_list = sorted(set(id_list), key=id_list.index)
    #                 else:
    #                     print(u'产品总数为0')
    #                 status = str(json_dict['status'])
    #                 if self.assertEqual(json_dict['status'], 0) != None :
    #                     logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #                 else:
    #                     logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']), 'PASS', file_name)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #                 common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #         return id_list
    #     except Exception as ex :
    #         print(ex)
    #
    #
    # def test_GetProductById(self):
    #     url = self.localReadConfig.get_string('url', 'product_by_id_url')
    #     for i in test_UserSync.test_xls(self):
    #         last_url = 'https://pre-licai-v2.meitu.com' + url + str(i)
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__=='dict':
    #            if self.assertEqual(status,'0') != None :
    #                logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #            else:
    #                logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #            return
    #
    # def test_profile(self):
    #     t_url = self.localReadConfig.get_string('url', 'profile_url')
    #     last_url = 'http://meitu-v2.test.congred.com' + t_url
    #     print(last_url)
    #     r = self.s.get('http://meitu-v2.test.congred.com/api/financial/user_sync', headers=self.headers, cookies=self.cookies)
    #     r = self.s.get('http://meitu-v2.test.congred.com/api/financial/profile')
    #     r.encoding = 'utf-8'
    #     json_dict = json.loads(r.text)
    #     print(json_dict)
    #     status = str(json_dict['status'])
    #     status_code = str(r.status_code)
    #     if type(json_dict).__name__ == 'dict':
    #         if self.assertEqual(status, '0') != None:
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #     else:
    #         return
    #
    # def test_risk(self):
    #     try:
    #         risk_url = self.localReadConfig.get_string('url','risk_url')
    #         last_url = 'http://meitu-v2.test.congred.com' + risk_url
    #         r = self.s.get('http://meitu-v2.test.congred.com' + self.url,headers = self.headers,cookies = self.cookies)
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(status, '0') != None:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex :
    #         print(ex)
    #
    # def test_account(self):
    #     try:
    #         account_url = self.localReadConfig.get_string('url','account_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + account_url
    #         r = self.s.get(self.localReadConfig.get_string('base_url','url') + self.url, headers = self.headers, cookies = self.cookies)
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(status,'0') != None :
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex:
    #         print(ex)
    #
    # #交易记录
    # def test_orders(self):
    #     try:
    #         orders_url = self.localReadConfig.get_string('url','orders_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + orders_url
    #         r = self.s.get(self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),headers = self.headers,cookies = self.cookies)
    #         file_name = '..//testFile//test.xls'
    #         start_num = 1
    #         end_num = 6
    #         for i in common.common.get_excel(start_num,end_num,file_name):
    #             r = self.s.get(last_url + i['CaseData'])
    #             json_dict = json.loads(r.text)
    #             status = str(json_dict['status'])
    #             status_code = str(r.status_code)
    #             r = r.text
    #             if 'status' in r :
    #                 json_dict = json.loads(r)
    #                 status = str(json_dict['status'])
    #                 if self.assertEqual(json_dict['status'], 0) != None :
    #                     logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #                 else:
    #                     logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']), 'PASS', file_name)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                 common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #     except Exception as ex :
    #         print(ex)
    #
    #
    # #买入记录
    # def test_orders_tender_record(self):
    #     try:
    #         orders_tender_record_url = self.localReadConfig.get_string('url','orders_tender_record_url')
    #         last_url = self.localReadConfig.get_string('base_url', 'url') + orders_tender_record_url
    #         r = self.s.get(
    #             self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         file_name = '..//testFile//test.xls'
    #         start_num = 1
    #         end_num = 6
    #         for i in common.common.get_excel(start_num,end_num,file_name):
    #             r = self.s.get(last_url + i['CaseData'])
    #             json_dict = json.loads(r.text)
    #             status = str(json_dict['status'])
    #             status_code = str(r.status_code)
    #             r = r.text
    #             if 'status' in r :
    #                 json_dict = json.loads(r)
    #                 status = str(json_dict['status'])
    #                 if self.assertEqual(json_dict['status'], 0) != None :
    #                     logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #                 else:
    #                     logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                     common.common.modify_excel(int(i['CaseNO']), 'PASS', file_name)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + str(i['CaseData']) + ' | GET | ' + status + ' | ' + status_code)
    #                 common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #     except Exception as ex :
    #         print(ex)
    #
    # def test_query_bank_card_url(self):
    #     try:
    #         query_bank_card_url = self.localReadConfig.get_string('url','query_bank_card_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + str(query_bank_card_url)
    #         r = self.s.get(self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),headers = self.headers,cookies = self.cookies)
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(json_dict['status'],'0') != None:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex :
    #         print(ex)
    # #实名认证
    # def test_id_validate(self):
    #     id_validate_url = self.localReadConfig.get_string('url','id_validate_url')
    #     last_url = self.localReadConfig.get_string('base_url','url') + id_validate_url
    #     r = self.s.get(
    #         self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),
    #         headers = self.headers,
    #         cookies = self.cookies
    #     )
    #     r = self.s.post(last_url,json={"id_name":"王嘉宝","id_card":"230103198409133743","mobile":"18210262865"})
    #     json_dict = json.loads(r.text)
    #     print(json_dict)
    #
    # def test_query_risk_subject(self):
    #     try:
    #         query_risk_url = self.localReadConfig.get_string('url','query_risk_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + query_risk_url
    #         r = self.s.get(
    #             self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(status,'0') != None:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex:
    #         print(ex)
    #
    # def test_couponlist(self):
    #     try:
    #         couponlist_url = self.localReadConfig.get_string('url','couponlist_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + couponlist_url
    #         r = self.s.get(
    #             self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','user_sync_url'),
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(status,'0') != None :
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex:
    #         print(ex)


    # def test_risk_flow(self):
    #     try:
    #         risk_flow_url = self.localReadConfig.get_string('url','risk_flow_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + risk_flow_url
    #         r = self.s.get(
    #             self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string("url", 'user_sync_url'),
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status = str(json_dict['status'])
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             if self.assertEqual(status,'0') != None:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex:
    #         print(ex)

    # def test_common_problem(self):
    #     try:
    #         common_problem_url = self.localReadConfig.get_string('url','common_problem_url')
    #         last_url = self.localReadConfig.get_string('base_url','url') + common_problem_url
    #         r = self.s.get(
    #             self.localReadConfig.get_string('base_url','url') + self.localReadConfig.get_string('url','common_problem_url'),
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         print(json_dict)
    #         if type(json_dict).__name__ == 'dict':
    #             status = str(json_dict['status'])
    #             status_code = str(r.status_code)
    #             if self.assertEqual(status,'0') != None:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status + ' | ' + status_code)
    #         else:
    #             return
    #     except Exception as ex :
    #         print(ex)

    def test_counponlist_unavailable(self):
        counponlist_un_url = self.localReadConfig.get_string('url','counponlist_un_url')
        

    def tearDown(self):
        print("end start")

if __name__ == '__main__':
    unittest.main()
    # now_time = time.strftime("%Y%m%M%H%M%S", time.localtime(time.time()))
    # suite = unittest.TestSuite()
    # suite.addTest(test_UserSync('test_GetProductById'))
    # fp = open('..//report//' + now_time + '.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='Test MeiTu',
    #     description='Test Case Run Result')
    # runner.run(suite)
    # common.sendEmail.send_email(now_time)
