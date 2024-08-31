"""
1
"""


def iterateTableData(table):
    """
    迭代表格数据方法
    :param table:
    """
    # 获取行数和列数
    rowCount = table.rowCount()
    colCount = table.columnCount()

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
        print(f"第 {row + 1}  行的数据: {rowData}")
        if rowData[1] == "鼠标":
            print("操作类型为：鼠标", end=' ')
            if rowData[2] == "单击左键" and rowData[7] == '1':
                print("功能指令为：单击左键", end=' \n')

            elif rowData[2] == "双击左键" and rowData[7] == '1':
                print("功能指令为：双击左键", end=' \n')

            elif rowData[2] == "单击右键" and rowData[7] == '1':
                print("功能指令为：单击右键", end=' \n')

            elif rowData[2] == "滚轮" and rowData[7] == '1':
                print("功能指令为：滚轮", end=' \n')

            elif rowData[2] == "鼠标定点移动" and rowData[7] == '1':
                print("功能指令为：鼠标定点移动", end=' \n')

            elif rowData[2] == "鼠标相对移动" and rowData[7] == '1':
                print("功能指令为：鼠标相对移动", end=' \n')

        elif rowData[1] == "键盘":
            print("操作类型为：键盘", end=' ')
            if rowData[2] == "按键" and rowData[7] == '1':
                print("功能指令为：按键", end=' \n')

            elif rowData[2] == "热键组合" and rowData[7] == '1':
                print("功能指令为：热键组合", end=' \n')

            elif rowData[2] == "键盘输入TXT内容" and rowData[7] == '1':
                print("功能指令为：键盘输入TXT内容", end=' \n')

        elif rowData[1] == "系统":
            print("操作类型为：系统", end=' ')
            if rowData[2] == "延时" and rowData[7] == '1':
                print("功能指令为：延时", end=' \n')

            elif rowData[2] == "定时" and rowData[7] == '1':
                print("功能指令为：定时", end=' \n')

        elif rowData[1] == "cmd指令":
            print("操作类型为：cmd指令", end=' ')

        elif rowData[1] == "其它":
            print("操作类型为：其它", end=' ')
            if rowData[2] == '输入' and rowData[7] == '1':
                print("功能指令为：输入", end=' \n')

        else:
            print("操作类型错误！！！")
