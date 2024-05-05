# _*_ coding : utf-8 _*_
# @Time : 2024/4/26 0:05
# @Author : aiqinghua
# @File : mysql_util
# @Project : prs_v5
import json

import pymysql
from utils.read_ini_util import HandleConf

class HandlerMysql():
    def __init__(self):
        self.conf = HandleConf("/config/config.ini")
        self.mysql_conf = self.conf.get_item(section="mysql")
        self.conn = pymysql.connect(host=self.mysql_conf["host"],
                                    port=int(self.mysql_conf["port"]),
                                    user=self.mysql_conf["user"],
                                    password=self.mysql_conf["password"],
                                    # cursorclass=pymysql.cursors.DictCursor,
                                    charset="utf8",
                                    autocommit=True)
        self.cursor = self.conn.cursor()

    def find_one(self, sql):
        self.cursor.execute(sql)
        value = self.cursor.fetchone()
        self.cursor.close()
        return value

    def find_all(self, sql):
        self.cursor.execute(sql)
        value = self.cursor.fetchall()
        self.cursor.close()
        return value

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    sql = "select network from prs_light.prs_network_regions where type = 'intranet'"
    mysql_db = HandlerMysql()
    # mysql_db.find_all(sql=sql)
    print(mysql_db.find_all(sql=sql))