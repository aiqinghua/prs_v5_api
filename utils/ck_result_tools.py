# _*_ coding : utf-8 _*_
# @Time : 2024/5/1 22:28
# @Author : aiqinghua
# @File : ck_result_tools
# @Project : prs_v5

def ck_result_tool(value):
    """
    将ck查询后的多组结果进行处理(ck_query_first_result_set方法)，将给定的元组列表转换成字典格式，每个元组包含阶段信息、风险计数和成功风险计数。
    参数:
    value - 一个元组列表，每个元组包含三个元素：(阶段, 风险计数, 成功风险计数)
    返回值:
    无返回值，该函数直接打印转换后的字典。
    """
    data_tuples = value
    data_dict = {}
    for phase, risk_count, success_risk_count in data_tuples:
        data_dict[phase] = {"risk_count": risk_count, "success_risk_count": success_risk_count}
    return data_dict

if __name__ == '__main__':
    data_tuples = [(1, 3976865, 977369), (2, 17789452, 95157), (3, 4286797, 34051), (4, 71849, 0), (5, 63112, 0)]
    ck_res = ck_result_tool(value=data_tuples)
    print(ck_res[1])