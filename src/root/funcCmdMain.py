"""
功能指令主执行程序
"""
import src.root.PyRPA.functions_mod as fm


def mainWork(self, table, action):
    """
    主执行方法（按行从上至下顺序依次执行）
    :param self:
    :param table: 指令表
    :param action: 执行方式(run_all/run_one)
    """
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

    print("--------------------  开始执行  --------------------")
    for row in range(len(tableData)):
        self.trigger.emit(['#FFFFFF', '\n'])
        rowData = tableData[row]
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

# if __name__ == '__main__':
#     # 文件名
#
#     filename = pyautogui.prompt(text='请输入[任务表格]的绝对路径', title='CocoPyRPA--表格路径',
#                                 default='绝对路径')
#
#     if filename is None:
#         my_logg.info('<<**********************$ 任务被取消 $**********************>>\n')
#         sys.exit(0)  # 程序终止
#
#     try:
#         w = xlrd.open_workbook(filename)
#     except OSError as e:
#         my_logg.error('输入的路径错误或不存在\n' + str(traceback.format_exc()) + '\n')
#         pyautogui.alert(text='\n\n表格路径错误！', title='CocoPyRPA--警告', button='退出')
#     # 打开文件
#     wb = xlrd.open_workbook(filename)
#     # 通过索引获取表格sheet页
#     sheet1 = wb.sheet_by_index(0)
#
#     # 数据检查
#     checkCmd = cm.data_check(sheet1)
#     if checkCmd:
#         my_logg.info('数据检查成功')
#         pyautogui.alert(text='\n\n数据检查成功', title='CocoPyRPA--提示', button='继续')
#         key = pyautogui.confirm(text='\n\n请选择功能:\n输入1只做一次,输入2循环n次', title='CocoPyRPA--功能选择',
#                                 buttons=['1', '2'])
#         if key == '1':
#             # 循环拿出每一行指令
#             mainWork(sheet1)
#             my_logg.info('<<======================$ 任务执行成功 $======================>>\n')
#             # 弹窗提示
#             pyautogui.alert('🎉恭喜任务执行完毕🎉\n单击确定退出!')
#         elif key == '2':
#             n = pyautogui.prompt(text='请输入循环次数', title='CocoPyRPA--循环次数', default='10')
#             n = int(n)
#             while n > 0:
#                 mainWork(sheet1)
#                 if n != 1:
#                     my_logg.info("等待0.1秒后再次执行")
#                 fm.time.sleep(0.1)
#                 n -= 1
#             my_logg.info('<<======================$ 任务执行成功 $======================>>\n')
#             # 弹窗提示
#             pyautogui.alert(text='🎉恭喜任务执行完毕🎉', title='CocoPyRPA--提示', button='退出')
#     else:
#         # 弹窗警告❌
#         pyautogui.alert(text='\n\n❌数据检查失败❌', title='CocoPyRPA--退出', button='退出')
