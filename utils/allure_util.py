# _*_ coding : utf-8 _*_
# @Time : 2024/5/10 21:56
# @Author : aiqinghua
# @File : allure_util
# @Project : prs_v5
import allure


class HandleAllure:
    @staticmethod
    def dynamic_allure(feature=None, story=None, title=None, desccase=None):
        """
        动态添加allure标签
        :param feature: 模块名称
        :param story: 功能名称
        :param title: 用例名称
        :param desccase: 用例描述
        :return:
        """
        allure.dynamic.feature(feature)
        allure.dynamic.story(story)
        allure.dynamic.title(title)
        allure.dynamic.description(desccase)