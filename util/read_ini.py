# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:22
# @Author  : mandy
import configparser

import conftest


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conftest.env_dir
        else:
            self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.data = self.read_ini()

    def read_ini(self):
        self.config.read(self.file_path, encoding='utf-8')
        return self.config

    def get_value(self, key, section=None):
        if section is None:
            section = 'api'
        else:
            section = section
        return self.data.get(section, key)

    def set_ini(self, section, key, value):
        try:
            self.config.set(section, key, value)
            self.config.write(open(self.file_path, 'r+'))
        except:
            print(u'写入数据失败')
        # write to file


# if __name__ == '__main__':
#     readIni = ReadIni()
#     print(readIni.file_path)
#     local = readIni.get_value('base_url', 'api')
#     print(local)
#     readIni.set_ini('app','app_name','test123')

