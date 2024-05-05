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

@allure.epic("总览")
@allure.feature("安全总览")
@allure.story("攻击者")
class TestAttacker:
    excle = HandleExcle(file_path() + "/data/SecurityOverview.xlsx", "attacker")
    case = excle.read_data()
    # 读取服务器相关配置
    server_conf = HandleConf("/config/config.ini")
    # 获取基础路径
    base_url = server_conf.get_str(section="server", option="base_url")
    sendrequest = SendRequest()
    # 实例化断言对象
    expected_eq = HandlerExpected()
    # 实例化时间对象
    risk_time = HandlerTime()
    # 实例化替换对象
    data_replace = HandleData()

    @pytest.mark.parametrize(argnames="cases", argvalues=case)
    def test_attacker(self, cases):
        # 获取请求数据
        # 用例名称
        casename = cases["casename"]
        # 动态设置报告中的用例名称
        allure.dynamic.title(casename)
        # 获取行号
        row = cases["case_id"] + 1
        # 获取查询数据的天数
        quert_day = cases["queryday"]
        print(quert_day, type(quert_day))

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
        if data != None:
            """
            进行热加载处理
            """
            data = self.data_replace.replace_time(data, quert_day)
            data = eval(data)
        # 获取预期结果
        expected = eval(cases["expected"])
        # 发送请求
        response = self.sendrequest.all_send_request(method, url, request_type, data, headers)
        res = response
        logging.info("预期结果为：{}".format(expected))

        try:
            assert expected["message"] == res["message"]
            assert expected["code"] == res["code"]
            # 缺少ck断言
        except AssertionError as e:
            logging.error(f"用例--【{casename}】--执行失败")
            logging.exception(e)
            # 回写结果,不建议会写结果
            # self.excle.write_data(row=row, column=9, value="fail")
            raise e
        else:
            logging.info(f"用例--【{casename}】--执行成功")
            # self.excle.write_data(row=row, column=9, value="pass")