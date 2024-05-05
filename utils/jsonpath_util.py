# _*_ coding : utf-8 _*_
# @Time : 2024/5/2 2:26
# @Author : aiqinghua
# @File : jsonpath_util
# @Project : prs_v5
from jsonpath import jsonpath


class HandleJsonPath:
    def __init__(self):
        pass
    @staticmethod
    def jsonpath_split(jsonpathstr, variable):
        jsonp = jsonpathstr.split(",")
        for i in jsonp:
            if variable in i:
                return i


if __name__ == '__main__':
    ip = HandleJsonPath.jsonpath_split("$..hostname,$..ip", "ip")
    print(ip)