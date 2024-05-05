# _*_ coding : utf-8 _*_
# @Time : 2024/5/1 21:03
# @Author : aiqinghua
# @File : network_tools
# @Project : prs_v5


def network_tool(value):
    network_list = []
    for item in value:
        network_list.extend(eval(item[0]))
    return network_list

if __name__ == '__main__':
    network = (('["10.0.0.0/8","172.16.0.0/12","192.168.0.0/16"]',), ('["2.2.2.2"]',))
    network_list = network_tool(network)
    print(network_list)