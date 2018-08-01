# coding:utf-8

import os
import configparser
import codecs


proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,"cfg.ini")

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        if data[:3] == codecs.BOM_UTF8:
            data = data[:3]
            file = codecs.open(configPath,"w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    #获取sections列表
    def get_sections(self):
        if self.cf:
            return self.cf.sections()

    # 获取指定section的配置信息列表
    def get_sections_items(self,section):
        if self.cf:
            return self.cf.items(section)

    def get_string(self,section,option):
        if self.cf:
            return self.cf.get(section,option)

    def get_int(self,section,option):
        if self.cf:
            return self.cf.getint(section,option)

    def get_float(self,section,option):
        if self.cf:
            return self.cf.getfloat(section,option)

    def get_boolean(self,section,option):
        if self.cf:
            return self.cf.getboolean(section,option)


# if __name__ == '__main__':
#     ini = ReadConfig()
#     sections = ini.get_sections()
#     for sec in sections:
#         items = ini.get_sections_items(sec)
#
#     print(ini.get_string('url','user_sync_url'))