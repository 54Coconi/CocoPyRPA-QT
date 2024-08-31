"""
功能指令主执行程序
"""
import re

import src.root.PyRPA.functions_mod as fm

goalRow_ = '0'


def mainWork(self, table, action):
    """
    主执行方法（按行从上至下顺序依次执行）
    :param self:
    :param table: 指令表
    :param action: 执行方式(run_all/run_one)
    """
    global goalRow_
    rowData = []
    tableData = []
    # 执行所有指令一次
    if action == "run_all":
        rowCount = table.rowCount()
        colCount = table.columnCount()
        print("\n表格行数：", rowCount)
        print("表格列数：", colCount)
        # 遍历每一行
        for row in range(rowCount):
            rowData = []
            # 遍历每一列
            for col in range(colCount):
                item = table.item(row, col)
                if item is not None:
                    rowData.append(item.text())
                else:
                    rowData.append(None)
            tableData.append(rowData)
        print("表格内容：")
        for row in range(len(tableData)):
            print(tableData[row])

    elif action == "run_one":
        selected_items = table.selectedItems()
        colCount = table.columnCount()
        if selected_items:
            # 获取用户选择的第一行的行号
            selected_row = selected_items[0].row()
            print("选中的一行为：", selected_row + 1)
            # 遍历每一列
            for col in range(colCount):
                if table.item(selected_row, col) is not None:
                    rowData.append(table.item(selected_row, col).text())
                else:
                    rowData.append(None)
            tableData.append(rowData)
            print("选中的一条指令为", tableData[0])

    else:
        print("action 未知")

    # print("--------------------  开始执行  --------------------")
    for row in range(len(tableData)):
        self.trigger.emit(['#FFFFFF', '\n'])
        rowData = tableData[row]

        if rowData[8] == "目标行,重复次数":
            print("默认值：", rowData[8])
        elif re.match(re.compile(r'[0-9]+,[0-9]+'), rowData[8]):
            print("自定义值：", rowData[8])
            goalRow = rowData[8].split(',')[0]
            goalRow_ = goalRow
            print("goalRow_ = ", goalRow_)
            repeat = rowData[8].split(',')[1]
            print(f"从当前第 {row + 1} 行到目标第 {goalRow} 行，局部指令块重复执行 {repeat} 次")
            self.trigger.emit(['#FFFFFF', f"从当前第 {row + 1} 行到目标第 {goalRow} 行，局部指令块重复执行 {repeat} 次"])
            if row + 1 < int(goalRow) <= len(tableData):  # 目标行在当前行之后且不超过表格总行数
                print("目标行【符合】范围")
                self.trigger.emit(['#FFFFFF', f"目标行: {row + 1} 符合范围"])
                for i in range(int(repeat)):  # 重复次数
                    for j in range(row, int(goalRow)):  # 需要重复执行的指令块（从当前行到目标行）
                        rowData = tableData[j]
                        matchCmd(self, j, rowData)
                    print("-------------------------------------------------------")
                    self.trigger.emit(['#C3E88D', f"-------------------------------------------------------"])
                # print("目标行执行完毕")
            else:
                print("目标行【超出】范围")
                self.trigger.emit(['#FFFFFF', f"目标行超出合法范围！请检查第 {row + 1} 行"])
        else:
            print("【多行重复】的值未知：", rowData[8])

        if int(goalRow_) <= row <= len(tableData) - 1:
            # print("######### row = ", row)
            # print("######### rowData = ", rowData)
            matchCmd(self, row, rowData)
            # if row == len(tableData) - 1:
            #     goalRow_ = '0'  # 一定要归零
            #     print("执行完毕")
    goalRow_ = '0'  # 一定要归零


def matchCmd(self, row, rowData):
    """

    :param self:
    :param row:
    :param rowData:
    """
    # 指令<单击左键>
    if rowData[2] == "单击左键":
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<单击左键>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;单击左键&gt;"])
            fm.RPA_mouse.clickL(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<双击左键>
    if rowData[2] == '双击左键':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<双击左键>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;双击左键&gt;"])
            fm.RPA_mouse.clickL(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<单击右键>
    if rowData[2] == '单击右键':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<单击右键>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;单击右键&gt;"])
            fm.RPA_mouse.clickR(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<滚轮>
    if rowData[2] == '滚轮':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<滚轮>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;滚轮&gt;"])
            fm.RPA_mouse.myScroll(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<鼠标相对移动>
    if rowData[2] == '鼠标相对移动':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<鼠标相对移动>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;鼠标相对移动&gt;"])
            fm.RPA_mouse.clickRelMove(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<鼠标定点移动>
    if rowData[2] == '鼠标定点移动':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<鼠标定点移动>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;鼠标定点移动&gt;"])
            fm.RPA_mouse.clickMoveTo(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<按键>
    if rowData[2] == '按键':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<按键>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;按键&gt;"])
            fm.RPA_keyboard.keystroke(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<热键组合>
    if rowData[2] == '热键组合':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<热键组合>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;热键组合&gt;"])
            fm.RPA_keyboard.hotkeyCombi(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<键盘输入TXT内容>
    if rowData[2] == '键盘输入TXT内容':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<键盘输入TXT内容>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;键盘输入TXT内容&gt;"])
            fm.RPA_keyboard.EnterTxtOnKeyboard(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<延时>
    if rowData[2] == '延时':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<延时>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;延时&gt;"])
            fm.RPA_control.waitTime(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<定时>
    if rowData[2] == '定时':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<定时>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;定时&gt;"])
            fm.RPA_control.onTime(self, rowData)

        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令 [cmd指令]
    if rowData[1] == 'cmd指令':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<cmd指令>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;cmd指令&gt;"])
            fm.RPA_cmd.executeCmd(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])

    # 指令<输入>
    if rowData[2] == '输入':
        if rowData[7] == '1':
            print(f"\nStep {row + 1}：" + "<输入>")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：&lt;输入&gt;"])
            fm.RPA_other.pasteboardInput(self, rowData)
        else:
            print(f"\nStep {row + 1}：" + "未启用")
            self.trigger.emit(['#FFFFFF', f"&#11162; Step {row + 1}：未启用"])
