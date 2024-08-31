"""
定时时钟
"""
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyTimer(QWidget):
    """
    定时时钟类
    """
    timerFinished = pyqtSignal()

    def __init__(self, targetTime, parent=None):
        super(MyTimer, self).__init__(parent)
        self.targetTime = targetTime
        self.resize(350, 100)
        self.setWindowTitle("定时时钟")

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(time.strftime("%X", time.localtime()))

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        self.setLayout(layout)

        # 新建一个QTimer对象
        self.timer = QTimer(parent)
        self.timer.setInterval(1000)
        self.timer.start()

        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)

    # 定义槽
    def onTimerOut(self):
        """
        超时事件，更新 LCD 时钟
        """
        current_time = time.strftime("%X", time.localtime())
        self.lcd.display(current_time)

        if current_time == self.targetTime:
            self.timerFinished.emit()
            self.timer.stop()


class ClockWindow(QWidget):
    """
    定时器主执行程序
    """
    def __init__(self, targetTime):
        super(ClockWindow, self).__init__()
        self.targetTime = targetTime
        self.resize(350, 100)

        # 在此处设置目标时间
        self.timer_widget = MyTimer(self.targetTime)

        self.timer_widget.timerFinished.connect(self.onTimerFinished)

        layout = QVBoxLayout()
        layout.addWidget(self.timer_widget)
        self.setLayout(layout)

    def onTimerFinished(self):
        print("Timer Finished!")
        # 当计时器到达目标时间时执行某项操作
        sys.exit()

