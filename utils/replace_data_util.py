# _*_ coding : utf-8 _*_
# @Time : 2024/4/29 23:12
# @Author : aiqinghua
# @File : replace_data_util
# @Project : prs_v5
import re
from utils.time_util import HandlerTime
from utils.yaml_util import YamlUtil


class HandleData:
    """
    该类用于数据替换
    """
    def __init__(self):
        self.risk_time = HandlerTime()
        self.start_time_mapping = {
            "5min": self.risk_time.last_5_min(),
            "30min": self.risk_time.last_30_min(),
            "1h": self.risk_time.last_1h(),
            "12h": self.risk_time.last_12h(),
            "24h": self.risk_time.last_24h(),
            1: self.risk_time.newday_zero0(),
            3: self.risk_time.threeday_zero0(),
            7: self.risk_time.sevenday_zero0(),
            30: self.risk_time.thirty_zero0(),
            90: self.risk_time.ninety_zero0()
        }
        self.end_time_mapping = {
            "5min": self.risk_time.new_time_second(),
            "30min": self.risk_time.new_time_second(),
            "1h": self.risk_time.new_time_second(),
            "12h": self.risk_time.new_time_second(),
            "24h": self.risk_time.new_time_second(),
            1: self.risk_time.new_time(),
            3: self.risk_time.new_time(),
            7: self.risk_time.new_time(),
            30: self.risk_time.new_time(),
            90: self.risk_time.new_time()
        }
        # self.end_time = self.risk_time.new_time()
        self.yaml_read = YamlUtil("/cache/temp.yaml")

    def replace_time(self, data, query_day):
        """
        根据提供的查询日，将数据中的特定时间标签替换为对应的时间。
        :param data: 包含时间标签的数据，标签形式为"${start_time}"和"${end_time}"。
        :param query_day: 查询的日，用于在时间映射中查找对应的时间。
        :return: 替换时间标签后的数据。
        """

        start_time = self.start_time_mapping.get(query_day, "")
        end_time = self.end_time_mapping.get(query_day, "")

        if start_time and end_time:
            data = data.replace("${start_time}", str(start_time))
            data = data.replace("${end_time}", str(end_time))
        else:
            raise ValueError(f"Unsupported query_day: {query_day}")

        return data


    def replace_data(self, data):
        temp_conf = self.yaml_read.read_yaml()
        print(temp_conf)
        for item in re.findall(r'\${(.+?)}', data):
            attr = item
            if attr in temp_conf:
                value = temp_conf[attr]
                print(value, type(value))
                data = data.replace('${' + attr + '}', f'"{value}"')

        return data
    # def replace_data(self, data):
    #     print(data)
    #     temp_conf = self.yaml_read.read_yaml()
    #     while re.search('\${(.+?)}', data):
    #         res = re.search('\${(.+?)}', data)
    #     #     # 获取正则匹配到的数据
    #         item = res.group()
    #         print(item)
    #         attr = res.group(1)
    #         if attr == temp_conf[attr]:
    #             pass
    #     #     try:
    #     #         # 获取类属性中需要被替换的值
    #     #         pass
    #     #         # value = getattr(cls, attr)
    #     #     except AttributeError:
    #     #         # 从配置文件中查找数据进行替换
    #     #         pass
    #         # 进行替换
    #         # data = data.replace(item, str(value))
    #     return data

if __name__ == '__main__':
    # data = '{"ts":[${start_time},${end_time}]}'
    # testtime = HandleData()
    # temp = testtime.replace_time(data, 7)
    # print(temp)
    data = '{"ip":${hostname},"netcard":"","startTime":1714674441,"endTime":1714676241,"step":"20"}'
    resp = HandleData()
    print(resp.replace_data(data))