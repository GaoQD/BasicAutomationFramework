'''
-*- coding: utf-8 -*-
@Author  : Admin
@Time    : 18-7-26 下午3:50
@Software: PyCharm Community Edition
@File    : testLog.py
'''

import logging


class Log:
    file_name = '..//logs//test.log'
    fmt = '%(asctime)s-%(levelname)s %(message)s'
    def __init__(self):
        logging.basicConfig(filename=self.file_name,filemode='a+',format=self.fmt)
        self.__hander = logging.StreamHandler()
        self.__hander.setLevel(logging.DEBUG)

        formatter = logging.Formatter(self.fmt)
        self.__hander.setFormatter(formatter)
        return

    def getInstance(self,strname):
        logger = logging.getLogger(strname)
        logger.addHandler(self.__hander)
        logger.setLevel(logging.DEBUG)
        # print(strname)
        logger.debug(strname)
        return logger

# if __name__ == '__main__':
#     rst = Log().getInstance('abc')
