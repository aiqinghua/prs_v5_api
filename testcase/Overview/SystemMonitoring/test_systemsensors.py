# _*_ coding : utf-8 _*_
# @Time : 2024/4/16 22:14
# @Author : aiqinghua
# @File : test_Overview
# @Project : prs_v5
import logging
import pytest
import allure
from jsonpath import jsonpath
from utils.path_util import file_path
from utils.excle_utli import HandleExcle
from utils.send_request_util import SendRequest
from utils.read_ini_util import HandleConf
from utils.expected_util import HandlerExpected
from utils.time_util import HandlerTime
from utils.jsonpath_util import HandleJsonPath
from utils.yaml_util import YamlUtil


@allure.epic("总览")
@allure.feature("系统监控")
@allure.story("sensors")
class TestSystemSensors:
    excle = HandleExcle(file_path() + "/data/SystemMonitoring.xlsx", "sensors")
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
    # 实例化yanm对象
    yaml_util = YamlUtil(server_conf.get_str(section="yaml", option="temp_yaml"))


    # @pytest.mark.dependency(scope="session")
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize(argnames="cases", argvalues=case)
    def test_systemsensors(self, cases):
        # 获取请求数据
        # 用例名称
        casename = cases["casename"]
        # 动态设置报告中的用例名称
        allure.dynamic.title(casename)
        # 获取行号
        row = cases["case_id"] + 1
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
        # 获取预期结果
        expected = eval(cases["expected"])
        # 发送请求
        response = self.sendrequest.all_send_request(method, url, request_type, data, headers)
        res = response
        logging.info("预期结果为：{}".format(expected))
        # 结果回写到临时变量
        jsonp = cases["jsonpath"]
        if jsonp != None:
            hostname_expr = HandleJsonPath.jsonpath_split(jsonpathstr=jsonp, variable="hostname")
            ip_expr = HandleJsonPath.jsonpath_split(jsonpathstr=jsonp, variable="ip")
            hostname = jsonpath(res, hostname_expr)
            ip = jsonpath(res, ip_expr)
            data = {"hostname": hostname, "ip": ip}
            self.yaml_util.write_yaml(data=data)
            logging.info("hostname的值为：{},ip的值为：{}".format(hostname, ip))

        try:
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