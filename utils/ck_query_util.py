# _*_ coding : utf-8 _*_
# @Time : 2024/4/15 0:19
# @Author : aiqinghua
# @File : ck_query_util
# @Project : prs_v5
import logging
import clickhouse_connect
from utils.read_ini_util import HandleConf


class HandlerCk():
    def __init__(self, filename):
        self.ck_conf = HandleConf(filename)
        self.host = self.ck_conf.get_str(section="clickhouse", option="host")
        self.port = int(self.ck_conf.get_str(section="clickhouse", option="port"))
        self.user = self.ck_conf.get_str(section="clickhouse", option="user")
        self.password = self.ck_conf.get_str(section="clickhouse", option="password")
        self.ck_client = clickhouse_connect.get_client(
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password
        )

    def ck_query_first_item(self, sql, table):
        result = self.ck_client.query(query=sql, parameters={"table": table})
        logging.info(f"CK查询结果为：{result.first_item}")
        return result.first_item

    def ck_query_first_result_rows(self, sql, table):
        result = self.ck_client.query(query=sql, parameters={"table": table})
        logging.info(f"CK查询结果为：{result.result_rows}")
        return result.result_rows

    def ck_query_first_result_set(self, sql, table):
        """
          执行查询并返回第一个结果集。
          :param sql: 执行的SQL查询语句。
          :return: 查询结果的结果集部分。
          """
        result = self.ck_client.query(query=sql, parameters={"table": table})
        logging.info(f"CK查询结果为：{result.result_set}")
        return result.result_set

    def __del__(self):
        self.ck_client.close()


if __name__ == '__main__':
    test = HandlerCk("/config/config.ini")
    sql = "SELECT risk_count.phase, risk_count, success_risk_count FROM ( SELECT phase, COUNT(1) AS risk_count FROM prs.{table:Identifier} WHERE ts >= toUnixTimestamp(toStartOfDay(now())) * 1000 AND ts <= toUnixTimestamp(now(timezone())) * 1000 AND ignore = false AND phase IS NOT NULL GROUP BY phase ) risk_count LEFT JOIN ( SELECT phase, COUNT(1) AS success_risk_count FROM prs.{table:Identifier} WHERE ts >= toUnixTimestamp(toStartOfDay(now())) * 1000 AND ts <= toUnixTimestamp(now(timezone())) * 1000 AND ignore = false AND is_success = 1 AND phase IS NOT NULL GROUP BY phase ) success_count ON risk_count.phase = success_count.phase WHERE phase != 0"
    ck_res = test.ck_query_first_result_set(sql, "risk_dist")
    print(ck_res)
    # print(ck_res["riskall"], type(ck_res))
    # print(test.ck_query_first_result_set(sql))
