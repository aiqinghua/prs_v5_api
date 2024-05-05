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
        warnings.filterwarnings(action="ignore")
        method = method.lower()
        if request_type == "params":
            response = SendRequest.session.request(method=method, url=url, params=data, headers=headers, **kwargs, verify=False)
        elif request_type == "data":
            response = SendRequest.session.request(method=method, url=url, data=data, headers=headers, **kwargs, verify=False)
        elif request_type == "json":
            response = SendRequest.session.request(method=method, url=url, json=data, headers=headers, **kwargs, verify=False)
        # logger.info(f"请求方法为：{method}, 请求地址为：{url}, 请求数据为：{data}")
        # logger.info(f"实际结果为：{response.json()}")
        logging.info(f"请求方法为：{method}, 请求地址为：{url}, 请求数据为：{data}")
        logging.info(f"实际结果为：{response.json()}")

        return response.json()