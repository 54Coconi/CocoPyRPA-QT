"""
功能模块,包含各个功能函数
目前包括的功能(指令)，指令实现功能详见说明文档

【about mouse 鼠标类】
1.<单击左键>
2.<双击左键>
3.<单击右键>
4.<滚轮>
5.<鼠标定点移动>
6.<鼠标相对移动>

【about keyboard 按键类】
1.<按键>
2.<热键组合>
3.<键盘输入TXT内容>

【about control 控制类】
1.<等待>
2.<cmd指令>

【other 其他类】
1.<输入>
"""
import os
import re
import subprocess
import time

import pyautogui
import pyperclip
from PyQt5.QtCore import QThread, pyqtSignal
from numpy.core.defchararray import lower
from pyautogui import ImageNotFoundException as pyautogui_ImageNotFoundException
from pyscreeze import ImageNotFoundException as pyscreeze_ImageNotFoundException

from src.utils.Clock import MyTimer


# funLogStr = ''


def mouseClick(self, errorLoop, lOrR, clickTime, content, img, loop):
    """
    定义鼠标点击事件
    :param self:
    :param errorLoop: 容错次数
    :param lOrR: 左键 或 右键
    :param clickTime: 点击次数
    :param content: 实例对象（坐标/图片）
    :param img: 图片路径
    :param loop: 重复次数
    """
    print("图片路径为[{}]".format(img))
    self.trigger.emit(['#FFFFFF', "🖼图片路径为[{}]".format(img)])
    i = 1
    while i <= int(loop):
        if img == '无':
            if lOrR == 'left' and clickTime == 1:
                pyautogui.leftClick()
                print("[INFO] - <单击左键> 执行第 {} 次".format(i))
                self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击左键&gt; 执行第 {} 次".format(i)])
            elif lOrR == 'right' and clickTime == 1:
                pyautogui.rightClick()
                print("[INFO] - <单击右键> 执行第 {} 次".format(i))
                self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击右键&gt; 执行第 {} 次".format(i)])
            elif lOrR == 'left' and clickTime == 2:
                pyautogui.doubleClick()
                print("[INFO] - <双击左键> 执行第 {} 次".format(i))
                self.trigger.emit(['#AAE84D', "[INFO] - &lt;双击左键&gt; 执行第 {} 次".format(i)])
            i += 1
        else:
            # pyautogui.useImageNotFoundException()
            try:
                pyautogui.locateCenterOnScreen(img, confidence=0.9)
                print("pyautogui.locateCenterOnScreen(img, confidence=0.9)的值为：",
                      pyautogui.locateCenterOnScreen(img, confidence=0.9))
            except (pyscreeze_ImageNotFoundException, pyautogui_ImageNotFoundException) as e:
                print(f"[ERROR] - 图片路径错误或不存在！\n{str(e)}")
                self.trigger.emit(['#FF5370', f"[ERROR] - 图片路径错误或不存在！\n{str(e)}"])

            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            print("\nlocation = ", location)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTime, interval=0.2, duration=0.2, button=lOrR)
                if lOrR == 'left' and clickTime == 1:
                    print("[INFO] - <单击左键> 执行第 {} 次".format(i))
                    self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击左键&gt; 执行第 {} 次".format(i)])
                elif lOrR == 'right' and clickTime == 1:
                    print("[INFO] - <单击右键> 执行第 {} 次".format(i))
                    self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击右键&gt; 执行第 {} 次".format(i)])
                elif lOrR == 'left' and clickTime == 2:
                    print("[INFO] - <双击左键> 执行第 {} 次".format(i))
                    self.trigger.emit(['#AAE84D', "[INFO] - &lt;双击左键&gt; 执行第 {} 次".format(i)])
                i += 1
            else:
                j = 1
                while j <= int(errorLoop):
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is not None:
                        # time.sleep(0.5)
                        print(" -- 已找到图像坐标位置为：x = {}, y = {}".format(loc.x, loc.y))
                        self.trigger.emit(['#FFFFFF', " -- 已找到图像坐标位置为：x = {}, y = {}".format(loc.x, loc.y)])
                        pyautogui.click(loc.x, loc.y, clicks=clickTime, interval=0.2, duration=0.2, button=lOrR)
                        if lOrR == 'left' and clickTime == 1:
                            print("[INFO] - <单击左键> 执行第 {} 次".format(i))
                            self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击左键&gt; 执行第 {} 次".format(i)])
                        elif lOrR == 'right' and clickTime == 1:
                            print("[INFO] - <单击右键> 执行第 {} 次".format(i))
                            self.trigger.emit(['#AAE84D', "[INFO] - &lt;单击右键&gt; 执行第 {} 次".format(i)])
                        elif lOrR == 'left' and clickTime == 2:
                            print("[INFO] - <双击左键> 执行第 {} 次".format(i))
                            self.trigger.emit(['#AAE84D', "[INFO] - &lt;双击左键&gt; 执行第 {} 次".format(i)])
                        break

                    if lOrR == 'left' and clickTime == 1:
                        print(f"[ERROR] - <单击左键> 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试")
                        self.trigger.emit(['#FF5370',
                                           f"[ERROR] - &lt;单击左键&gt; 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试"])
                    elif lOrR == 'right' and clickTime == 1:
                        print(f"[ERROR] - <单击右键> 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试")
                        self.trigger.emit(['#FF5370',
                                           f"[ERROR] - &lt;单击右键&gt; 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试"])
                    elif lOrR == 'left' and clickTime == 2:
                        print(f"[ERROR] - <双击左键> 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试")
                        self.trigger.emit(['#FF5370',
                                           f"[ERROR] - &lt;双击左键&gt; 执行第 {i} 次未找到匹配图片, 第 {j} 次尝试寻找, 0.1秒后重试"])
                    time.sleep(0.1)
                    j += 1
                i += 1


