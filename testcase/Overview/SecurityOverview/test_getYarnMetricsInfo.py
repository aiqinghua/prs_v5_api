# _*_ coding : utf-8 _*_
# @Time : 2024/4/16 22:14
# @Author : aiqinghua
# @File : test_Overview
# @Project : prs_v5
import logging
import pytest
import allure
from utils.path_util import file_path
from utils.excle_utli import HandleExcle


@allure.epic("总览")
class TestGetYarnMetricsInfo:
    @allure.feature("安全总览")
    @pytest.mark.parametrize(argnames="cases", argvalues=HandleExcle(file_path() + "/data/SecurityOverview.xlsx", "getYarnMetricsInfo").read_data())
    def test_getYarnmetricsInfo(self, cases, start_up):
        interface, casename, row, url, method, headers, request_type, data, expected, \
        redis_client, ck_client, risk_table, sendrequest = start_up
        # 动态设置报告
        allure.dynamic.story(interface)
        allure.dynamic.title(casename)
        with allure.step("发送请求"):
            response = sendrequest.all_send_request(method, url, request_type, data, headers)
            res = response
            logging.info("预期结果为：{}".format(expected))

        try:
            with allure.step("进行接口断言"):
                assert expected["message"] == res["message"]
                assert expected["code"] == res["code"]
        except AssertionError as e:
            logging.error(f"用例--【{casename}】--执行失败")
            logging.exception(e)
            # 回写结果,不建议会写结果
            # self.excle.write_data(row=row, column=9, value="fail")
            raise e
        else:
            logging.info(f"用例--【{casename}】--执行成功")
            # self.excle.write_data(row=row, column=9, value="pass")