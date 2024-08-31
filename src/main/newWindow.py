"""
继承自 Ui_MainWindow 的类
"""
import datetime
import os
import re
import shutil
import time
import webbrowser
import xml.etree.ElementTree as ET

import qdarkstyle
import requests
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QTime, QDateTime, QThread, pyqtSignal, QFile, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QHeaderView, QTableWidgetItem, QMenu, QAction, \
    QDialog, QTextBrowser, QAbstractItemView, QVBoxLayout, QDesktopWidget, QFileDialog, QTableWidget
from PyQt5.QtXml import QDomDocument

import src.utils.QSSLoader as QL
import src.utils.checkStr as checkStr
import src.utils.saveAndLoadExcel as sandlexcel
import src.utils.taskAutoGenerateXml as taskAutoGenXml
from src.main.EditCmdWindow import Ui_CmdEditWindow
from src.main.CocoPyRPA_new import Ui_MainWindow
from src.root.funcCmdMain_new import mainWork
from src.utils.ScreenCoordinate import ScreenCoorWidget
from src.utils.Timer import TimingDialog
from src.utils.image_widget import ImageWidget
from src.utils.saveAndLoadExcel import load_from_excel, save_to_excel
from src.utils.screenShot import CaptureScreen

LOGO1 = "      ______                 ____       ____   ____  ___  "
LOGO2 = "     / ____/___  _________  / __ \__ __/ __ \ / __ \/   | "
LOGO3 = "    / /   / __ \/ ___/ __ \/ /_/ / / / / /_/ / /_/ / /| | "
LOGO4 = "   / /___/ /_/ / /__/ /_/ / ____/ /_/ / _, _/ ____/ ___ | "
LOGO5 = "   \____/\____/\___/\____/_/    \__, /_/ |_/_/   /_/  |_| "
LOGO6 = "                               /____/                     "
# 自定义 QMessageBox 弹窗消息字体样式
INFO_STYLE = ["<p align='center'><font color='#0055FF' size='5'>", "</font></p>"]
WANR_STYLE = ["<p align='center'><font color='#FF0000' size='5'>", "</font></p>"]
THEME = 'default'


# 获取表头的文本并映射为对应的英文作为字典的键
def header_text_toEnglish(headerText):
    """
    获取表头的文本并映射为对应的英文作为字典的键
    :param headerText:
    :return: English of headerText
    """
    if headerText == "操作图":
        return "order"
    elif headerText == "操作类型":
        return "operationType"
    elif headerText == "功能指令":
        return "functionCmd"
    elif headerText == "实例对象":
        return "content"
    elif headerText == "循环次数":
        return "loop"
    elif headerText == "容错次数":
        return "errorLoop"
    elif headerText == "图片路径":
        return "src"
    elif headerText == "是否启用":
        return "isRun"
    elif headerText == "多行重复":
        return "multipleLineRepeat"
    elif headerText == "备注":
        return "desc"


# 用正则表达式匹配图片路径的末尾是否为”.png“
def is_png_file(file_path):
    """
    用正则表达式匹配图片路径的末尾是否为”.png“
    :return: True/False
    """
    pattern = re.compile(r'\.png$', re.IGNORECASE)
    return bool(pattern.search(file_path))


class CocoPyRPAApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    主窗口程序实现类
    """
    current_version = "1.2.1"
    print()
    print(LOGO1)
    print(LOGO2)
    print(LOGO3)
    print(LOGO4)
    print(LOGO5)
    print(LOGO6)
    print(f"\t当前版本：CocoPyRPA-GUI版 v{current_version}")
    print("-----------------------------------------------------------")

    def __init__(self, parent=None):
        super(CocoPyRPAApp, self).__init__(parent)
        # 初始化界面

        self.setupUi(self)
        self.editor = None  # cmd指令编辑器类实例
        self.about_dialog = None  # 关于页面显示类实例
        self.feature_dialog = None  # 功能说明页面显示类实例
        self.screenshot = None  # 截图类实例
        self.screenCoorWidget1 = None  # 获取屏幕坐标类的实例 1（获取定点坐标）
        self.screenCoorWidget2 = None  # 获取屏幕坐标类的实例 2（获取相对坐标）
        self.thread = None  # 线程类实例
        self.loadCmdConfig("src/config/CmdConfig.xml")  # 加载 cmd 指令的 XML 配置文件
        # 允许接收拖拽事件
        self.setAcceptDrops(True)
        # 将表格部件的拖放覆盖模式设置为False
        self.tableWidget.setDragDropOverwriteMode(False)
        # 设置拖拽模式为内部移动
        self.tableWidget.setDragDropMode(QAbstractItemView.InternalMove)
        # 设置主窗口标题
        self.setWindowTitle("CocoPyRPA-GUI版 v" + self.current_version)
        # 设置主窗口图标
        self.setWindowIcon(QIcon("res/icons/logo.png"))

        # 创建 ImageWidget 对象并传入图片路径参数
        self.image_widget = ImageWidget(image_path='')

        # 获取“TASKS”目录中的目录列表
        tasks_directory = "work/TASKS"
        directories = [name for name in os.listdir(tasks_directory) if
                       os.path.isdir(os.path.join(tasks_directory, name))]
        # 将目录添加到列表
        self.listWidget.addItems(directories)

        # 设置 QTableWidget 列自适应内容
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 设置列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 手动调整列宽
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # 设置表格整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置表格列标题
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(
            ["操作图", "操作类型", "功能指令", "实例对象", "循环次数", "容错次数", "图片路径", "是否启用",
             "多行重复", "备注"])
        # 设置表格行标题
        # self.tableWidget.setVerticalHeaderLabels(["序号", "序号"])

        # 存储界面表格内的所有 Action 数据到 action_list
        self.action_list = []
        # 存储复制的一行数据
        self.copied_row = []

        '''连接 【菜单项/工具栏】 点击事件到槽函数'''
        self.action_RefreshDir.triggered.connect(self.refreshList)  # 刷新目录列表
        self.action_menu_NewDir.triggered.connect(self.newDirectory)  # 新建任务
        self.action_menu_Open.triggered.connect(self.openTaskDirectory)  # 打开
        self.action_menu_Save.triggered.connect(self.saveTaskToXml)  # 保存
        self.action_menu_SaveToExcel.triggered.connect(self.saveTaskToExcel)  # 另存为 Excel 表格
        self.action_menu_OpenExcel.triggered.connect(self.openTaskFromExcel)  # 加载 Excel 表格

        self.action_menu_checkUpdate.triggered.connect(self.show_update_dialog)  # 检查更新

        # 主题切换
        self.action_menu_defaultTheme.triggered.connect(lambda: self.changeTheme(theme='default'))  # 设置默认主题
        self.action_menu_darkTheme.triggered.connect(lambda: self.changeTheme(theme='dark'))  # 设置深色主题
        self.action_menu_lightTheme.triggered.connect(lambda: self.changeTheme(theme='light'))  # 设置明亮主题
        self.action_menu_protectEyesTheme.triggered.connect(lambda: self.changeTheme(theme='protectEyes'))  # 设置护眼主题

        # 点击菜单项时启动线程
        self.action_menu_RunAll.triggered.connect(self.runAll)  # 运行一次
        self.action_menu_RunOne.triggered.connect(self.runOne)  # 指定运行

        self.action_tool_Copy.triggered.connect(self.copyRow)  # 复制
        self.action_tool_Paste.triggered.connect(self.pasteRow)  # 粘贴
        self.action_tool_Delete.triggered.connect(self.deleteRow)  # 删除

        self.action_tool_Add.triggered.connect(
            lambda: self.addRow(operation_type='', function_cmd='', content=''))  # 增加
        self.action_tool_InsertUp.triggered.connect(self.insertAbove)  # 插入上方
        self.action_tool_InsertDown.triggered.connect(self.insertBelow)  # 插入下方
        self.action_tool_MoveUp.triggered.connect(self.moveUp)  # 上移
        self.action_tool_MoveDown.triggered.connect(self.moveDown)  # 下移
        self.action_tool_screenShot.triggered.connect(self.screenShot)  # 截图
        self.action_about.triggered.connect(self.show_about_dialog)  # 显示关于页面
        self.action_cmdDesc.triggered.connect(self.show_feature_dialog)  # 显示帮助页面

        '''连接【功能指令】到槽函数'''
        # 鼠标
        self.action_menu_LClickOne.triggered.connect(self.left_click_one)  # 单击左键
        self.action_menu_LClickDou.triggered.connect(self.left_click_dou)  # 双击左键
        self.action_menu_RClickOne.triggered.connect(self.right_click_one)  # 单击右键
        self.action_menu_Scroll.triggered.connect(self.my_scroll)  # 滚轮
        self.action_menu_MouseMoveTo.triggered.connect(self.mouse_move_to)  # 鼠标定点移动
        self.action_menu_MouseRelMove.triggered.connect(self.mouse_relative_move)  # 鼠标相对移动
        # 键盘
        self.action_menu_KeyStroke.triggered.connect(self.key_stroke)  # 按键
        self.action_menu_HotkeyCombi.triggered.connect(self.hotkey_combi)  # 热键组合
        self.action_menu_EntTxtOnKeyboard.triggered.connect(self.enter_txt_on_keyboard)  # 键盘输入TXT内容
        # 系统
        self.action_menu_Delay.triggered.connect(self.set_os_delay)  # 延时
        self.action_menu_Timing.triggered.connect(self.set_os_timing)  # 定时
        self.action_menu_Timing.setDisabled(True)  # 暂时禁用定时
        # cmd指令
        self.action_menu_SelfCmd.triggered.connect(self.openCmdEditor)
        # 其它
        self.action_menu_Input.triggered.connect(self.inputFromPasteboard)  # 输入

        # 创建定时器和计数器变量
        self.timer = QTimer(self)
        self.counter = 0
        # 连接定时器的 timeout 信号到槽函数
        self.timer.timeout.connect(self.update_timer)
        # 获取 Text Browser 组件
        self.logBrowser = self.findChild(QTextBrowser, 'logBrowser')

        # 连接目录列表被左键双击事件到槽函数
        self.listWidget.itemDoubleClicked.connect(self.listDoubleClicked)

        # 连接目录列表被右键单击事件到槽函数
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.listWidget_context_menu)

        # 连接表格单元格数据发生改变事件到槽函数
        self.tableWidget.itemChanged.connect(self.cell_changed)

        # 连接双击单元格事件到槽函数
        self.tableWidget.itemDoubleClicked.connect(self.cell_double_clicked)

    # 新建任务目录
    def newDirectory(self):
        """
        新建任务目录的方法（同时会检查输入的目录字符串的合法性）
        """
        print("newDirectory ---> 方法【执行】了！")
        # 弹出对话框，让用户输入新任务的名称
        task_name, ok_pressed = QInputDialog.getText(self, "新建任务", "请输入任务名称:", QLineEdit.Normal, "")
        if ok_pressed and task_name:
            if checkStr.validate_input(task_name):
                parent_path = os.path.abspath('work/TASKS')
                # 构建新任务目录的路径
                task_dir_path = os.path.join(parent_path, task_name)
                # 检查目录是否已经存在
                if os.path.exists(task_dir_path):
                    QMessageBox.warning(self, "警告", f"任务目录 '{task_name}' 已经存在！", QMessageBox.Ok)
                else:
                    try:
                        # 尝试创建新目录
                        os.makedirs(task_dir_path)
                        # 在这里可以添加一些额外的逻辑，例如显示成功消息
                        QMessageBox.information(self, "成功", f"任务 '{task_name}' 创建成功！", QMessageBox.Ok)
                        taskAutoGenXml.create_xml_file(task_dir_path)
                        self.refreshList()
                    except Exception as e:
                        # 如果目录创建失败，显示错误消息
                        QMessageBox.warning(self, "错误", f"无法创建任务目录:\n{str(e)}", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "错误", "目录名称包含不允许的字符 ('/' 或 '\\')", QMessageBox.Ok)
        print("newDirectory ---> 方法【完成】了！")

    # 删除选中的任务目录
    def deleteDirectory(self):
        """
        删除任务目录的方法
        """
        print("deleteTaskDirectory ---> 方法【执行】了！")

        # 弹出对话框，让用户确认是否删除任务目录
        reply = QMessageBox.question(self, "确认删除", "确定要删除任务目录吗？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 获取当前在任务列表内选中的任务名字
            current_item = self.listWidget.currentItem()
            if current_item is not None:
                selected_dir_name = current_item.text()
                # 构建任务目录的路径
                parent_path = os.path.abspath('work/TASKS')
                task_dir_path = os.path.join(parent_path, selected_dir_name)
                try:
                    # 尝试删除目录
                    shutil.rmtree(task_dir_path)
                    # 显示删除成功消息
                    QMessageBox.information(self, "成功", f"任务目录 \"{selected_dir_name}\" 删除成功！", QMessageBox.Ok)
                    self.refreshList()
                except Exception as e:
                    # 如果目录删除失败，显示错误消息
                    QMessageBox.warning(self, "错误", f"无法删除任务目录:\n{str(e)}", QMessageBox.Ok)

    # 重命名选中的任务目录
    def renameDirectory(self):
        """
        重命名选中的任务目录的方法
        """
        print("renameTaskDirectory ---> 方法【执行】了！")

        # 获取当前在任务列表内选中的任务名字
        current_item = self.listWidget.currentItem()
        if current_item is not None:
            selected_dir_name = current_item.text()
            # 弹出对话框，让用户输入新的目录名称
            new_dir_name, ok = QInputDialog.getText(self, "重命名", "请输入新的任务名称:", QLineEdit.Normal,
                                                    selected_dir_name)
            if checkStr.validate_input(new_dir_name):
                if ok and new_dir_name:
                    # 构建任务目录的路径
                    parent_path = os.path.abspath('work/TASKS')
                    old_task_dir_path = os.path.join(parent_path, selected_dir_name)
                    new_task_dir_path = os.path.join(parent_path, new_dir_name)
                    try:
                        # 尝试重命名目录
                        os.rename(old_task_dir_path, new_task_dir_path)
                        # 显示重命名成功消息
                        QMessageBox.information(self, "成功",
                                                f"任务 '{selected_dir_name}' 重命名为 '{new_dir_name}' 成功！",
                                                QMessageBox.Ok)
                        self.refreshList()
                    except Exception as e:
                        # 如果目录重命名失败，显示错误消息
                        QMessageBox.warning(self, "错误", f"无法重命名任务:\n{str(e)}", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "错误", "目录名称包含不允许的字符 ('/' 或 '\\')", QMessageBox.Ok)

    # 打开任务目录
    def openTaskDirectory(self):
        """
        打开任务目录的方法
        """
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "work/TASKS")
        # 打印所选文件夹的路径
        print("选择的文件夹路径：", folder_path)

    # 保存任务到 xml 配置文件
    def saveTaskToXml(self):
        """
        保存任务到 xml 配置文件
        """
        # 清空 action_list 列表
        self.action_list.clear()
        # 遍历表格的所有行
        for row in range(self.tableWidget.rowCount()):
            # 创建一个字典保存当前行的数据
            data = {}
            # 遍历当前行的所有列
            for col in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(row, col):
                    # 获取当前单元格的文本
                    cell_text = self.tableWidget.item(row, col).text()
                    # 获取表头的文本作为字典的键
                    header_text = self.tableWidget.horizontalHeaderItem(col).text()
                    headerText = header_text_toEnglish(header_text)
                    # 将数据存入字典
                    data[headerText] = cell_text
                else:
                    print("action_list.tableWidget.item() 为 None")
            # 将当前行的字典添加到 action_list 列表
            self.action_list.append(data)

        # 输出保存的数据（可选）
        for row in range(len(self.action_list)):
            print(self.action_list[row])

        # 获取当前在任务列表内选中的任务名字
        current_item = self.listWidget.currentItem()
        if current_item is not None:
            selected_dir_name = current_item.text()
            print("\n选中的目录名字:", selected_dir_name)
            try:
                self.generate_xml(actionList=self.action_list, saveDir=selected_dir_name)
            except Exception as e:
                QMessageBox.warning(self, "错误", f"保存为xml配置文件时出现错误：{str(e)}", QMessageBox.Ok)

    # 指令内容另存至 Excel 表格
    def saveTaskToExcel(self):
        """
        指令内容另存至 Excel 表格的方法
        """
        print("saveTaskToExcel ---> 方法【执行】了！")

        # 清空 action_list 列表
        self.action_list.clear()
        # 遍历表格的所有行
        for row in range(self.tableWidget.rowCount()):
            # 创建一个字典保存当前行的数据
            data = {}
            # 遍历当前行的所有列
            for col in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(row, col):
                    # 获取当前单元格的文本
                    cell_text = self.tableWidget.item(row, col).text()
                    # 获取表头的文本作为字典的键
                    header_text = self.tableWidget.horizontalHeaderItem(col).text()
                    headerText = header_text_toEnglish(header_text)
                    # 将数据存入字典
                    data[headerText] = cell_text
                else:
                    print("action_list.tableWidget.item() 为 None")
                    cell_text = None  # 指定内容为 None
                    # 获取表头的文本作为字典的键
                    header_text = self.tableWidget.horizontalHeaderItem(col).text()
                    headerText = header_text_toEnglish(header_text)
                    # 将数据存入字典
                    data[headerText] = cell_text

            # 将当前行的字典添加到 action_list 列表
            self.action_list.append(data)
        # 输出保存的数据（可选）
        for row in range(len(self.action_list)):
            print(self.action_list[row])

        # 获取当前在任务列表内选中的任务名字
        current_item = self.listWidget.currentItem()
        if current_item is not None:
            selected_dir_name = current_item.text()
            print("\n选中的目录名字:", selected_dir_name)
            save_to_excel(self, action_list=self.action_list, task_directory=selected_dir_name)

    # 加载 Excel 表格指令内容
    def openTaskFromExcel(self):
        """
        加载 Excel 表格指令内容的方法
        """
        print("openTaskFromExcel ---> 方法【执行】了！")

        # QMessageBox.information(self, "提示", "【加载 Excel 表格】 -- 菜单项被点击了！", QMessageBox.Ok)
        # 获取当前在任务列表内选中的任务名字
        current_item = self.listWidget.currentItem()
        if current_item is not None:
            selected_dir_name = current_item.text()
            print("\n选中的目录名字:", selected_dir_name)
            if load_from_excel(self, selected_dir_name) is not None:
                self.action_list = load_from_excel(self, selected_dir_name)
                # 归零
                sandlexcel.actionList = []
                QMessageBox.information(self, "提示", "成功加载表格数据到任务 \"{}\"".format(selected_dir_name),
                                        QMessageBox.Ok)
                print("加载的 Excel 数据如下：")
                for action in self.action_list:
                    print(action)

                # 清空表格
                self.tableWidget.clearContents()
                # 设置表格列数和行数
                self.tableWidget.setColumnCount(10)  # 根据表头的列数设置
                self.tableWidget.setRowCount(len(self.action_list))
                # 设置表头
                headers = ["操作图", "操作类型", "功能指令", "实例对象", "循环次数", "容错次数", "图片路径", "是否启用",
                           "多行重复", "备注"]
                self.tableWidget.setHorizontalHeaderLabels(headers)
                # 将数据填充到表格中
                for row, action_data in enumerate(self.action_list):
                    for col, (key, value) in enumerate(action_data.items()):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget.setItem(row, col, item)
                        self.tableWidget.setRowHeight(row, 56)  # 设置行高

    '''
    ##########################################################################
    #                        以下为工具栏【功能指令】对应方法
    ##########################################################################
    '''

    # 操作 -- 鼠标 -- 单击左键
    def left_click_one(self):
        """
        鼠标单击左键
        """
        self.addRow(operation_type='鼠标', function_cmd='单击左键', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 鼠标 -- 双击左键
    def left_click_dou(self):
        """
        鼠标双击左键
        """
        self.addRow(operation_type='鼠标', function_cmd='双击左键', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 鼠标 -- 单击右键
    def right_click_one(self):
        """
        鼠标单击右键
        """
        self.addRow(operation_type='鼠标', function_cmd='单击右键', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 鼠标 -- 滚轮
    def my_scroll(self):
        """
        鼠标滚轮滑动
        """
        self.addRow(operation_type='鼠标', function_cmd='滚轮', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 鼠标 -- 鼠标定点移动
    def mouse_move_to(self):
        """
        鼠标移动到指定位置
        """
        QMessageBox.information(self, "信息",
                                "请点击屏幕上要定点移动的位置\n退出请连按鼠标右键")
        # 获取相对坐标类的实例
        self.screenCoorWidget1 = ScreenCoorWidget(1)
        # 接收信号连接槽函数
        self.screenCoorWidget1.relCoordinatesChanged.connect(self.onCoordinatesChanged)
        self.screenCoorWidget1.show()  # 显示窗口
        self.screenCoorWidget1.start_capture()  # 开始捕获

    # 操作 -- 鼠标 -- 鼠标相对移动
    def mouse_relative_move(self):
        """
        鼠标相对移动
        """
        QMessageBox.information(self, "提示",
                                "请点击屏幕上的两个坐标，\n第一个点击的是当前坐标，\n第二个点击的是目标坐标，\n程序会自动计算相对坐标\n退出请连按鼠标右键")
        # 获取相对坐标类的实例
        self.screenCoorWidget2 = ScreenCoorWidget(2)
        # 接收信号连接槽函数
        self.screenCoorWidget2.relCoordinatesChanged.connect(self.onRelCoordinatesChanged)
        self.screenCoorWidget2.show()  # 显示窗口
        self.screenCoorWidget2.start_capture()  # 开始捕获

    # 操作 -- 键盘 -- 按键
    def key_stroke(self):
        """
        键盘单个按键按下和释放
        """
        self.addRow(operation_type='键盘', function_cmd='按键', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/keyboard.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 键盘 -- 热键组合
    def hotkey_combi(self):
        """
        热键组合
        """
        self.addRow(operation_type='键盘', function_cmd='热键组合', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/keyboard.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 键盘 -- 键盘输入TXT内容
    def enter_txt_on_keyboard(self):
        """
        键盘输入TXT内容
        """
        self.addRow(operation_type='键盘', function_cmd='键盘输入TXT内容', content='')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/keyboard.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 系统 -- 延时
    def set_os_delay(self):
        """
        系统延时
        """
        # 系统延时
        self.addRow(operation_type='系统', function_cmd='延时', content='1')
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/OS.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 操作 -- 系统 -- 定时
    def set_os_timing(self):
        """
        系统定时
        """
        # 创建并显示设置定时的窗口
        timing_dialog = TimingDialog(self)
        if timing_dialog.exec_() == QDialog.Accepted:
            # 用户点击确认按钮，获取设置的时间
            target_time_str = timing_dialog.time_edit.time().toString('HH:mm:ss')
            print(target_time_str)
            # 将设置的时间填入表格
            self.addRow(operation_type='系统', function_cmd='定时', content=target_time_str)

            # # 将时间字符串转换为 QTime 对象
            # target_time = QTime.fromString(target_time_str, 'HH:mm:ss')
            # print(target_time)
            # # 计算倒计时的初始值
            # current_time = QTime.currentTime()  # 当前时间
            # delay = current_time.msecsTo(target_time)
            # print("当前时间：", current_time)
            # # 设置定时器的定时时间
            # self.timer.start(1000)

    def set_os_timing1(self):
        """
        系统定时
        """
        # 创建 TimingDialog 对象
        timing_dialog = TimingDialog(self)
        result = timing_dialog.exec_()

        if result == QDialog.Accepted:
            # 获取用户选择的时间
            target_time = timing_dialog.time_edit.time()

            # 计算延时
            current_time = QDateTime.currentDateTime()
            target_datetime = QDateTime(current_time.date(), target_time)
            if current_time.time() > target_time:
                target_datetime = target_datetime.addDays(1)  # 如果目标时间早于当前时间，延时到明天同一时间

            delay = current_time.msecsTo(target_datetime)

            # 启动定时器
            self.timer.start(delay)

            # 在 Text Browser 中显示定时信息
            self.logBrowser.append(f"下一步操作定时时间为：{target_datetime.toString('yyyy-MM-dd hh:mm:ss')}")

    # 操作 -- cmd指令 -- 加载指令菜单
    def loadCmdConfig(self, xml_path):
        """
        加载 cmd 指令菜单
        :param xml_path: cmd指令的 xml 配置文件路径
        """
        doc = QDomDocument()
        file = QFile(xml_path)
        if not file.open(QIODevice.ReadOnly):
            return False
        if not doc.setContent(file):
            file.close()
            return False
        file.close()
        # 获取根元素，即 <CMD>
        root = doc.documentElement()
        # 获取第一个子元素，即第一个 <Item>
        node = root.firstChild()
        while not node.isNull():  # 遍历所有的 <Item>
            element = node.toElement()  # 将节点转换为元素
            if not element.isNull():
                _key = element.attribute("Key")  # 获取 Key 属性
                _value = element.attribute("Value")  # 获取 Value 属性
                _desc = element.attribute("Desc")  # 获取 Desc 属性
                # 创建三级菜单
                action = self.menu_cmd.addAction(_key)
                action.setStatusTip(_desc)
                # 设置槽函数，传递 Value 参数
                action.triggered.connect(lambda checked, key=_key, value=_value: self.executeCmd(key, value))
            node = node.nextSibling()  # 获取下一个兄弟元素，即下一个 <Item>

    # 操作 -- 其它 -- 输入
    def inputFromPasteboard(self):
        """
        添加 <输入> 指令
        """
        self.addRow(operation_type='其它', function_cmd='输入', content='')

    '''
    ##########################################################################
    #                      以下为工具栏【表格操作】对应方法
    ##########################################################################
    '''

    # 运行一次
    def runAll(self):
        """
        运行一次
        """
        if self.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "警告", "表格为空，无法执行！", QMessageBox.Ok)
            return
        # QMessageBox.information(self, "提示", "【运行一次】 -- 菜单项被点击了！", QMessageBox.Ok)
        # 实例化线程对象，传入 QTableWidget 的实例对象 tableWidget，设置 action='run_all'
        self.thread = WorkThread(tableWidget=self.tableWidget, action='run_all', logBrowser=self.logBrowser)
        # 连接线程的信号和槽函数
        self.thread.trigger.connect(self.displayLog)
        # 窗口最小化
        self.showMinimized()
        # 启动线程
        self.thread.start()
        # 禁用菜单项 [运行一次] 和 [指定运行]
        self.action_menu_RunAll.setDisabled(True)
        self.action_menu_RunOne.setDisabled(True)
        # 清除日志
        self.clearLog()

        # 窗口恢复正常
        self.thread.finished.connect(self.window_normal)
        # 线程结束后启用菜单项 [运行一次] 和 [指定运行]
        self.thread.finished.connect(self.enable_runAll)
        self.thread.finished.connect(self.enable_runOne)

    # 指定运行
    def runOne(self):
        """
        指定运行
        """
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请先选中一行数据！", QMessageBox.Ok)
            return
        # QMessageBox.information(self, "提示", "【指定运行】 -- 菜单项被点击了！", QMessageBox.Ok)
        # 实例化线程对象，传入 QTableWidget 的实例对象 tableWidget，设置 action='run_one'
        self.thread = WorkThread(tableWidget=self.tableWidget, action='run_one', logBrowser=self.logBrowser)
        # 连接线程的信号和槽函数
        self.thread.trigger.connect(self.displayLog)
        # 窗口最小化
        self.showMinimized()
        # 启动线程
        self.thread.start()
        # 禁用菜单项 [运行一次] 和 [指定运行]
        self.action_menu_RunOne.setDisabled(True)
        self.action_menu_RunAll.setDisabled(True)
        # 清除日志
        self.clearLog()

        # 窗口恢复正常
        self.thread.finished.connect(self.window_normal)
        # 线程结束后启用菜单项 [运行一次] 和 [指定运行]
        self.thread.finished.connect(self.enable_runOne)
        self.thread.finished.connect(self.enable_runAll)

    # 复制一行
    def copyRow(self):
        """
        复制一行
        """
        selected_items = self.tableWidget.selectedItems()
        print("复制操作选中的是：", selected_items)
        if selected_items:
            selected_row = selected_items[0].row()
            copied_row = []
            for col in range(self.tableWidget.columnCount()):
                action_data_item = self.tableWidget.item(selected_row, col)
                if action_data_item:
                    action_data = action_data_item.text()
                    copied_row.append(action_data)
                else:
                    copied_row.append(None)
            self.copied_row = copied_row
            print("复制的一行数据为：", copied_row)

    # 粘贴一行
    def pasteRow(self):
        """
        粘贴一行
        """
        if self.copied_row:
            selected_items = self.tableWidget.selectedItems()
            print("粘贴操作选中的是：", selected_items)
            if selected_items:
                selected_row = selected_items[0].row()
                for col, value in enumerate(self.copied_row):
                    item = QTableWidgetItem(value)
                    self.tableWidget.setItem(selected_row, col, item)

    # 删除一行
    def deleteRow(self):
        """
        删除一行
        """
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.tableWidget.removeRow(selected_row)

    # 增加
    def addRow(self, operation_type, function_cmd, content):
        """
        增加 Action 数据项
        """
        # order = str(action_list.tableWidget.rowCount() + 1)  # 序号
        operation_type = operation_type  # 操作类型
        function_cmd = function_cmd  # 功能指令
        content = content  # 实例对象
        loop = '1'  # 循环次数
        error_loop = '1'  # 容错次数
        src = "无"  # 图片路径（默认为‘无’）
        is_run = "1"  # 是否启用（默认启用（1启用  0停用））
        multiple_lineRepeat = "目标行,重复次数"  # 多行重复(格式为”目标行,重复次数“)
        desc = "无"  # 备注
        print(
            "OperationType={},FunctionCmd={},Content={},Loop={},ErrorLoop={},Src={},IsRun={},MultipleLineRepeat={},Desc={}"
            .format(operation_type, function_cmd, content, loop, error_loop, src, is_run, multiple_lineRepeat, desc))

        data = {
            # "order": order,
            "operationType": operation_type,
            "functionCmd": function_cmd,
            "content": content,
            "loop": loop,
            "error_loop": error_loop,
            "src": src,
            "isRun": is_run,
            "multiple_lineRepeat": multiple_lineRepeat,
            "desc": desc
        }

        self.tableWidget.insertRow(self.tableWidget.rowCount())
        for col, (key, value) in enumerate(data.items()):
            item = QTableWidgetItem(value)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, col + 1, item)
            self.tableWidget.setRowHeight(self.tableWidget.rowCount() - 1, 56)

    # 插入上方
    def insertAbove(self):
        """
        插入上方
        """
        print("insertAbove ---> 方法执行了！")
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.tableWidget.insertRow(selected_row)
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                self.tableWidget.setItem(selected_row, col, item)
            self.tableWidget.setRowHeight(selected_row, 56)

    # 插入下方
    def insertBelow(self):
        """
        插入下方
        """
        print("insertBelow ---> 方法执行了！")
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.tableWidget.insertRow(selected_row + 1)
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                self.tableWidget.setItem(selected_row + 1, col, item)
            self.tableWidget.setRowHeight(selected_row + 1, 56)

    # 上移
    def moveUp(self):
        """
        将当前选中的一行数据 上移
        """
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            print("******选中的一行为: ", selected_row)
            if selected_row > 0:
                self.swap_rows(selected_row, selected_row - 1)

    # 下移
    def moveDown(self):
        """
        将当前选中的一行数据 下移
        """
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            if selected_row < self.tableWidget.rowCount() - 1:
                self.swap_rows(selected_row, selected_row + 1)

    # 截图
    def screenShot(self):
        """
        截图
        """
        self.screenshot = CaptureScreen()  # 截图类实例
        # # 窗口最小化
        # self.showMinimized()
        # time.sleep(1)
        self.screenshot.show()

    # 显示关于页面
    def show_about_dialog(self):
        """
        关于
        """
        print("about ---> 方法执行了！")
        html_path = 'template/static/about.html'
        self.about_dialog = AboutDialog(html_path)
        self.about_dialog.show()

    # 显示功能介绍页面
    def show_feature_dialog(self):
        """
        功能介绍
        """
        print("show_feature_dialog ---> 方法执行了！")
        html_path = 'template/static/feature.html'
        self.feature_dialog = FeatureDialog(html_path)
        self.feature_dialog.show()

    # 刷新目录列表
    def refreshList(self):
        """
        刷新目录列表
        """
        print("refreshList ---> 方法【执行】了！")
        # 清除列表内容
        self.listWidget.clear()
        # 获取“TASKS”目录中的目录列表
        tasks_directory = "work/TASKS"
        directories = [name for name in os.listdir(tasks_directory) if
                       os.path.isdir(os.path.join(tasks_directory, name))]
        # 将目录添加到列表小组件
        self.listWidget.addItems(directories)
        # print("refreshList ---> 方法【完成】了！")

    '''
    ################################################################################
    #                                 以下为其它方法
    ################################################################################
    '''

    # 检查更新
    def get_github_version(self):
        """
        检查 github 上的最新版本，并与当前版本进行比较
        :return: latest_version:
        """
        github_api_url = 'https://api.github.com/repos/{owner}/{repo}/releases/latest'
        owner = '54Coconi'
        repo = 'CocoPyRPA-QT'

        try:
            response = requests.get(github_api_url.format(owner=owner, repo=repo))
            if response.status_code == 200:
                data = response.json()
                latest_version = data['tag_name'].split('v')[-1]
                print("Latest version: ", latest_version)
                if latest_version > self.current_version:
                    return latest_version
                else:
                    QMessageBox.information(self, "更新", "当前已是最新版本")
                    return None
            else:
                return None
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "错误", "无法从 GitHub API 获取版本信息。")
            return None

    # 显示更新信息对话框
    def show_update_dialog(self):
        """
        显示更新信息对话框
        """
        if self.get_github_version():
            msg = f"有新版本 ({self.get_github_version()}) 可用，你想更新吗？"
            reply = QMessageBox.question(self, "可用更新", msg, QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                # 让用户跳转到浏览器下载链接
                webbrowser.open("https://github.com/54Coconi/CocoPyRPA-QT/releases/")
                # 这里可以添加下载更新文件和安装更新的代码
                QMessageBox.information(self, "更新", "下载完成后，请解压后覆盖整个软件根目录。")

    # 目录列表双击事件方法
    def listDoubleClicked(self):
        """
        目录列表双击事件方法，双击目录项后加载该目录下的配置文件 ”CocoPyRPATask.xml“ 到表格
        """
        selected_directory = self.listWidget.currentItem().text()
        print("\n任务目录 \"{}\" 被选中".format(selected_directory))
        xml_file_path = os.path.join('work/TASKS/' + selected_directory, 'CocoPyRPATask.xml')

        if os.path.exists(xml_file_path):
            tree = ET.parse(xml_file_path)
            root = tree.getroot()

            # 清空表格
            self.tableWidget.clear()

            # 设置表格的行数和列数
            row = len(root)
            if row != 0:
                self.tableWidget.setRowCount(row)
                col = len(root[0].attrib)
                self.tableWidget.setColumnCount(col)
                # 设置表头标签名
                self.tableWidget.setHorizontalHeaderLabels(
                    ["操作图", "操作类型", "功能指令", "实例对象", "循环次数", "容错次数", "图片路径", "是否启用",
                     "多行重复", "备注"])

                # 获取 XML 文件中的属性名
                header_labels = [attr for attr in root[0].attrib.keys()]  # if attr != "Order" 减去 "Order" 属性

                # 填充表格内容
                for row, action in enumerate(root):
                    for col, attr_name in enumerate(header_labels):
                        if col != 0:  # 第一列 “Order” 不显示
                            attr_value = action.get(attr_name, "")
                            item = QTableWidgetItem(attr_value)
                            self.tableWidget.setItem(row, col, item)
                            self.tableWidget.setRowHeight(row, 56)  # 设置表格的行高为 56 个像素
                        else:
                            item = QTableWidgetItem('')
                            self.tableWidget.setItem(row, 0, item)
                            self.tableWidget.setRowHeight(row, 56)
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(10)
                # 设置表头标签名
                self.tableWidget.setHorizontalHeaderLabels(
                    ["操作图", "操作类型", "功能指令", "实例对象", "循环次数", "容错次数", "图片路径", "是否启用",
                     "多行重复", "备注"])
                QMessageBox.information(self, "提示", "配置文件无数据！", QMessageBox.Ok)
        else:
            print(f"文件 {xml_file_path} 不存在！")
            QMessageBox.warning(self, "警告", f"文件 {xml_file_path} 不存在!", QMessageBox.Ok)

    # 目录列表右键菜单的槽函数
    def listWidget_context_menu(self, position):
        """
        目录列表右键菜单的槽函数，包括 "新建任务", "删除任务", "重命名"
        :param position:
        """
        # 创建右键菜单
        context_menu = QMenu(self)
        # 右键菜单项 -- 新建任务
        new_task_action = QAction("新建任务", self)
        new_task_action.triggered.connect(self.newDirectory)
        context_menu.addAction(new_task_action)
        # 右键菜单项 -- 删除任务
        new_task_action = QAction("删除任务", self)
        new_task_action.triggered.connect(self.deleteDirectory)
        context_menu.addAction(new_task_action)
        # 右键菜单项 -- 重命名
        rename_task_action = QAction("重命名", self)
        rename_task_action.triggered.connect(self.renameDirectory)
        context_menu.addAction(rename_task_action)
        # 显示右键菜单
        context_menu.exec_(self.listWidget.mapToGlobal(position))

    # 单元格内容发生改变事件的处理方法
    def cell_changed(self, item):
        """
        单元格内容发生改变事件的处理方法
        :param item:
        """
        # 获取修改的单元格的行和列
        row = item.row()
        col = item.column()

        print("第 {} 行，第 {} 列的值变为“{}“ ".format(row + 1, col + 1, item.text()))
        image_src = self.tableWidget.item(row, 6)
        operation_type = self.tableWidget.item(row, 1)
        function_cmd = self.tableWidget.item(row, 2)
        if operation_type is not None:
            # 判断当前行的第2列的操作类型是否为“鼠标”
            if operation_type.text() == "鼠标":
                # 判断当前行的第7列单元格是否为空（即没有被创建或没有内容）
                if image_src is not None:
                    # 获取当前行的第7列的【图片路径】的值
                    image = image_src.text()
                    # 图片路径存在时(判断后缀是否为 .png 格式)
                    if os.path.exists(image) and is_png_file(image):
                        # 判断功能指令是否需要图片
                        if function_cmd is not None and (
                                function_cmd.text() == "单击左键" or
                                function_cmd.text() == "单击右键" or
                                function_cmd.text() == "双击左键"):
                            image_widget = ImageWidget(image)
                            self.tableWidget.setCellWidget(row, 0, image_widget)
                            if self.tableWidget.item(row, 3).text() != "图片":
                                self.tableWidget.item(row, 3).setText("图片")  # 设置默认值
                        # else:
                        #     QMessageBox.warning(self, "警告",
                        #                         "此功能无需图片！\n满足条件的功能为<单击左键><双击左键><单击右键>",
                        #                         QMessageBox.Ok)
                    # 图片路径不存在时
                    else:
                        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
                        self.tableWidget.setCellWidget(row, 0, image_widget)  # 设置默认图片
                        if image_src.text() != "无":
                            image_src.setText("无")  # 设置默认路径值
            elif operation_type.text() == "键盘":
                if image_src is not None:
                    image_widget = ImageWidget('res/actionDefaultImages/keyboard.png')
                    self.tableWidget.setCellWidget(row, 0, image_widget)
                    if image_src.text() != "无":
                        image_src.setText("无")
            elif operation_type.text() == "系统":
                if image_src is not None:
                    image_widget = ImageWidget('res/actionDefaultImages/OS.png')
                    self.tableWidget.setCellWidget(row, 0, image_widget)
                    if image_src.text() != "无":
                        image_src.setText("无")
            elif operation_type.text() == "cmd指令":
                if image_src is not None:
                    image_widget = ImageWidget('res/actionDefaultImages/cmd.png')
                    self.tableWidget.setCellWidget(row, 0, image_widget)
                    if image_src.text() != "无":
                        image_src.setText("无")
            elif operation_type.text() == "其它":
                if image_src is not None:
                    image_widget = ImageWidget('res/actionDefaultImages/other.png')
                    self.tableWidget.setCellWidget(row, 0, image_widget)
                    if image_src.text() != "无":
                        image_src.setText("无")
            else:
                # 操作指令（operation_type）内容为空时，此方法不弹窗警告，避免频繁警告
                if operation_type.text() != "":
                    QMessageBox.warning(self, "警告", "第 {} 行，第 1 列的操作类型 \"{}\" 错误！"
                                        .format(row + 1, operation_type.text()))
        else:
            print("第 {} 行，第 1 列的值为 None！".format(row + 1))

    # 生成 action_list 列表对应的 xml 文件的方法
    def generate_xml(self, actionList, saveDir):
        """
        生成 action_list 指令列表对应的 xml 文件的方法
        """
        root = ET.Element("PyRPACode")

        for i, data in enumerate(actionList):
            order = str(i + 1)
            operationType = data["operationType"]
            functionCmd = data["functionCmd"]
            content = data["content"]
            loop = data["loop"]
            errorLoop = data["errorLoop"]
            src = data["src"]
            isRun = data["isRun"]
            multipleLineRepeat = data["multipleLineRepeat"]
            desc = data["desc"]
            # 将数据依次赋给 Action 的每个元素对应的属性值
            action = ET.SubElement(root, "Action")
            action.set("Order", order)
            action.set("OperationType", operationType)
            action.set("Type", functionCmd)
            action.set("Content", content)
            action.set("Loop", loop)
            action.set("ErrorLoop", errorLoop)
            action.set("Src", src)
            action.set("IsRun", isRun)
            action.set("MultipleLineRepeat", multipleLineRepeat)
            action.set("Desc", desc)
        tree = ET.ElementTree(root)

        # save_dir = QFileDialog.getExistingDirectory(action_list, '选择保存目录')
        save_dir = 'work/TASKS/' + saveDir
        if save_dir:
            save_path = os.path.join(save_dir, "CocoPyRPATask.xml")
            tree.write(save_path, encoding="utf-8", xml_declaration=True)
            QMessageBox.information(self, "保存成功", "配置文件生成成功！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "保存失败", "未选择保存路径！")

    # 交换两行数据的方法
    def swap_rows(self, row1, row2):
        """
        交换上下相邻两行数据的方法
        :param row1:
        :param row2:
        """
        columnCount = self.tableWidget.columnCount()
        list1 = [None]
        list2 = [None]
        # 循环遍历需要交换数据的两行指令，并将数据存入临时列表(注意从第2列开始遍历，第1列已经赋值为 None)
        for col in range(1, columnCount):
            item1 = self.tableWidget.item(row1, col)  # 获取 row1 行所有单元格数据
            item2 = self.tableWidget.item(row2, col)  # 获取 row2 行所有单元格数据
            if item1 and item2:  # 判断单元格是否为空
                value1 = item1.text()
                list1.append(value1)
                # print(f"{row1+1}行 ，{col+1}列的值 value1 = {value1}")
                value2 = item2.text()
                list2.append(value2)
                # print(f"{row2+1}行 ，{col+1}列的值 value2 = {value2}")
        # print(f"list1 = {list1}")
        # print(f"list2 = {list2}")
        # 将临时列表的数据交换赋给对应的行
        for col in range(columnCount):
            item1 = self.tableWidget.item(row1, col)
            if item1:  # 判断单元格是否为空
                item1.setText(list2[col])

        for col in range(columnCount):
            item2 = self.tableWidget.item(row2, col)
            if item2:  # 判断单元格是否为空
                item2.setText(list1[col])

    # 单元格被双击触发的函数
    def cell_double_clicked(self, item):
        """
        单元格被双击触发的函数，用于预览图片
        """
        # 获取双击的单元格的行和列
        row = item.row()
        col = item.column()
        print("第 {} 行，第 {} 列被双击了！".format(row + 1, col + 1))
        # 若为第 1 列单元格
        if col == 0:
            # 获取图片路径
            src_item = self.tableWidget.item(row, 6)
            if src_item is not None and src_item.text() != "无":
                # 获取 ”图片路径“ 一列对应单元格的图片路径
                image_path = src_item.text()
                print("第 {} 行，第 7 列的图片路径为 \"{}\" ".format(row + 1, image_path))
                # 显示图片预览窗口
                self.image_widget.set_image_for_preview(image_path)
                self.image_widget.show()
            else:
                print("第 {} 行，第 7 列的图片路径为 \"无/空\" ".format(row + 1))

        # 获取单元格的文本内容
        cell_text = item.text()
        print(f"双击单元格 ({row + 1}, {col + 1}) 内容为: {cell_text}")

    # 定时器的槽函数
    def update_timer(self):
        """
        定时器槽函数，用于更新倒计时和显示状态
        """
        # 获取 Text Browser 组件
        logBrowser = self.logBrowser

        # 计算倒计时
        remaining_time = self.timer.remainingTime()  # 剩余时间（毫秒）
        remaining_time_secs = remaining_time // 1000  # 剩余时间（秒）

        if remaining_time > 0:
            # 更新倒计时状态
            formatted_time = QTime(0, 0).addSecs(remaining_time_secs).toString('HH:mm:ss')
            logBrowser.setText(f"距离下一步操作还剩 {formatted_time}")
            # 在这里添加你需要执行的操作

        else:
            # 倒计时结束时执行的操作
            logBrowser.setText("倒计时结束，执行下一步操作")
            self.timer.stop()

    # 图片拖入表格事件
    def dragEnterEvent(self, event):
        """
        重写dragEnterEvent方法，判断拖拽的数据是否为文件，如果是则接受拖拽事件
        :param event:
        """
        if event.mimeData().hasUrls():  # 判断拖拽的数据是否为URL
            event.acceptProposedAction()  # 接受拖拽事件
        else:
            super().dragEnterEvent(event)

    # 拖入结束事件
    def dropEvent(self, event):
        """
        重写 dropEvent 方法，将文件路径添加到表格中
        :param event:
        """
        if event.mimeData().hasUrls():  # 判断拖拽的数据是否为URL
            for url in event.mimeData().urls():
                if url.isLocalFile():  # 判断URL是否为本地文件
                    # 获取当前行标
                    row = self.tableWidget.currentRow()
                    # 将文件路径添加到表格的第7列
                    self.tableWidget.setItem(row, 6, QTableWidgetItem(url.toLocalFile()))
                    print("拖入的文件路径为：", url.toLocalFile())
                    if not is_png_file(url.toLocalFile()):
                        QMessageBox.warning(self, "警告", "图片格式必须为”.png“!", QMessageBox.Ok, QMessageBox.NoButton)
            event.acceptProposedAction()  # 接受拖拽事件
        else:
            super().dropEvent(event)

    def setSelectionBehavior(self, SelectRows):
        pass

    # 在 logBrowser 文本区域显示日志信息
    def displayLog(self, msg):
        """
        显示日志信息
        :param msg: list 类型的消息
        """
        # 在 logBrowser 中添加信息
        self.logBrowser.append(f"<p>"
                               f"<font color='{msg[0]}' size='4'>" +
                               str(msg[1])
                               + "</font>"
                                 "</p>")
        # self.logBrowser.append("<font color='{}'>".format(msg[0]) + msg[1] + "<font>")

    # 清除 logBrowser 里的日志信息
    def clearLog(self):
        """
        清除 logBrowser 里的日志信息
        """
        self.logBrowser.clear()

    # 启用菜单项 [运行一次]
    def enable_runAll(self):
        """
        启用菜单项 [运行一次]
        """
        self.action_menu_RunAll.setDisabled(False)

    # 启用菜单项 [指定运行]
    def enable_runOne(self):
        """
        启用菜单项 [指定运行]
        """
        self.action_menu_RunOne.setDisabled(False)

    # 相对坐标改变信号连接的槽函数
    def onRelCoordinatesChanged(self, rel_coordinates):
        """
        处理相对坐标变化的槽函数
        :param rel_coordinates: 相对坐标值
        """
        print("【相对坐标为】:", rel_coordinates)
        self.addRow(operation_type='鼠标', function_cmd='鼠标相对移动', content=str(rel_coordinates))

        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 定点坐标改变信号连接的槽函数
    def onCoordinatesChanged(self, coordinates):
        """
        处理定点坐标变化的槽函数
        :param coordinates: 定点坐标值
        """
        print("【定点坐标为】:", coordinates)
        self.addRow(operation_type='鼠标', function_cmd='鼠标定点移动', content=str(coordinates))

        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/mouse.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    # 打开自定义cmd指令编辑器的方法
    def openCmdEditor(self):
        """
        打开自定义cmd指令编辑器的方法
        """
        # 创建一个编辑器窗口
        self.editor = EditorWindow()
        # 显示编辑器窗口
        self.editor.show()

    # 执行 cmd 指令的方法
    def executeCmd(self, key, value):
        """
        执行 cmd 指令的方法
        :param key: 指令名
        :param value: 指令值
        """
        print(f"执行cmd指令 - {key} : {value}")
        self.addRow(operation_type='cmd指令', function_cmd=key, content=value)
        # 创建一个 ImageWidget，并将其设置为表格的单元格内容
        row = self.tableWidget.rowCount() - 1
        image_widget = ImageWidget('res/actionDefaultImages/cmd.png')
        self.tableWidget.setCellWidget(row, 0, image_widget)
        self.tableWidget.setRowHeight(row, 56)

    #  主题切换
    def changeTheme(self, theme):
        """
        主题切换方法
        :param theme: 主题
        """
        global THEME
        if theme == 'default':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/default.qss'))
            THEME = 'default'
            print("默认主题")
        elif theme == 'dark':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/dark.qss'))
            THEME = 'dark'
            print("黑色主题")
        elif theme == 'light':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/light.qss'))
            THEME = 'light'
            print("浅色主题")
        elif theme == 'protectEyes':
            self.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
            # self.setStyleSheet(QSSLoader.read_qss_file('template/QSS/protectEyes.qss'))
            THEME = 'protectEyes'
            print("护眼主题")
        else:
            print("主题错误")

    # 窗口最小化
    def window_min(self):
        """
        窗口最小化
        """
        if self.isMinimized():
            self.showNormal()
        else:
            self.showMinimized()

    # 窗口最大化
    def window_max(self):
        """
        窗口最大化
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # 窗口恢复正常化
    def window_normal(self):
        """
        窗口恢复正常化
        """
        self.showNormal()