# @鼠标类
class RPA_mouse:
    """
    鼠标指令类
    """

    # 1.<单击左键> 和 2.<双击左键>
    @staticmethod
    def clickL(self, rowData):
        """
        鼠标左键指令功能方法
        :param self:
        :param rowData: 表格每行数据，list 类型
        """
        # 取实例对象
        content = rowData[3]
        # 取图片名称(路径)
        imgName = rowData[6]
        # 设置默认循环次数为1
        loop = 1
        # 循环次数不为 0（若不满足则按默认的执行 1 次）
        if rowData[4] != '0':
            # 取循环次数
            loop = rowData[4]
        # 取容错次数
        errorLoop = rowData[5]
        if rowData[2] == '单击左键':
            # 调用鼠标执行点击操作的方法
            mouseClick(self, errorLoop, 'left', clickTime=1, content=content, img=imgName, loop=loop)
        if rowData[2] == '双击左键':
            # 调用鼠标执行点击操作的方法
            mouseClick(self, errorLoop, 'left', clickTime=2, content=content, img=imgName, loop=loop)

    # 3.<单击右键>
    @staticmethod
    def clickR(self, rowData):
        """
        鼠标右键指令功能方法
        :param self:
        :param rowData: 表格每行数据，list 类型
        """
        # 取实例对象
        content = rowData[3]
        # 取图片名称
        imgName = rowData[6]
        # 设置默认执行次数为1
        loop = 1
        # 重复次数必须为数字类型且重复次数不为0（若不满足则按默认的执行1次）
        if rowData[4] != '0':
            # 取循环次数
            loop = rowData[4]
        # 取容错次数
        errorLoop = rowData[5]
        mouseClick(self, errorLoop, 'right', 1, content, imgName, loop)

    # 4.<滚轮>
    @staticmethod
    def myScroll(self, rowData):
        """
        鼠标滚轮滚动指令方法
        :param self:
        :param rowData: 表格每行数据，list 类型
        """
        # 取要移动的距离值
        scroll = rowData[3]
        print("滚动值：", scroll)
        if scroll:
            pyautogui.scroll(int(scroll))
            if int(scroll) < 0:
                print(f"[INFO] - <滚轮> 向下滑动了 {abs(int(scroll))} 距离")
                self.trigger.emit(['#AAE84D', f"[INFO] - &lt;滚轮&gt; 向下滑动了 {abs(int(scroll))} 距离"])
            elif int(scroll) > 0:
                print(f"[INFO] - <滚轮> 向上滑动了 {abs(int(scroll))} 距离")
                self.trigger.emit(['#AAE84D', f"[INFO] - &lt;滚轮&gt; 向上滑动了 {abs(int(scroll))} 距离"])
            else:
                print(f"[INFO] - <滚轮> 滑动了 {abs(int(scroll))} 距离")
                self.trigger.emit(['#AAE84D', f"[INFO] - &lt;滚轮&gt; 滑动了 {abs(int(scroll))} 距离"])
        else:
            # 可以给一个默认的滚动值，或者采取其他措施
            pyautogui.scroll(0)
            print(f"[INFO] - <滚轮> 滑动了 0 距离")
            self.trigger.emit(['#AAE84D', f"[INFO] - &lt;滚轮&gt; 滑动了 0 距离"])

    # 5.<鼠标定点移动>
    @staticmethod
    def clickMoveTo(self, rowData):
        """
        鼠标移动到指定的绝对坐标
        :param self:
        :param rowData:
        """
        xy_list = rowData[3].split(',')
        x = int(float(xy_list[0].split('(')[1]))
        y = int(float(xy_list[1].split(')')[0]))
        pyautogui.moveTo(x, y, 0.3)  # 移动延时为 0.3s
        print(f"[INFO] - <鼠标定点移动> x = {x}, y = {y}")
        self.trigger.emit(['#AAE84D', f"[INFO] - &lt;鼠标定点移动&gt; x = {x}, y = {y}"])

    # 6.<鼠标相对移动>
    @staticmethod
    def clickRelMove(self, rowData):
        """
        鼠标相对当前坐标移动
        :param self:
        :param rowData:
        """
        xy_list = rowData[3].split(',')
        x = int(float(xy_list[0].split('(')[1]))
        y = int(float(xy_list[1].split(')')[0]))
        pyautogui.move(x, y, 0.4)  # 移动延时为 0.4s
        if x > 0:
            xMove = '[INFO] - &lt;鼠标相对移动&gt; ' + 'x右移' + str(abs(x)) + ', '
        elif x < 0:
            xMove = '[INFO] - &lt;鼠标相对移动&gt; ' + 'x左移' + str(abs(x)) + ', '
        else:
            xMove = '[INFO] - &lt;鼠标相对移动&gt; ' + 'x移动' + str(abs(x)) + ', '

        if y > 0:
            yMove = 'y下移' + str(abs(y))
        elif y < 0:
            yMove = 'y上移' + str(abs(y))
        else:
            yMove = 'y移动' + str(abs(y))
        print(xMove + yMove)
        self.trigger.emit(['#AAE84D', f"{xMove + yMove}"])


