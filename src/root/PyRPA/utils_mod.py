"""
工具模块
"""
import re


def MyRegexMatch(pattern, restr):
    """
    正则表达式匹配
    :param pattern: 正则表达式匹配规则
    :param restr: 需要匹配的字符串
    :return: isRestr -- true/false
    """
    isRestr = True
    result = re.match(pattern, restr)
    if result is None:
        isRestr = False
    return isRestr
