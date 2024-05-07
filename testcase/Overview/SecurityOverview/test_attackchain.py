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
from utils.ck_result_tools import ck_result_tool


@allure.epic("总览")
@allure.feature("安全总览")
@allure.story("攻击链")
class TestAttackChain:
    @pytest.mark.parametrize(argnames="cases", argvalues=HandleExcle(file_path() + "/data/SecurityOverview.xlsx", "attackChain").read_data())
    def test_attackchain(self, cases,start_up):
        casename, row, url, method, headers, request_type, data, expected, \
        redis_client, ck_client, risk_table, sendrequest = start_up
        with allure.step("清空redis缓存"):
            redis_key = cases["redis_key"]
            redis_client.redis_del(keys=redis_key)
        with allure.step("发送请求"):
            response = sendrequest.all_send_request(method, url, request_type, data, headers)
            res = response
            logging.info("预期结果为：{}".format(expected))
        if cases["ck_check"] != None:
            with allure.step("进行CK查询"):
                sql = cases["ck_check"]
                ck_res = ck_client.ck_query_first_result_set(sql, table=risk_table)
                ck_res = ck_result_tool(ck_res)

        try:
            with allure.step("进行接口断言"):
                assert res["message"] == expected["message"]
                assert res["code"] == expected["code"]
            with allure.step("进行CK断言"):
                if ck_res != {}:
                    assert res["data"][0]["count"] == ck_res[1]["risk_count"]
                    assert res["data"][0]["isSuccessCount"] == ck_res[1]["success_risk_count"]
                    assert res["data"][1]["count"] == ck_res[2]["risk_count"]
                    assert res["data"][1]["isSuccessCount"] == ck_res[2]["success_risk_count"]
                    assert res["data"][2]["count"] == ck_res[3]["risk_count"]
                    assert res["data"][2]["isSuccessCount"] == ck_res[3]["success_risk_count"]
                    assert res["data"][3]["count"] == ck_res[4]["risk_count"]
                    assert res["data"][3]["isSuccessCount"] == ck_res[4]["success_risk_count"]
                    assert res["data"][4]["count"] == ck_res[5]["risk_count"]
                    assert res["data"][4]["isSuccessCount"] == ck_res[5]["success_risk_count"]
        except AssertionError as e:
            logging.info(f"用例--【{casename}】--执行失败")
            logging.exception(e)
            # 回写结果,不建议会写结果
            # self.excle.write_data(row=row, column=9, value="fail")
            raise e
        else:
            logging.info(f"用例--【{casename}】--执行成功")
            # self.excle.write_data(row=row, column=9, value="pass")