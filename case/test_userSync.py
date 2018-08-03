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
    cookies = {'session': 'ce95395f3936432c83af5a41d1a8fb34', '__mt_client_id__': '1089867707',
               '__mt_access_token__': 'aI2-C4liGBugQDXmq691O4GPgAGXo7DuxA1VgRf6Z7qC2_0ODreyW4Szdz77-yAnu-vC9rJu95c6eQZgb-0Lf2dSyLsCqqGgjYMahp-U_vjOFn80zuxkUp9bKpNfIRmZxkyDI1GRiH-dW4Z7tp207bXI6izG6auOlPWKFjosfdY='}
    url = localReadConfig.get_string("url", 'user_sync_url')
    base_url = localReadConfig.get_string('base_url','url')
    s = requests.session()

    # def test_user_sync(self):
    #    try:
    #        last_url = self.base_url + self.url
    #        r = self.s.get(
    #            last_url,
    #            headers = self.headers,
    #            cookies = self.cookies
    #        )
    #        r.encoding = 'utf-8'
    #        json_dict = json.loads(r.text)
    #        status_code = str(r.status_code)
    #        if type(json_dict).__name__=='dict':
    #            status = json_dict['status']
    #            self.assertTrue(status in (0,1))
    #            logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #        else:
    #            logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #    except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_xls(self):
    #     try:
    #         product_url = self.localReadConfig.get_string('url','product_url')
    #         file_name = '..//testFile//test.xls'
    #         start_num = 1
    #         end_num = 6
    #         id_list = []
    #         productIdList = []
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         for i in common.common.get_excel(start_num,end_num,file_name):
    #             last_url = self.base_url + product_url + i['CaseData']
    #             r = self.s.get(last_url)
    #             r.encoding='utf-8'
    #             status_code = str(r.status_code)
    #             r = r.text
    #             if 'status' in r :
    #                 json_dict = json.loads(r)
    #                 id_total = json_dict['data'].get('total')
    #                 if id_total > 1:
    #                     for j in range(id_total):
    #                         p_id = json_dict['data'].get('list')[j]['id']
    #                         product_id = json_dict['data'].get('list')[j]['prdid']
    #                         id_list.append(p_id)
    #                         productIdList.append(product_id)
    #                     id_list = sorted(set(id_list), key=id_list.index)
    #
    #                 status = json_dict['status']
    #                 self.assertTrue(status in (0, 1))
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #                 common.common.modify_excel(int(i['CaseNO']), 'FAIL', file_name)
    #             else:
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #                 common.common.modify_excel(int(i['CaseNO']),'FAIL',file_name)
    #         return id_list,productIdList
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    #
    # def test_GetProductById(self):
    #     try:
    #         product_by_id_url = self.localReadConfig.get_string('url', 'product_by_id_url')
    #         for i in test_UserSync.test_xls(self):
    #             last_url = self.base_url + product_by_id_url + str(i)
    #             r = self.s.get(last_url)
    #             json_dict = json.loads(r.text)
    #             status = json_dict['status']
    #             status_code = str(r.status_code)
    #             if type(json_dict).__name__=='dict':
    #                 self.assertTrue(status in (0, 1))
    #                 logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #             else:
    #                logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_profile(self):
    #     try:
    #         profile_url = self.localReadConfig.get_string('url', 'profile_url')
    #         last_url = self.base_url + profile_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers=self.headers,
    #             cookies=self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         r.encoding = 'utf-8'
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_risk(self):
    #     try:
    #         risk_url = self.localReadConfig.get_string('url','risk_url')
    #         last_url = self.base_url + risk_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(ex)
    #
    # ###账户总览
    # def test_account(self):
    #     try:
    #         account_url = self.localReadConfig.get_string('url','account_url')
    #         last_url = self.base_url + account_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status) + ' | ' + str(json_dict['data']))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #交易记录
    # def test_orders(self):
    #     try:
    #         orders_url = self.localReadConfig.get_string('url','orders_url')
    #         last_url = self.base_url + orders_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         for pid in test_UserSync.test_xls(self)[1]:
    #             r = self.s.get(last_url + pid)
    #             json_dict = json.loads(r.text)
    #             status_code = str(r.status_code)
    #             if type(json_dict).__name__ == 'dict' :
    #                 status = json_dict['status']
    #                 self.assertTrue(status in (0, 1))
    #                 logs.Log.Log().getInstance(last_url + pid + ' | GET | ' + status_code + ' | ' + str(status) + ' | ' + str(json_dict['data']))
    #             else:
    #                 logs.Log.Log().getInstance(last_url + pid + ' | GET | ' + status_code + ' | ' + str(status))
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))

    #
    #
    # def test_query_bank_card_url(self):
    #     try:
    #         query_bank_card_url = self.localReadConfig.get_string('url','query_bank_card_url')
    #         last_url = self.base_url + query_bank_card_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + str(r.text))
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # ##实名认证
    #
    # # def test_id_validate(self):
    # #     try:
    # #         id_validate_url = self.localReadConfig.get_string('url','id_validate_url')
    # #         last_url = self.base_url + id_validate_url
    # #         r = self.s.get(
    # #             self.base_url + self.url,
    # #             headers = self.headers,
    # #             cookies = self.cookies
    # #         )
    # #         r = self.s.post(last_url,json={"id_name":"高强德","id_card":"620421199107176437","mobile":"xxxxx"})
    # #         json_dict = json.loads(r.text)
    # #         # 需要找个未绑定的身份证号验证下
    # #         if type(json_dict).__name__  == 'dict':
    # #             status = json_dict['status']
    # #             status_code = str(r.status_code)
    # #             if self.assertEqual(status,1) == None:
    # #                 logs.Log.Log().getInstance(last_url + ' | POST | ' + str(status) + ' | ' + status_code + ' | ' + str(json_dict['data']))
    # #             elif self.assertEqual(status,0) == None:
    # #                 logs.Log.Log().getInstance(last_url + ' | POST | ' + str(status) + ' | ' + status_code + ' | ' + str(json_dict['data']))
    # #             else:
    # #                 logs.Log.Log().getInstance(last_url + ' | POST | ' + str(status) + ' | ' + status_code + ' | ' + str(json_dict['data']))
    # #         else:
    # #             logs.Log.Log().getInstance(last_url)
    # #     except Exception as ex :
    # #         logs.Log.Log().getInstance(ex)
    #
    # def test_query_risk_subject(self):
    #     try:
    #         query_risk_url = self.localReadConfig.get_string('url','query_risk_url')
    #         last_url = self.base_url + query_risk_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_couponlist(self):
    #     try:
    #         couponlist_url = self.localReadConfig.get_string('url','couponlist_url')
    #         last_url = self.base_url + couponlist_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    #
    # def test_risk_flow(self):
    #     try:
    #         risk_flow_url = self.localReadConfig.get_string('url','risk_flow_url')
    #         last_url = self.base_url + risk_flow_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_common_problem(self):
    #     try:
    #         common_problem_url = self.localReadConfig.get_string('url','common_problem_url')
    #         last_url = self.base_url + common_problem_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_counponlist_unavailable(self):
    #     try:
    #         counponlist_un_url = self.localReadConfig.get_string('url','counponlist_un_url')
    #         last_url = self.base_url + counponlist_un_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #优惠券兑换码
    # def test_verifyredeemcode(self):
    #     try:
    #         verifyredeemcode_url = self.localReadConfig.get_string('url','verifyredeemcode_url')
    #         last_url = self.base_url + verifyredeemcode_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.post(last_url,json={"redeem_code":"12asdfas34"})
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict' :
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #存管账户充值流程
    # def test_recharge_flow(self):
    #     try:
    #         recharge_flow_url = self.localReadConfig.get_string('url','recharge_flow_url')
    #         last_url = self.base_url + recharge_flow_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #存管账户提现流程
    # def test_withdraw_flow(self):
    #     try:
    #         withdraw_flow_url = self.localReadConfig.get_string('url','withdraw_flow_url')
    #         last_url = self.base_url + withdraw_flow_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #提现后的流程
    # def test_query_bank_withdraw(self):
    #     try:
    #         query_bank_withdraw_url = self.localReadConfig.get_string('url','query_bank_withdraw_url')
    #         last_url = self.base_url + query_bank_withdraw_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #我的存管子账户余额查询
    # def test_query_amount_balance(self):
    #     try:
    #         query_amount_balance_url = self.localReadConfig.get_string('url','query_amount_balance_url')
    #         last_url = self.base_url + query_amount_balance_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_is_realname(self):
    #     try:
    #         is_realname_url = self.localReadConfig.get_string('url','is_realname_url')
    #         last_url = self.base_url + is_realname_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict' :
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #开通微支付绑卡
    # def test_repayment_flow(self):
    #     try:
    #         repayment_flow_url = self.localReadConfig.get_string('url','repayment_flow_url')
    #         last_url = self.base_url + repayment_flow_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.post(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #绑定银行卡信息接口
    # def test_query_persongold_account(self):
    #     try:
    #         query_persongold_account_url = self.localReadConfig.get_string('url','query_persongold_account_url')
    #         last_url = self.base_url + query_persongold_account_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         print(json_dict)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex:
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #购买成功状态显示接口
    # def test_buy_result(self):
    #     try:
    #         buy_result_url = self.localReadConfig.get_string('url','buy_result_url')
    #         last_url = self.base_url + buy_result_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.post(last_url,json={"order_no":"MT2018031216055500817909"})
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(status))
    #         else :
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #######合同查看接口
    # def test_transfer_contract(self):
    #     try:
    #         transfer_contract_url = self.localReadConfig.get_string('url','transfer_contract_url')
    #         last_url = self.base_url + transfer_contract_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         jsonData = {}
    #         typelist = ['oc','ac','dc']
    #         orderNolist = test_UserSync.test_orders_tender_record(self)
    #         for i in orderNolist:
    #             for j in typelist :
    #                 jsonData['order_no'] = i
    #                 jsonData['type'] = j
    #                 r = self.s.post(last_url,json=jsonData)
    #                 json_dict = json.loads(r.text)
    #                 status_code = str(r.status_code)
    #                 if type(json_dict).__name__ == 'dict' :
    #                     status = json_dict['status']
    #                     self.assertTrue(status in (0,1))
    #                     logs.Log.Log().getInstance(last_url + ' | POST | ' + status_code + ' | ' + str(status) + ' | ' + json_dict['data'])
    #                 else:
    #                     logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # def test_regbank(self):
    #     try:
    #         regbank_url = self.localReadConfig.get_string('url','regbank_url')
    #         last_url = self.base_url + regbank_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = r.status_code
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0, 1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else :
    #             logs.Log.Log().getInstance(last_url + ' | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #
    # #####查询银行限额
    # def test_bank_limit(self):
    #     try:
    #         bank_limit_url = self.localReadConfig.get_string('url','bank_limit_url')
    #         last_url = self.base_url + bank_limit_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         r = self.s.get(last_url)
    #         json_dict = json.loads(r.text)
    #         status_code = str(r.status_code)
    #         if type(json_dict).__name__ == 'dict':
    #             status = json_dict['status']
    #             self.assertTrue(status in (0,1))
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(status))
    #         else:
    #             logs.Log.Log().getInstance(last_url + ' | GET | ' + status_code + ' | ' + str(r.text))
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))
    #

    # ##债权记录接口
    # def test_asset_info(self):
    #     try:
    #         asset_info_url = self.localReadConfig.get_string('url','asset_info_url')
    #         last_url = self.base_url + asset_info_url
    #         r = self.s.get(
    #             self.base_url + self.url,
    #             headers = self.headers,
    #             cookies = self.cookies
    #         )
    #         #test_xls返回一个元祖，一个id，一个prdid。获取后取出来
    #         productIdList = test_UserSync.test_xls(self)[1]
    #         for pid in productIdList:
    #             r = self.s.get(last_url + pid)
    #             json_dict = json.loads(r.text)
    #             status_code = str(r.status_code)
    #             if type(json_dict).__name__ == 'dict':
    #                 status = json_dict['status']
    #                 self.assertTrue(status in (0,1))
    #                 logs.Log.Log().getInstance(last_url + pid + ' | GET | ' + status_code + ' | ' + str(status))
    #             else:
    #                 logs.Log.Log().getInstance(last_url + pid + ' | GET | ' + status_code + ' | ' + r.text)
    #     except Exception as ex :
    #         logs.Log.Log().getInstance(str(ex))

    def test_risk_contrast(self):
        risk_contrast_url = self.localReadConfig.get_string('url','risk_contrast_url')
        

    def tearDown(self):
        print("end start")

