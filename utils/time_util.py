# _*_ coding : utf-8 _*_
# @Time : 2024/4/21 23:59
# @Author : aiqinghua
# @File : time_util
# @Project : prs_v5
from datetime import time, date, datetime, timedelta


class HandlerTime:
    def __init__(self):
        self.times = time.min
        self.dates = date.today()
        self.date = datetime.combine(self.dates, self.times)

    def last_5_min(self):
        """
        计算并返回距当前时间30分钟前的时间戳（整数型）。
        :return: last_30_min - 距当前时间30分钟前的秒级时间戳。
        """
        time_5min = datetime.now() - timedelta(minutes=5)
        last_5_min = int(time_5min.timestamp())
        return last_5_min

    def last_30_min(self):
        """
        计算并返回距当前时间30分钟前的时间戳（整数型）。
        :return: last_30_min - 距当前时间30分钟前的秒级时间戳。
        """
        time_30min = datetime.now() - timedelta(minutes=30)
        last_30_min = int(time_30min.timestamp())
        return last_30_min

    def last_1h(self):
        time_1h = datetime.now() - timedelta(hours=1)
        last_1h = int(time_1h.timestamp())
        return last_1h

    def last_12h(self):
        time_12h = datetime.now() - timedelta(hours=12)
        last_12h = int(time_12h.timestamp())
        return last_12h

    def last_24h(self):
        time_24h = datetime.now() - timedelta(hours=24)
        last_24h = int(time_24h.timestamp())
        return last_24h


    def newday_zero0(self):
        newday_tszero0 = int(self.date.timestamp() * 1000)
        return newday_tszero0


    def threeday_zero0(self):
        data_3 = self.date + timedelta(days=-3)
        threeday_tszero0 = int(data_3.timestamp() * 1000)
        return threeday_tszero0


    def sevenday_zero0(self):
        data_7 = self.date + timedelta(days=-6)
        threeday_tszero0 = int(data_7.timestamp() * 1000)
        return threeday_tszero0

    def thirty_zero0(self):
        data_30 = self.date + timedelta(days=-29)
        threeday_tszero0 = int(data_30.timestamp() * 1000)
        return threeday_tszero0

    def ninety_zero0(self):
        data_90 = self.date + timedelta(days=-89)
        threeday_tszero0 = int(data_90.timestamp() * 1000)
        return threeday_tszero0

    def new_time(self):
        new_ts = int(datetime.now().timestamp()* 1000)
        return new_ts

    def new_time_second(self):
        """
        获取当前时间的秒数表示
        :return: 返回当前时间的秒级时间搓
        """
        new_ts_second = int(datetime.now().timestamp())
        return new_ts_second


if __name__ == '__main__':
    testtime = HandlerTime()
    # print(testtime.new_time())
    # print("当天0点的时间搓为：", testtime.newday_zero0())
    # print("3天前0点的时间搓为：", testtime.threeday_zero0())
    # print("7天前0点的时间搓为：", testtime.sevenday_zero0())
    print("30天前0点的时间搓为：", testtime.newday_zero0())
    print("90天前0点的时间搓为：", testtime.ninety_zero0())
    print("30分钟前的时间为：", testtime.last_24h())
