# _*_ coding : utf-8 _*_
# @Time : 2024/5/3 0:18
# @Author : aiqinghua
# @File : empty_file
# @Project : prs_v5
from utils.path_util import file_path


def empty_file(filename):
    """
    清空文件内容
    :param filename:要清空的文件
    :return:
    """
    with open(file=file_path() + filename, mode="w", encoding="utf-8") as fp:
        fp.write("")