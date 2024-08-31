"""
检查字符串模块
"""


def validate_input(input_str):
    """
    检查字符串中是否包含 "/" 或 "\\\\"
    :param input_str: 输入的字符串
    :return: '/' not in input_str and '\\' not in input_str - 布尔值
    """
    # 检查字符串中是否包含 "/" 或 "\"
    return '/' not in input_str and '\\' not in input_str

