# _*_ coding : utf-8 _*_
# @Time : 2024/4/10 22:22
# @Author : aiqinghua
# @File : send_request
# @Project : prs_v5
import warnings
import logging
import requests


class SendRequest():
    session = requests.session()

    valid_methods = {"get", "post", "put", "delete", "options", "head"}  # 定义有效HTTP方法
    valid_request_types = {"params", "data", "json"}  # 定义有效请求
    def all_send_request(self, method, url, request_type=None, data=None,headers=None, **kwargs):
        """
        统一封装请求
        :param method:请求方法
        :param url:请求地址
        :param request_type: 入参关键字，根据该值决定发送什么请求
        :param data:请求内容
        :param headers:请求头
        :param kwargs:
        :return:
        """
        # 忽略警告信息
        warnings.filterwarnings(action="ignore")
        method = method.lower()
        # 参数校验
        if method not in self.valid_methods:
            raise ValueError(f"Invalid method: {method}. Must be one of {', '.join(self.valid_methods)}")
        if request_type not in self.valid_request_types:
            raise ValueError(
                f"Invalid request type: {request_type}. Must be one of {', '.join(self.valid_request_types)}")
        try:
            if request_type == "params":
                response = self.session.request(method=method, url=url, params=data, headers=headers, **kwargs, verify=False)
            elif request_type == "data":
                response = self.session.request(method=method, url=url, data=data, headers=headers, **kwargs, verify=False)
            elif request_type == "json":
                response = self.session.request(method=method, url=url, json=data, headers=headers, **kwargs, verify=False)

            logging.info(f"请求方法为：【{method}】, 请求地址为：【{url}】, 请求数据类型为：【{request_type}】, 请求数据为：{data}")
            if response:
                logging.info(f"实际结果为：{response.json()}")
            else:
                logging.info("无响应返回")

            return response.json() if response else None
        except requests.RequestException as e:
            logging.error(f"请求异常：{e}")
            return None