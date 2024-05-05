# _*_ coding : utf-8 _*_
# @Time : 2024/4/29 22:01
# @Author : aiqinghua
# @File : remove_file_util
# @Project : prs_v5
import os
from utils.path_util import file_path

def remove_file(pathname):
    """
    该方法用于删除指定目录下的所有文件
    :param pathname: 要删除的目录
    :return:
    """
    del_list = os.listdir(file_path() + pathname)
    for f in del_list:
        filepath = os.path.join(file_path()+ pathname, f)
        if os.path.isfile(filepath):
            os.remove(filepath)