# coding:utf-8

import xlrd
from xlutils.copy import copy
import requests
import config.readConfig as readConfig
import json
import pymysql

'''
    #写入excel
    ncls 代表要输入的列的值，动态输入列值
'''
def modify_excel(num,result_des,file_name,ncls):
    wb = xlrd.open_workbook(file_name)
    wb2 = copy(wb)
    sheet2 = wb2.get_sheet(0)
    for i in range(num,num + 1):
        sheet2.write(i, ncls, result_des)
    wb2.save(file_name)
    return

'''
    #获取excel文件中固定的值
'''
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
    #获取excel文件中所有的内容
'''
def get_xls(file_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_name(wb.sheet_names()[0])
    nrows = sheet.nrows
    titleList = sheet.row_values(0)
    cls = []
    for i in range(1,nrows):
        rowValues = sheet.row_values(i)
        caseDict = dict(zip(titleList,rowValues))
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

'''
    数据库连接，需要传入参数，数据库的host，port，用户名密码以及数据库名称
    返回游标
'''
def getMysqlConnection(host,port,user,passwd,db):
    connect = pymysql.Connect(host = host,port = port,user = user,passwd = passwd,db = db,charset = 'utf8')
    cursors = connect.cursor()
    return cursors

'''
    关闭数据库连接
'''
def closeMysqlConnection(host,port,user,passwd,db):
    connect = pymysql.Connect(host = host,port = port,user = user,passwd = passwd,db = db,charset = 'utf8')
    connect.close()

'''
    关闭游标
'''
def closeMysqlCursors():
    cursors = getMysqlConnection()
    cursors.close()


'''
    清空log日志文件
    把文件定位到position 0，不加这句，文件默认定位到数据最后，truncate也是从这里开始删除，相当于追加
'''
def clearLog(file_name):
    with open(file_name,'r+') as f :
        f.seek(0)
        f.truncate()


# if __name__ == '__main__':
#     cursors = getMysqlConnection('localhost',3306,'root','root','sys')
#     sql = "select * from apps"
#     cursors.execute(sql)
#     for row in cursors.fetchall():
#         print(row)
#     url = 'http://cofss.test.congred.com/api/sx_capital/h5_login'
#     r = getLoginState(url)
#     print(r.cookies)
    # print(r.text)
#     url = 'https://jr.huanqiu.com/api/financial/login'
#     r = getLoginState(url)
#     print(r.cookies)
    # r = requests.session().post('https://jr.huanqiu.com/api/financial/real_name',json={"id_name": "高强德","id_card": "620421199107176437"},cookies = r.cookies)
    # r = requests.session().get('https://jr.huanqiu.com/api/financial/product_record?sort=create_at&page=0&prd_id=170712110125149')
    # print(r)
