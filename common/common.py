# coding:utf-8

import os
import xlrd
from xml.etree import ElementTree as ElementTree
from xlutils.copy import copy


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
    print(cls)
    return cls

database = {}
def set_xml():
    if len(database) == 0 :
        sql_path = os.path.join('..//testFile','SQL.xml')
        tree = ElementTree.parse(sql_path)
        for db in tree.findall('database'):
            db_name = db.get('name')
            table = {}
            for tb in db.getchildren():
                table_name = tb.get('name')
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get('id')
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name,table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name,table_name,sql_id):
    db = get_xml_dict(database_name,table_name)
    sql = db.get(sql_id)
    return sql

if __name__ == '__main__':
    file_name = '..//testFile//test.xls'
    num = 1
    end_num = 6
    get_excel(num,end_num,file_name)
    # modify_excel(num,'PASS',file_name)