# @键盘类
class RPA_keyboard:
    """
    按键指令类
    """
    # 要传递给press() 、keyDown() 、keyUp() 和 hotkey()函数的有效字符串：
    KEYBOARD_KEYS = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                     'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                     'command', 'option', 'optionleft', 'optionright']

    # 7.<按键>
    @staticmethod
    def keystroke(self, rowData):
        """
        模拟按下一个键然后松开它
        """
        key = str(rowData[3])
        if lower(key) not in RPA_keyboard.KEYBOARD_KEYS:
            print(f"[ERROR] - 按键 \"{key}\" 无效")
            self.trigger.emit(['#FF5370', f"[ERROR] - 按键 \"{key}\" 无效"])
        else:
            # 设置默认循环次数为1
            loop = 1
            # 循环次数不为 0（若不满足则按默认的执行 1 次）
            if int(rowData[4]) > 0:
                # 取循环次数
                loop = int(rowData[4])
            i = 1
            while i <= loop:
                pyautogui.press(key)
                print(f"[INFO] - &lt;按键&gt; 按下 \"{key}\" 第 {i} 次")
                self.trigger.emit(['#AAE84D', f"[INFO] - &lt;按键&gt; 按下 \"{key}\" 第 {i} 次"])
                i += 1

    # 8.<热键组合>
    @staticmethod
    def hotkeyCombi(self, rowData):
        """
        获取表格单元格的内容（形如 'key1+key2+key3+...'）并将其分割得到一个列表
        key_list['key1','key2',...] 并将整个 list 传入 hotkey() 函数中。
        对按顺序传递的参数执行按键按下，然后按相反顺序执行按键释放。
        其效果是调用热键（“ctrl”，“shift”，“c”）将执行 “Ctrl-Shift-C” 热键键盘快捷键。
        """
        # 编译一个正则表达式对象
        pattern1 = re.compile(r"^(\w+\+)+\w+$")
        pattern2 = re.compile(r"^(\w+\+)+(\w|[+\-*/])+$")
        inputVal = rowData[3]
        # 检查字符串是否匹配模式
        if re.match(pattern1, inputVal) or re.match(pattern2, inputVal):
            # 如果匹配，将其分割得到一个列表
            key_list = inputVal.split('+')
            # 设置默认循环次数为1
            loop = 1
            # 循环次数大于 0（若不满足则按默认的执行 1 次）
            if int(rowData[4]) > 0:
                # 取循环次数
                loop = int(rowData[4])
            i = 1
            while i <= loop:
                # 调用 hotkey() 函数
                pyautogui.hotkey(key_list)
                print(f"[INFO] - <热键组合> \"{inputVal}\" 执行第 {i} 次")
                self.trigger.emit(['#AAE84D', f"[INFO] - &lt;热键组合&gt; \"{inputVal}\" 执行第 {i} 次"])
                i += 1
        else:
            # 如果不匹配，打印一个错误信息
            print(f"[ERROR] - 无效的热键格式 \"{inputVal}\" ")
            self.trigger.emit(['#FF5370', f"[ERROR] - 无效的热键格式 \"{inputVal}\" "])

    # 9.<键盘输入TXT内容>
    @staticmethod
    def EnterTxtOnKeyboard(self, rowData):
        """
        键盘输入TXT内容(由于是模拟键盘的按键按下和释放，所以不支持中文)
        从表格单元格获取 txt 文件路径，找到文件并打开得到内容，然后对内容中的每个字符执行键盘按键按下，然后释放
        """
        inputVal = rowData[3]
        filepath = inputVal
        # 检查路径是否是一个文件
        if os.path.isfile(filepath):
            # 检查文件扩展名是否是 .txt
            if filepath.endswith(".txt"):
                # 如果是，打开文件并读取内容
                with open(filepath, 'r', encoding='UTF-8') as file:  # ‘r’只读文件
                    message = file.read()

                # 设置默认循环次数为1
                loop = 1
                # 循环次数不为 0（若不满足则按默认的执行 1 次）
                if int(rowData[4]) > 0:
                    # 取循环次数
                    loop = int(rowData[4])
                i = 1
                while i <= loop:
                    pyautogui.typewrite(message, interval=0.025)  # interval 指输入间隔(秒)
                    print(f"[INFO] - <键盘输入TXT内容> \"{message}\" 第 {i} 次")
                    self.trigger.emit(['#AAE84D', f"[INFO] - &lt;键盘输入TXT内容&gt; \"{message}\" 第 {i} 次"])
                    i += 1

            else:
                # 如果不是，打印一个错误信息
                print(f"[ERROR] - [{filepath}] 文件扩展名不是 \".txt\" ")
                self.trigger.emit(['#FF5370', f"[ERROR] - [{filepath}] 文件扩展名不是 \".txt\" "])
        else:
            if not os.path.exists(filepath):
                print(f"[ERROR] - [{filepath}] 路径不存在 ")
                self.trigger.emit(['#FF5370', f"[ERROR] - [{filepath}] 路径不存在 "])
            else:
                # 如果不是一个文件，打印一个错误信息
                print(f"[ERROR] - [{filepath}] 路径不是一个文件 ")
                self.trigger.emit(['#FF5370', f"[ERROR] - [{filepath}] 路径不是一个文件 "])