if __name__ == '__main__':
    unittest.main()
    # now_time = time.strftime("%Y%m%M%H%M%S", time.localtime(time.time()))
    # suite = unittest.TestSuite()
    # suite.addTest(test_UserSync('test_user_sync'))
    # suite.addTest(test_UserSync('test_xls'))
    # suite.addTest(test_UserSync('test_GetProductById'))
    # suite.addTest(test_UserSync('test_profile'))
    # suite.addTest(test_UserSync('test_risk'))
    # suite.addTest(test_UserSync('test_account'))
    # suite.addTest(test_UserSync('test_orders'))
    # suite.addTest(test_UserSync('test_orders_tender_record'))
    # suite.addTest(test_UserSync('test_query_bank_card_url'))
    # suite.addTest(test_UserSync('test_query_risk_subject'))
    # suite.addTest(test_UserSync('test_couponlist'))
    # suite.addTest(test_UserSync('test_risk_flow'))
    # suite.addTest(test_UserSync('test_common_problem'))
    # suite.addTest(test_UserSync('test_counponlist_unavailable'))
    # suite.addTest(test_UserSync('test_verifyredeemcode'))
    # suite.addTest(test_UserSync('test_recharge_flow'))
    # suite.addTest(test_UserSync('test_withdraw_flow'))
    # suite.addTest(test_UserSync('test_query_bank_withdraw'))
    # suite.addTest(test_UserSync('test_query_amount_balance'))
    # suite.addTest(test_UserSync('test_query_persongold_account'))
    # suite.addTest(test_UserSync('test_transfer_contract'))
    # suite.addTest(test_UserSync('test_buy_result'))
    # suite.addTest(test_UserSync('test_repayment_flow'))
    # suite.addTest(test_UserSync('test_is_realname'))
    # suite.addTest(test_UserSync('test_bank_limit'))
    # fp = open('..//report//' + now_time + '.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='Test MeiTu',
    #     description='Test Case Run Result')
    # runner.run(suite)
    # common.sendEmail.send_email(now_time)
