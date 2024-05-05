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
from utils.send_request_util import SendRequest
from utils.read_ini_util import HandleConf
from utils.expected_util import HandlerExpected
from utils.time_util import HandlerTime
from utils.replace_data_util import HandleData
from utils.redis_util import HandleRedis
from utils.ck_query_util import HandlerCk


@allure.epic("总览")
@allure.feature("安全总览")
@allure.story("全部风险")
class TestAllRisk:
    excle = HandleExcle(file_path() + "/data/SecurityOverview.xlsx", "allrisk")
    case = excle.read_data()
    # 读取服务器相关配置
    server_conf = HandleConf("/config/config.ini")
    # 获取基础路径
    base_url = server_conf.get_str(section="server", option="base_url")
    # 获取风险表
    risk_table = server_conf.get_str(section="clickhouse", option="risk_table")
    sendrequest = SendRequest()
    # 实例化断言对象
    expected_eq = HandlerExpected()
    # 实例化时间对象
    risk_time = HandlerTime()
    # 实例化替换对象
    data_replace = HandleData()
    # 实例化redis对象
    redis_client = HandleRedis("/config/config.ini")
    # 实例化CK对象
    ck_client = HandlerCk("/config/config.ini")

    @pytest.mark.parametrize(argnames="cases", argvalues=case)
    def test_allrisk(self, cases):
        # 获取请求数据
        # 用例名称
        casename = cases["casename"]
        # 动态设置报告中的用例名称
        allure.dynamic.title(casename)
        # 获取行号
        row = cases["case_id"] + 1
        # 获取查询数据的天数
        quert_day = cases["queryday"]
        # 获取请求路径
        url = self.base_url + cases["url"]
        # 获取请求方法
        method = cases["method"]
        # 获取请求头
        headers = eval(self.server_conf.get_str(section="server", option="headers"))
        # 获取请求类型
        request_type = cases["request_type"]
        # 获取请求数据
        data = cases["data"]
        with allure.step("对请求数据进行替换"):
            if data != None:
                """
                进行热加载处理
                """
                data = self.data_replace.replace_time(data, quert_day)
                data = eval(data)
        # 获取预期结果
        expected = eval(cases["expected"])
        with allure.step("清空redis缓存"):
            redis_key = cases["redis_key"]
            self.redis_client.redis_del(keys=redis_key)

            response = self.sendrequest.all_send_request(method, url, request_type, data, headers)
            res = response
            logging.info("预期结果为：{}".format(expected))
        with allure.step("进行ck查询"):
            sql = cases["ck_check"]
            ck_res = self.ck_client.ck_query_first_item(sql, table=self.risk_table)

        try:
            with allure.step("进行断言"):
                assert expected["message"] == res["message"]
                assert expected["code"] == res["code"]
                # 进行ck断言
                # 全部风险
                assert res["data"]["riskSumCount"] == ck_res["riskall"]
                # 今日新增风险
                assert res["data"]["todayNewRiskCount"] == ck_res["newaddrisk"]
                # 攻击成功风险
                assert res["data"]["attackSuccess"] == ck_res["successattackrisk"]
        except AssertionError as e:
            logging.error(f"用例--【{casename}】--执行失败")
            logging.exception(e)
            # 回写结果,不建议会写结果
            # self.excle.write_data(row=row, column=9, value="fail")
            raise e
        else:
            logging.info(f"用例--【{casename}】--执行成功")
            # self.excle.write_data(row=row, column=9, value="pass")