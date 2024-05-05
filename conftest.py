# _*_ coding : utf-8 _*_
# @Time : 2024/5/4 22:03
# @Author : aiqinghua
# @File : conftest
# @Project : prs_v5
# conftest.py
import pytest


@pytest.hookimpl
def pytest_configure(config):
    log_colors = {
        'CRITICAL': 'magenta',
        'ERROR': 'red',
        'WARNING': 'yellow',
        'INFO': 'green',
        'DEBUG': 'blue',
    }
    config.option.log_level = 'DEBUG'
    config.option.color = 'yes'
    config.option.log_format = '%(levelname)s:%(name)s:%(message)s'
    config.option.log_datefmt = '%H:%M:%S'
    config.option.log_style = '{level}: {msg}'
    for level, color in log_colors.items():
        config.option.color = {level: color}