# @系统类
class RPA_control:
    """
    系统控制类
    """
    ON_TIME = ''

    # 10.<延时>
    @staticmethod
    def waitTime(self, rowData):
        """
        获取延时时长
        :param self:
        :param rowData:
        """
        wait_time = float(rowData[3])
        print("[INFO] - <延时> {} 秒".format(wait_time))
        self.trigger.emit(['#AAE84D', f"[INFO] - <延时> {wait_time} 秒后执行下一步操作"])
        time.sleep(wait_time)

        # # 启动定时器
        # self.timer.start()
        # # 设置倒计时的初始值
        # self.countdown = wait_time
        # # 设置原来的日志信息
        # self.original_log = "[INFO] - <延时> {} 秒".format(wait_time)

    # 11.<定时>
    @staticmethod
    def onTime(self, rowData):
        """
        获取定时时间
        :param self:
        :param rowData:
        """
        on_time = str(rowData[3])
        RPA_control.ON_TIME = on_time
        print(f"[INFO] - <定时> {on_time} 秒后执行下一步操作")
        self.trigger.emit(['#AAE84D', f"[INFO] - <定时> 到 {on_time} 时刻后执行下一步操作"])

        # # 创建一个新的线程对象，继承自 QThread 类
        # self.runClockThread = RunClockThread(on_time)
        # # 连接新的线程的信号和槽
        # self.runClockThread.timerFinished.connect(self.onTimerFinished)
        # # 启动新的线程
        # self.runClockThread.start()


