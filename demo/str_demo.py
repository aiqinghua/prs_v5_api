# _*_ coding : utf-8 _*_
# @Time : 2024/4/22 23:05
# @Author : aiqinghua
# @File : str_demo
# @Project : prs_v5
from jsonpath import jsonpath

data = {
    "message": "请求成功!",
    "data": [
        {
            "ip": "10.0.81.101",
            "hostname": "10.0.81.101"
        },
        {
            "ip": "10.0.81.54",
            "hostname": "prs-sensor"
        }
    ],
    "code": 20000
}

value = jsonpath(data, "$..hostname")
print(str(value[0]))