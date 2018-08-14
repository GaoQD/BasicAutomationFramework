# coding:utf-8

import xlrd
from xlutils.copy import copy
import requests
import config.readConfig as readConfig
import json

#写入excel
def modify_excel(num,result_des,file_name):
    wb = xlrd.open_workbook(file_name)
    wb2 = copy(wb)
    sheet2 = wb2.get_sheet(0)
    for i in range(num,num + 1):
        sheet2.write(i, 5, result_des)
    wb2.save(file_name)
    return

#获取excel文件中固定的值
def get_excel(start_num,end_num,file_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_name(wb.sheet_names()[0])
    nrows = sheet.nrows
    titleList = sheet.row_values(0)
    cls = []
    if end_num < nrows:
        for j in range(start_num, end_num):
            rowValues = sheet.row_values(j)
            caseDict = dict(zip(titleList, rowValues))
            cls.append(caseDict)
    else:
        end_num = nrows
        for j in range(start_num, end_num):
            rowValues = sheet.row_values(j)
            caseDict = dict(zip(titleList, rowValues))
            cls.append(caseDict)
    return cls

'''
    创建并返回登录session
    注意：
        不管是get还是post方法，都需要传递cookies参数
'''
def getLoginState(url):
    s = requests.session()
    r = s.get(
        url,
        headers = json.loads(readConfig.ReadConfig().get_string('data','headers')),
        cookies = json.loads(readConfig.ReadConfig().get_string('data','cookies'))
    )
    return r

# if __name__ == '__main__':
#     url = 'https://jr.huanqiu.com/api/financial/login'
#     r = getLoginState(url)
#     print(r.cookies)
#     # r = requests.session().post('https://jr.huanqiu.com/api/financial/real_name',json={"id_name": "高强德","id_card": "620421199107176437"},cookies = r.cookies)
#     r = requests.session().get('https://jr.huanqiu.com/api/financial/product_record?sort=create_at&page=0&prd_id=170712110125149')
#     print(r)
