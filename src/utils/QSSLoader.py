"""
@author: 54Coconi
加载QSS文件类
"""


class QSSLoader:
    """
    加载QSS文件类
    """

    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        """

        :param qss_file_name:
        :return:
        """
        with open(qss_file_name, 'r', encoding='UTF-8') as file:
            return file.read()
