"""
另存为 Excel 模块
"""
import os

import pandas as pd


def save_to_excel(action_list, task_dir_name):
    """
    将数据保存至 Excel 文件中
    :param action_list: 数据列表
    :param task_dir_name: 任务目录名
    """
    # 确保目标目录存在
    output_dir = "work/TASKS/" + task_dir_name
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 构建 Excel 文件路径
    excel_file_path = os.path.join(output_dir, f"{task_dir_name}.xlsx")

    # 构建 DataFrame
    df = pd.DataFrame(action_list)

    # 将列名重新命名，以匹配指定的表头
    column_mapping = {
        "order": "操作图",
        "operationType": "操作类型",
        "functionCmd": "功能指令",
        "content": "实例对象",
        "loop": "循环次数",
        "errorLoop": "容错次数",
        "src": "图片路径",
        "isRun": "是否启用",
        "desc": "备注"
    }

    df.rename(columns=column_mapping, inplace=True)

    # 保存到 Excel 文件
    df.to_excel(excel_file_path, index=False)
    print(f"数据已保存至 {excel_file_path}")
