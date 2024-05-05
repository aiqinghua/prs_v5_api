# _*_ coding : utf-8 _*_
# @Time : 2024/4/10 22:42
# @Author : aiqinghua
# @File : read_file
# @Project : prs_v5
import os
import yaml
from utils.path_util import file_path

class YamlUtil():
    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        with open(file_path() + self.filename, encoding="utf-8") as fp:
            value =yaml.load(stream=fp, Loader=yaml.FullLoader)
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, list):
                        value[k] = ', '.join(map(str, v))
            else:
                raise ValueError("读取到的值并非字典")
            return value

    def write_yaml(self, data):
        path = file_path() + self.filename
        with open(file=path, mode="a", encoding="utf-8") as fp:
            yaml.dump(data=data, stream=fp, allow_unicode=True)

if __name__ == '__main__':
    hostname = "prs-sensor"
    ip  = "1.1.1.1"
    data = {
        "hostname": hostname,
        "ip": ip
    }
    yaml_util = YamlUtil(filename="/cache/temp.yaml")
    # yaml_util.write_yaml(data=data)
    value = yaml_util.read_yaml()
    print(value)
    # {'flinkCluster': 'true', 'hostname': 'prs-sensor', 'ip': '10.0.81.54'}