# @定义cmd指令编辑器窗口类
class EditorWindow(QtWidgets.QMainWindow, Ui_CmdEditWindow):
    """
    cmd指令编辑窗口类
    """

    def __init__(self, parent=None):
        super(EditorWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置窗口标题和大小
        self.setWindowTitle('cmd指令编辑器')
        self.resize(600, 400)
        # 设置窗口图标
        self.setWindowIcon(QIcon("res/icons/logo.png"))
        # 设置表格的列数和行数
        self.CmdEditTable.setColumnCount(3)
        self.CmdEditTable.setRowCount(0)
        # 设置表格的表头
        self.CmdEditTable.setHorizontalHeaderLabels(['cmd指令名', 'cmd指令内容', '描述'])
        # 设置表格的表头自适应宽度
        # self.CmdEditTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.CmdEditTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格的选择模式为单行选择
        self.CmdEditTable.setSelectionMode(QTableWidget.SingleSelection)
        # 设置表格的选择行为为整行选择
        self.CmdEditTable.setSelectionBehavior(QTableWidget.SelectRows)
        # 设置表格的编辑模式为双击编辑
        self.CmdEditTable.setEditTriggers(QTableWidget.DoubleClicked)

        # 将按钮连接到槽函数
        self.addButton.clicked.connect(self.addRow)
        self.deleteButton.clicked.connect(self.deleteRow)
        self.saveButton.clicked.connect(self.saveFile)

        # 加载配置文件
        self.loadFile()

        # 设置主题
        self.changeCmdWindowTheme(THEME)

    def changeCmdWindowTheme(self, theme):
        """
        主题切换方法
        :param theme: 主题
        """
        if theme == 'default':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/default.qss'))
            print("CMD默认主题")
        elif theme == 'dark':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/dark.qss'))
            print("CMD黑色主题")
        elif theme == 'light':
            self.setStyleSheet(QL.QSSLoader.read_qss_file('template/QSS/light.qss'))
            print("CMD浅色主题")
        elif theme == 'protectEyes':
            self.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
            # self.setStyleSheet(QSSLoader.read_qss_file('template/QSS/protectEyes.qss'))
            print("CMD护眼主题")
        else:
            print("CMD主题错误")

    def loadFile(self):
        """
        加载 xml 配置文件
        """
        # 打开配置文件
        file = open('src/config/CmdConfig.xml', 'r', encoding='utf-8')
        # 读取配置文件内容
        content = file.read()
        # 关闭配置文件
        file.close()
        # 解析xml文件
        root = ET.fromstring(content)
        # 遍历xml文件中的每个Item元素
        for item in root.findall('Item'):
            # 获取Item元素的属性
            key = item.get('Key')
            value = item.get('Value')
            desc = item.get('Desc')
            # 在表格中添加一行
            self.addRow()
            # 获取表格的最后一行
            row = self.CmdEditTable.rowCount() - 1
            # 在表格的最后一行设置单元格的内容
            self.CmdEditTable.setItem(row, 0, QTableWidgetItem(key))
            self.CmdEditTable.setItem(row, 1, QTableWidgetItem(value))
            self.CmdEditTable.setItem(row, 2, QTableWidgetItem(desc))

    def addRow(self):
        """
        在表格中添加一行
        """
        self.CmdEditTable.insertRow(self.CmdEditTable.rowCount())

    def deleteRow(self):
        """
        在表格中删除一行
        """
        # 获取表格的当前行
        row = self.CmdEditTable.currentRow()
        # 如果当前行有效
        if row >= 0:
            # 在表格中删除当前行
            self.CmdEditTable.removeRow(row)

    def saveFile(self):
        """
        保存表格数据到 xml 文件
        """
        # 创建一个xml根元素
        root = ET.Element('CMD')
        # 设置根元素的属性
        root.set('MenuItemName', 'm_menuItem_CMD_')
        # 遍历表格中的每一行
        for row in range(self.CmdEditTable.rowCount()):
            # 检查单元格是否为空
            if all(self.CmdEditTable.item(row, col) is not None
                   for col in range(self.CmdEditTable.columnCount())):
                # 获取表格中的每一行的单元格内容
                key = self.CmdEditTable.item(row, 0).text()
                value = self.CmdEditTable.item(row, 1).text()
                desc = self.CmdEditTable.item(row, 2).text()
                # 创建一个Item子元素
                item = ET.SubElement(root, 'Item')
                # 设置Item子元素的属性
                item.set('Order', str(row + 1))
                item.set('Key', key)
                item.set('Value', value)
                item.set('Desc', desc)
            else:
                QMessageBox.warning(self, "警告",
                                    WANR_STYLE[0] + f"\t第 {row + 1} 行的指令不合法！\t" + WANR_STYLE[1],
                                    QMessageBox.Ok)
                return
        # 创建一个xml树对象
        tree = ET.ElementTree(root)
        # 保存xml文件
        tree.write('src/config/CmdConfig.xml', encoding='utf-8', xml_declaration=True)
        # 弹出一个对话框提示保存成功
        QMessageBox.information(self, "提示",
                                INFO_STYLE[0] + "保存成功" + INFO_STYLE[1],
                                QMessageBox.Ok)


# @关于页面显示类
class AboutDialog(QDialog):
    """
    关于页面显示类
    """

    def __init__(self, html_path):
        super().__init__()
        self.setWindowTitle("关于")
        self.setGeometry(0, 0, 500, 600)

        # 获取屏幕的大小和位置用于居中显示
        screen_geometry = QDesktopWidget().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        # 设置窗口图标
        self.setWindowIcon(QIcon("res/icons/logo.png"))  # 替换成你的图标路径

        layout = QVBoxLayout()
        # 移除内容区域边距
        layout.setContentsMargins(0, 0, 0, 0)

        text_browser = QTextBrowser()
        text_browser.setOpenExternalLinks(True)
        text_browser.setHtml(open(html_path, 'r', encoding='utf-8').read())
        layout.addWidget(text_browser)
        self.setLayout(layout)


# @功能介绍页面显示类
class FeatureDialog(QDialog):
    """
    功能介绍页面显示类
    """

    def __init__(self, html_path):
        super().__init__()
        self.setWindowTitle("功能介绍")
        self.setGeometry(0, 0, 650, 700)

        # 获取屏幕的大小和位置用于居中显示
        screen_geometry = QDesktopWidget().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        layout = QVBoxLayout()

        # 移除内容区域边距
        layout.setContentsMargins(0, 0, 0, 0)

        # 设置窗口图标
        self.setWindowIcon(QIcon("res/icons/logo.png"))  # 替换成你的图标路径

        text_browser = QTextBrowser()
        text_browser.setOpenExternalLinks(True)
        text_browser.setHtml(open(html_path, 'r', encoding='utf-8').read())
        layout.addWidget(text_browser)
        self.setLayout(layout)


# @主执行线程类
class WorkThread(QThread):
    """
    主执行线程类
    """
    # 自定义信号对象。参数list就代表这个信号可以传一个列表
    trigger = pyqtSignal(list)

    def __init__(self, tableWidget, action, logBrowser):
        # 初始化函数
        super(WorkThread, self).__init__()
        # 接收 QTableWidget 对象作为参数，并将其保存在线程对象中
        self.tableWidget = tableWidget
        # 接收 action 参数，并将其保存在线程对象中
        self.action = action
        # 接收 QTextBrowser 对象作为参数，并将其保存在线程对象中
        self.logBrowser = logBrowser
        # 创建一个定时器对象
        self.timer = QtCore.QTimer()
        # 设置定时器的间隔为 1000 毫秒
        self.timer.setInterval(1000)
        # 连接定时器的 timeout 信号和槽函数
        self.timer.timeout.connect(self.updateCountdown)
        # 设置倒计时的初始值
        self.countdown = None
        # 设置原来的日志信息
        self.original_log = None

    def run(self):
        """
        重写线程执行的run函数，# 根据 action 参数的值，执行不同的内容
        """
        if self.action == 'run_all':
            print("\n=============  🚀运行一次🚀  =============")
            self.trigger.emit(['#F5FA52', ""])
            self.trigger.emit(['#F5FA52', "=============  🚀运行一次🚀  =============\n"])
            self.trigger.emit(['#F5FA52', "开始时间:[{}]".format(datetime.datetime.now())])
            mainWork(self, self.tableWidget, self.action)
            self.trigger.emit(['#F5FA52', ''])  # 换行
            self.trigger.emit(['#F5FA52', "完成时间:[{}]".format(datetime.datetime.now())])
            self.trigger.emit(['#F5FA52', "=============  🎉任务完成🎉  ============="])
            self.trigger.emit(['#F5FA52', ''])  # 换行
            print("=============  🎉任务完成🎉  =============\n")
        elif self.action == 'run_one':
            print("\n=============  👉🏻指定运行👈🏻  =============")
            self.trigger.emit(['#7CFAFF', "=============  👉🏻指定运行👈🏻  ============="])
            self.trigger.emit(['#7CFAFF', "开始时间:[{}]".format(datetime.datetime.now())])
            mainWork(self, self.tableWidget, self.action)
            self.trigger.emit(['#7CFAFF', ''])  # 换行
            self.trigger.emit(['#7CFAFF', "完成时间:[{}]".format(datetime.datetime.now())])
            self.trigger.emit(['#7CFAFF', "=============  ✨任务完成✨  ============="])
            self.trigger.emit(['#7CFAFF', ''])  # 换行
            print("=============  ✨任务完成✨  =============\n")
        else:
            print("action 的值未知")

    def onTimerFinished(self):
        """
        处理 runClockThread 的 timerFinished 信号的方法
        """
        # 这里是你想要执行的代码，例如打印一句话
        print("Timer finished!")

    def updateCountdown(self):
        """
        更新倒计时的槽函数
        """
        print("updateCountdown 方法调用了")
        # 获取 QTextBrowser 的光标对象
        cursor = self.logBrowser.textCursor()
        # 移动光标到最后一行
        cursor.movePosition(cursor.End)
        cursor.movePosition(cursor.StartOfLine)
        # 删除最后一行的内容
        cursor.removeSelectedText()
        # 插入新的倒计时信息
        cursor.insertText("[INFO] - <倒计时> {} 秒".format(self.countdown))
        # 更新 QTextBrowser 的显示
        self.logBrowser.setTextCursor(cursor)
        # 判断倒计时是否结束
        if self.countdown == 0:
            # 停止定时器
            self.timer.stop()
            # 恢复原来的日志信息
            cursor.removeSelectedText()
            cursor.insertText(self.original_log)
            self.logBrowser.setTextCursor(cursor)
        else:
            # 减少倒计时的值
            self.countdown -= 1

# @加载QSS文件类
# class QSSLoader:
#     """
#     加载QSS文件类
#     """
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def read_qss_file(qss_file_name):
#         """
#
#         :param qss_file_name:
#         :return:
#         """
#         with open(qss_file_name, 'r', encoding='UTF-8') as file:
#             return file.read()
