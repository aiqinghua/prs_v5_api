# _*_ coding : utf-8 _*_
# @Time : 2024/5/4 22:03
# @Author : aiqinghua
# @File : conftest
# @Project : prs_v5
# conftest.py
import logging
import pytest
import allure
from utils.ck_query_util import HandlerCk
from utils.expected_util import HandlerExpected
from utils.read_ini_util import HandleConf
from utils.redis_util import HandleRedis
from utils.replace_data_util import HandleData
from utils.send_request_util import SendRequest
from utils.time_util import HandlerTime



def pytest_collection_modifyitems(session, config, items):
    logging.info("收集到的测试用例为：{}".format(items))
    logging.info(f"收集到的用例数量为：{len(items)}")

@pytest.fixture(scope="function", autouse=True)
def start_up(cases):
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
    # 获取请求数据
    # 用例名称
    casename = cases["casename"]
    # 获取行号
    row = cases["case_id"] + 1
    # 获取查询数据的天数
    quert_day = cases["queryday"]
    # 获取请求路径
    url = base_url + cases["url"]
    # 获取请求方法
    method = cases["method"]
    # 获取请求头
    headers = eval(server_conf.get_str(section="server", option="headers"))
    # 获取请求类型
    request_type = cases["request_type"]
    # 获取请求数据
    data = cases["data"]
    with allure.step("对请求数据进行替换"):
        if data != None:
            """
            进行热加载处理
            """
            data = data_replace.replace_time(data, quert_day)
            data = eval(data)
    # 获取预期结果
    expected = eval(cases["expected"])
    yield casename, row, url, method, headers, request_type, data, expected, \
          redis_client, ck_client, risk_table, sendrequest



@pytest.hookimpl
def pytest_configure(config):
    log_colors = {
        'CRITICAL': 'magenta',
        'ERROR': 'red',
        'WARNING': 'yellow',
        'INFO': 'green',
        'DEBUG': 'blue',
    }
    config.option.log_level = 'DEBUG'
    config.option.color = 'yes'
    config.option.log_format = '%(levelname)s:%(name)s:%(message)s'
    config.option.log_datefmt = '%H:%M:%S'
    config.option.log_style = '{level}: {msg}'
    for level, color in log_colors.items():
        config.option.color = {level: color}
