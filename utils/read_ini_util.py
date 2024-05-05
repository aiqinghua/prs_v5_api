# _*_ coding : utf-8 _*_
# @Time : 2024/4/14 16:06
# @Author : aiqinghua
# @File : read_ini_util
# @Project : prs_v5
import configparser
from utils.path_util import file_path


class HandleConf():
    def __init__(self, filename):
        self.conf_ini = configparser.ConfigParser(interpolation=None)
        self.conf_ini.read(filenames=file_path() + filename, encoding="utf-8")

    def get_str(self, section, option):
        value = self.conf_ini.get(section=section, option=option)
        return value

    def get_int(self, section, option):
        value = self.conf_ini.getint(section=section, option=option)
        return value

    def get_float(self, section, option):
        value = self.conf_ini.getfloat(section=section, option=option)
        return value

    def get_item(self, section):
        value = self.conf_ini.items(section=section)
        return dict(value)

    def write_data(self):
        pass



# conf_ini = HandleConf("/config/config.ini")
# print(conf_ini.get_str(section="server", option="headers"))
# print(conf_ini.get_item(section="mysql"))
