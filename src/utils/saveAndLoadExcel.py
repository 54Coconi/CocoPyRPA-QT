"""
 - 将数据保存至 Excel 文件
 - 加载 Excel 表格
"""
import os

import xlrd
import xlwt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

# def save_to_excel(action_list, task_dir_name):
#     """
#     将数据保存至 Excel 文件中
#     :param action_list: 数据列表
#     :param task_dir_name: 任务目录名
#     """
#     # 确保目标目录存在
#     output_dir = "work/TASKS/" + task_dir_name
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     # 构建 Excel 文件路径
#     excel_file_path = os.path.join(output_dir, f"{task_dir_name}.xls")
#
#     # 构建 DataFrame
#     df = pd.DataFrame(action_list)
#
#     # 将列名重新命名，以匹配指定的表头
#     column_mapping = {
#         "order": "操作图",
#         "operationType": "操作类型",
#         "functionCmd": "功能指令",
#         "content": "实例对象",
#         "loop": "循环次数",
#         "errorLoop": "容错次数",
#         "src": "图片路径",
#         "isRun": "是否启用",
#         "desc": "备注"
#     }
#
#     df.rename(columns=column_mapping, inplace=True)
#
#     # 保存到 Excel 文件
#     df.to_excel(excel_file_path, index=False)
#     print(f"数据已保存至 {excel_file_path}")

actionList = []


def save_to_excel(self, action_list, task_directory):
    """
    将数据保存至 Excel(.xls) 文件中
    :param self:
    :param action_list:
    :param task_directory:
    """
    # 创建一个Workbook对象
    workbook = xlwt.Workbook()
    # 添加一个工作表
    sheet = workbook.add_sheet('Sheet1')
    # 设置表头
    headers = ["操作图", "操作类型", "功能指令", "实例对象", "循环次数", "容错次数", "图片路径", "是否启用", "多行重复",
               "备注"]
    # 写入表头
    for col_index, header in enumerate(headers):
        sheet.write(0, col_index, header)

    # 写入数据
    for row_index, action in enumerate(action_list):
        sheet.write(row_index + 1, 0, action['order'])
        sheet.write(row_index + 1, 1, action['operationType'])
        sheet.write(row_index + 1, 2, action['functionCmd'])
        sheet.write(row_index + 1, 3, action['content'])
        sheet.write(row_index + 1, 4, action['loop'])
        sheet.write(row_index + 1, 5, action['errorLoop'])
        sheet.write(row_index + 1, 6, action['src'])
        sheet.write(row_index + 1, 7, action['isRun'])
        sheet.write(row_index + 1, 8, action['multipleLineRepeat'])
        sheet.write(row_index + 1, 9, action['desc'])

    # 确保目录存在
    task_path = os.path.join('work/TASKS/', task_directory)
    os.makedirs(task_path, exist_ok=True)
    # 构建 Excel 表格保存路径
    file_path = os.path.join(task_path, f"{task_directory}.xls")

    if action_list:
        # 保存文件
        workbook.save(file_path)
        QMessageBox.information(self, "提示", f"文件成功保存为 \"{task_directory}.xls\" 表格", QMessageBox.Ok)
    else:
        QMessageBox.warning(self, "警告", "表格内无任何数据需要保存!", QMessageBox.Ok)
    print(f"文件成功保存在： {file_path}")


def load_from_excel(self, task_dir_name):
    """
    读取 excel 文件中的数据的方法
    :param self:
    :param task_dir_name: 选中的任务名
    :return: action_list[{},{},...]
    """
    global actionList
    # 构建 Excel 文件路径
    excel_path = os.path.join("work/TASKS/", task_dir_name, f"{task_dir_name}.xls")

    # 检查 Excel 文件是否存在
    if not os.path.exists(excel_path) and actionList == []:
        reply = QMessageBox.question(self, "文件不存在", "当前选中的任务 \"{}\" 下无同名 \"{}.xls\" 表格文件，\n是否手动选择表格文件？"
                                     .format(task_dir_name, task_dir_name), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 弹出资源管理器选择文件
            default_path = "work/TASKS/"
            excel_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, '选择 Excel 文件', default_path,
                                                                  'Excel Files (*.xls)')
            if not excel_path:
                return None
        else:
            return None

    try:
        if actionList:
            return actionList
        # 映射中文表头到英文表头的字典
        header_mapping = {
            "操作图": "order",
            "操作类型": "operationType",
            "功能指令": "functionCmd",
            "实例对象": "content",
            "循环次数": "loop",
            "容错次数": "errorLoop",
            "图片路径": "src",
            "是否启用": "isRun",
            "多行重复": "multipleLineRepeat",
            "备注": "desc",
        }

        # 打开 Excel 文件
        workbook = xlrd.open_workbook(excel_path)
        sheet = workbook.sheet_by_index(0)
        # 获取表头
        headers = [header_mapping.get(sheet.cell_value(0, col), sheet.cell_value(0, col)) for col in range(sheet.ncols)]
        # 从第二行开始读取数据
        for row_index in range(1, sheet.nrows):
            action = {}
            for col_index in range(sheet.ncols):
                action[headers[col_index]] = sheet.cell_value(row_index, col_index)
            actionList.append(action)
        print(actionList)
        return actionList
    except Exception as e:
        QMessageBox.warning(self, "错误", f"从 Excel 文件加载数据时出现错误：{str(e)}", QMessageBox.Ok)
        return None
