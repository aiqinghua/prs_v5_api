# _*_ coding : utf-8 _*_
# @Time : 2024/4/15 0:18
# @Author : aiqinghua
# @File : expected_util
# @Project : prs_v5

class HandlerExpected:
    def expected_eq(self, expected, response):
        assert expected == response