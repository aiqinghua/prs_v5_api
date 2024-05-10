# _*_ coding : utf-8 _*_
# @Time : 2024/5/4 19:00
# @Author : aiqinghua
# @File : run
# @Project : prs_v5
import os
import pytest
from utils.remove_file_util import remove_file
from utils.empty_file import empty_file


if __name__ == '__main__':
    # 每次执行前删除日志文件
    remove_file("/logs")
    # 清空临时变量文件内容
    empty_file("/cache/temp.yaml")
    pytest.main()
    # os.system("copy environment.properties temp\environment.properties")
    # os.system("allure generate temp -o report --clean")