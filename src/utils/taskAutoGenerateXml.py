"""
自动生成一定结构的 xml 文件的功能模块
"""
import os
import xml.etree.ElementTree as ET


def create_xml_file(directory):
    """
    在新建任务的目录下生成一个具有相应结构的XML文件
    :param directory:
    """
    # 创建XML文件路径
    xml_file_path = os.path.join(directory, "CocoPyRPATask.xml")

    # 创建根元素
    root = ET.Element("PyRPACode")

    # 创建Action元素, 并赋初值
    # action = ET.SubElement(root, "Action")
    # action.set("Order", "")
    # action.set("OperationType", "")
    # action.set("FunctionCmd", "")
    # action.set("Content", "")
    # action.set("Loop", "")
    # action.set("ErrorLoop", "")
    # action.set("Desc", "")
    # action.set("Src", "")
    # action.set("IsRun", "")

    # 创建XML文件并写入内容
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)