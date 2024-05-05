# _*_ coding : utf-8 _*_
# @Time : 2024/4/14 16:06
# @Author : aiqinghua
# @File : log_util
# @Project : prs_v5
import logging
from utils.path_util import file_path
from utils.read_ini_util import HandleConf


def create_logger(logname, stream_level, filename, file_level, fmt, datefmt):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    # 日志控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    # 日志输出文件
    file_handler = logging.FileHandler(filename=file_path() + filename, encoding="utf-8")
    file_handler.setLevel(file_level)

    # 日志格式
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


conf_ini = HandleConf("/config/logs.ini")
logger = create_logger(
    logname = conf_ini.get_str(section="loggers", option="name"),
    stream_level = conf_ini.get_str(section="StreamHandler", option="stream_level"),
    filename = conf_ini.get_str(section="FileHandler", option="filename"),
    file_level = conf_ini.get_str(section="FileHandler", option="file_level"),
    fmt = conf_ini.get_str(section="formatter", option="fmt"),
    datefmt = conf_ini.get_str(section="formatter", option="datefmt")
)

# logger.debug("这是debug日志")
# logger.info("这是info日志")
# logger.warning("这是warning日志")
# logger.error("这是error日志")
# logger.critical("这是critical日志")