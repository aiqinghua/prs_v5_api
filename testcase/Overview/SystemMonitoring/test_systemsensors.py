# _*_ coding : utf-8 _*_
# @Time : 2024/4/16 22:14
# @Author : aiqinghua
# @File : test_Overview
# @Project : prs_v5
import logging
import pytest
import allure
from jsonpath import jsonpath
from utils.allure_util import HandleAllure
from utils.path_util import file_path
from utils.excle_utli import HandleExcle
from utils.jsonpath_util import HandleJsonPath


@allure.epic("总览")
class TestSystemSensors:
    # @pytest.mark.dependency(scope="session")
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize(argnames="cases", argvalues=HandleExcle(file_path() + "/data/SystemMonitoring.xlsx", "sensors").read_data())
    def test_systemsensors(self, cases, start_up):
        module, interface, casename, row, url, method, headers, request_type, data, expected, \
        redis_client, ck_client, risk_table, sendrequest, yaml_util = start_up
        # 动态设置报告
        HandleAllure.dynamic_allure(feature=module, story=interface, title=casename)

        with allure.step("发送请求"):
            response = sendrequest.all_send_request(method, url, request_type, data, headers)
            res = response
            logging.info("预期结果为：{}".format(expected))
        with allure.step("结果回写到临时变量"):
            jsonp = cases["jsonpath"]
            if jsonp != None:
                hostname_expr = HandleJsonPath.jsonpath_split(jsonpathstr=jsonp, variable="hostname")
                ip_expr = HandleJsonPath.jsonpath_split(jsonpathstr=jsonp, variable="ip")
                hostname = jsonpath(res, hostname_expr)
                ip = jsonpath(res, ip_expr)
                data = {"hostname": hostname, "ip": ip}
                yaml_util.write_yaml(data=data)
                logging.info("hostname的值为：{},ip的值为：{}".format(hostname, ip))

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