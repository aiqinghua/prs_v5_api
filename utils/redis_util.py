# _*_ coding : utf-8 _*_
# @Time : 2024/5/1 0:18
# @Author : aiqinghua
# @File : redis_util
# @Project : prs_v5
import redis
from utils.read_ini_util import HandleConf


class HandleRedis:
    def __init__(self, filename):
        self.redis_conf = HandleConf(filename)
        self.host = self.redis_conf.get_str(section="redis", option="host")
        self.port = int(self.redis_conf.get_str(section="redis", option="port"))
        self.password = self.redis_conf.get_str(section="redis", option="password")
        self.db = int(self.redis_conf.get_str(section="redis", option="db"))
        self.redis_client = redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db
        )

    def redis_query(self, keys):
        """
        查询redis缓存
        :param keys: 要查询的key
        :return:
        """
        self.key = self.redis_client.keys(keys)
        return self.key

    def redis_del(self, keys):
        """
        清空redis缓存
        :param keys: 要清空的key
        :return:
        """
        try:
            for key in self.redis_client.keys(keys):
                self.redis_client.delete(key)
        except Exception as e:
            pass

    def __del__(self):
        self.redis_client.close()

# if __name__ == '__main__':
#     r = HandleRedis("/config/config.ini")
#     r.redis_query("ckSOAttackChain*")
#     r.redis_del("ckSOAttackChain*")