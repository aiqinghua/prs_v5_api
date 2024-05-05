import os
import pytest
from utils.remove_file_util import remove_file
from utils.empty_file import empty_file


if __name__ == '__main__':
    # 每次执行前删除日志文件
    remove_file("logs/")
    # 清空临时变量文件内容
    empty_file("/cache/temp.yaml")
    # time.sleep(2)
    pytest.main()
    os.system("allure generate temp -o report --clean")