# 定义一个新的线程类，继承自 QThread 类
class RunClockThread(QThread):
    """
    执行时钟线程类
    """
    # 定义一个自定义的信号，用于传递时钟类的定时完成事件
    timerFinished = pyqtSignal()

    # 重写构造方法，可以传入自定义的参数
    def __init__(self, targetTime):
        super().__init__()
        self.myTimer = None
        self.targetTime = targetTime

    # 重写 run () 方法，将你想要执行的代码放在这里
    def run(self):
        # 创建一个时钟类的对象，传入目标时间
        self.myTimer = MyTimer(self.targetTime)
        # 连接时钟类的信号和槽
        self.myTimer.timerFinished.connect(self.onTimerFinished)
        # 显示时钟类的窗口
        self.myTimer.show()

    # 定义槽
    def onTimerFinished(self):
        """
        定时完成事件，关闭 LCD 时钟，并发出自定义的信号
        """
        # 关闭时钟类的窗口
        self.myTimer.close()
        # 退出线程
        self.quit()
        # 发出自定义的信号
        self.timerFinished.emit()


# def runClock(targetTime):
#     """
#     运行时钟类的方法
#     """
#     # 创建一个应用程序对象
#     app = QApplication(sys.argv)
#     # 创建一个线程类的对象，传入目标时间
#     t = MyThread(targetTime)
#     # 启动线程
#     t.start()
#     # 等待线程结束
#     t.wait()
#     # 进入应用程序的主循环
#     sys.exit(app.exec_())


# 定义一个线程类，继承自 QThread 类
# class MyThread(QThread):
#     """
#     自定义线程类（用于显示时钟）
#     """
#     # 重写构造方法，可以传入自定义的参数
#     def __init__(self, targetTime):
#         super().__init__()
#         self.myTimer = None
#         self.targetTime = targetTime
# 
#     # 重写 run () 方法，将你想要执行的代码放在这里
#     def run(self):
#         """
#         执行方法
#         """
#         # 创建一个时钟类的对象，传入目标时间
#         self.myTimer = MyTimer(self.targetTime)
#         # 连接时钟类的信号和槽
#         self.myTimer.timerFinished.connect(self.onTimerFinished)
#         # 显示时钟类的窗口
#         self.myTimer.show()
# 
#     # 定义槽
#     def onTimerFinished(self):
#         """
#         定时完成事件，关闭 LCD 时钟
#         """
#         # 关闭时钟类的窗口
#         self.myTimer.close()
#         # 退出线程
#         self.quit()

# @cmd指令类
class RPA_cmd:
    """
    cmd指令类
    """

    @staticmethod
    def executeCmd(self, rowData):
        """
        执行 cmd 指令的方法
        :param self:
        :param rowData:
        """
        key = rowData[2]
        value = rowData[3]
        # 使用 subprocess.Popen 方法执行 cmd 命令，返回一个进程对象
        process = subprocess.Popen(value, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"[INFO] - [cmd指令] <{key}> : {value} 开始执行")
        self.trigger.emit(['#AAE84D', f"[INFO] - [cmd指令] &lt;{key}&gt; : {value} 开始执行"])

        # 使用 wait() 方法等待子进程结束，并捕获错误
        return_code = process.wait()
        print(return_code)
        if return_code != 0:
            # 命令执行出错
            error = process.stderr.read()
            if error:
                print(error.strip())
                self.trigger.emit(['#FF5370', f"[ERROR] - [cmd指令] \"{key}\" 执行错误：{error.strip()}"])
            else:
                # 命令执行成功
                self.trigger.emit(['#AAE84D', f"[INFO] - [cmd指令] \"{key}\" 执行成功"])
        else:
            # 命令执行成功
            self.trigger.emit(['#AAE84D', f"[INFO] - [cmd指令] \"{key}\" 执行成功"])


# @其它类
class RPA_other:
    """
    其它类
    """

    # 11.<输入>
    @staticmethod
    def pasteboardInput(self, rowData):
        """
        复制表格单元格里的内容到粘贴板，并粘贴输入内容
        """
        # 取单元格中要输入的内容
        inputVal = str(rowData[3])
        # 复制单元格内容到粘贴板
        pyperclip.copy(inputVal)
        # 粘贴内容
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        print(f"[INFO] - <输入> 内容：\"{inputVal}\" ")
        self.trigger.emit(['#AAE84D', f"[INFO] - <输入> 内容：\"{inputVal}\" "])
