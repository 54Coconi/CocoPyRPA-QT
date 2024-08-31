import sys

from PyQt5.QtCore import Qt, QEvent, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor, QGuiApplication, QPen, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox


# import src.main.newWindow as mn


# 定义一个ScreenCoorWidget类，继承自QWidget
class ScreenCoorWidget(QWidget):
    """
    捕捉屏幕点击处坐标的类
    """
    relCoordinatesChanged = pyqtSignal(tuple)  # 相对坐标改变信号
    painter = QPainter()  # 创建一个绘画对象
    fullScreenImage = None  # 全屏图
    coordinates = []  # 用于存储鼠标点击的坐标
    RelCoordinates = ''  # 相对坐标
    Coordinate = ''  # 定点坐标
    i = 0

    def __init__(self, functype):
        self.functype = functype
        super(QWidget, self).__init__()
        self.init_ui()  # 初始化用户界面
        self.captureFullScreen()  # 获取全屏
        self.paintBackgroundImage()  # 绘制模糊背景图
        # 创建一个QPixmap对象，你可以加载你自己的图像文件
        pixmap = QPixmap('res/icons/ScreenCoordinate.png')

        # 创建一个自定义的鼠标样式
        cursor = QCursor(pixmap, -1, -1)

        # 将窗口的鼠标样式设置为自定义的鼠标样式
        self.setCursor(cursor)

    def init_ui(self):
        """
        初始化窗口的方法
        """
        self.setMouseTracking(True)  # 开启鼠标追踪
        # self.setCursor(Qt.CrossCursor)  # 设置光标为十字形
        self.setWindowFlag(Qt.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowFullScreen)  # 窗口全屏

    # 获取全屏的方法，无参数
    def captureFullScreen(self):
        """
        捕获全屏的方法
        """
        # 获取全屏图像
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

    # 绘制模糊背景图的方法，无参数
    def paintBackgroundImage(self):
        """
        绘制模糊背景图的方法
        """
        shadowColor = QColor(225, 255, 255, 100)  # 黑色半透明
        self.painter.drawPixmap(0, 0, self.fullScreenImage)  # 绘制全屏图像
        self.painter.fillRect(self.fullScreenImage.rect(), shadowColor)  # 填充矩形阴影

    # 重写绘制事件的方法，接受一个 event 参数，表示事件对象
    def paintEvent(self, event):
        """
        绘制事件的方法
        :param event:
        """
        self.painter.begin(self)  # 开始重绘
        self.paintBackgroundImage()  # 绘制模糊背景图
        penColor = QColor(113, 214, 82)  # 画笔颜色
        self.painter.setPen(QPen(penColor, 1, Qt.DashLine, Qt.RoundCap))  # 设置画笔,绿色,1px大小,实线,圆形笔帽
        self.painter.end()  # 结束重绘

    def eventFilter(self, obj, event):
        """

        :param obj:
        :param event:
        :return:
        """
        # 事件过滤器，用于处理鼠标点击事件
        if obj == self and event.type() == QEvent.MouseButtonRelease:
            # 若点击的是左键且功能指令为<鼠标相对移动>
            if event.button() == Qt.LeftButton and self.functype == 2:
                mouse_pos = event.pos()  # 获取鼠标位置
                global_pos = self.mapToGlobal(mouse_pos)  # 将鼠标位置转换为全局坐标
                if self.i == 0:
                    self.coordinates.append((global_pos.x(), global_pos.y()))  # 将坐标添加到列表中
                    QMessageBox.information(self, "提示",
                                            f"当前坐标为：{self.coordinates[self.i]}\n若要退出请按右键")  # 提示信息
                    print("当前坐标为:", global_pos.x(), global_pos.y())  # 打印点击的坐标
                    print(self.coordinates)
                    self.update_image()  # 更新图像
                    self.i += 1
                    print("i = ", self.i)
                elif self.i == 1:
                    self.coordinates.append((global_pos.x(), global_pos.y()))  # 将坐标添加到列表中
                    QMessageBox.information(self, "提示",
                                            f"目标坐标为：{self.coordinates[self.i]}")  # 提示信息
                    print("目标坐标为:", global_pos.x(), global_pos.y())  # 打印点击的坐标
                    print(self.coordinates)

                    # 计算相对坐标值
                    if len(self.coordinates) >= 2:
                        x1, y1 = self.coordinates[len(self.coordinates) - 2]  # 列表倒数第二个坐标
                        print(f"x1 = {x1}, y1 = {y1}")
                        x2, y2 = self.coordinates[len(self.coordinates) - 1]  # 列表最后一个坐标
                        print(f"x2 = {x2}, y2 = {y2}")
                        self.RelCoordinates = (x2 - x1, y2 - y1)
                        self.relCoordinatesChanged.emit(self.RelCoordinates)  # 发射信号给主窗口
                        print(f"相对坐标为：{self.RelCoordinates}")
                        QMessageBox.information(self, "提示", f"相对坐标为：{self.RelCoordinates}")  # 提示信息
                    self.close()  # 关闭应用程序

            # 若点击的是左键且功能指令为<鼠标定点移动>
            elif event.button() == Qt.LeftButton and self.functype == 1:
                mouse_pos = event.pos()  # 获取鼠标位置
                global_pos = self.mapToGlobal(mouse_pos)  # 将鼠标位置转换为全局坐标
                self.Coordinate = (global_pos.x(), global_pos.y())
                self.relCoordinatesChanged.emit(self.Coordinate)  # 发射信号给主窗口
                print("鼠标定点移动的坐标为:", self.Coordinate)  # 打印点击的坐标
                QMessageBox.information(self, "提示",
                                        f"鼠标定点移动的坐标为：{self.Coordinate}\n")  # 提示信息
                self.close()  # 关闭应用程序

            elif event.button() == Qt.RightButton:
                self.coordinates.clear()  # 清除坐标
                self.i = 0  # 将 i 归 0
                print(f"self.coordinates = {self.coordinates}\nself.i = {self.i}")
                self.close()  # 如果点击右键，则关闭应用程序
        return super().eventFilter(obj, event)

    def update_image(self):
        """
        更新图像
        """
        # 更新图像
        pixmap = QPixmap(self.size())  # 创建一个QPixmap对象
        pixmap.fill(QColor(0, 0, 0, 0))  # 设置背景为透明

        painter = QPainter(pixmap)  # 创建一个QPainter对象
        painter.setRenderHint(QPainter.Antialiasing, True)  # 设置渲染提示为抗锯齿
        painter.setPen(Qt.NoPen)  # 设置画笔为无笔
        painter.setBrush(QColor(128, 128, 128, 100))  # 设置画刷颜色

        for x, y in self.coordinates:
            local_pos = self.mapFromGlobal(QDesktopWidget().screenGeometry().topLeft())  # 将全局坐标转换为本地坐标
            painter.drawEllipse(x - local_pos.x() - 5, y - local_pos.y() - 5, 10, 10)  # 画一个椭圆

        painter.end()  # 结束绘画

    def start_capture(self):
        """
        开始
        """
        # 开始捕获
        self.installEventFilter(self)  # 安装事件过滤器

    def getValue(self):
        """
        获取坐标
        """
        relCoordinates = self.RelCoordinates
        return relCoordinates


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个QApplication对象

    capture_widget = ScreenCoorWidget()  # 创建一个ScreenCoorWidget对象
    capture_widget.show()  # 显示窗口
    capture_widget.start_capture()  # 开始捕获

    sys.exit(app.exec_())  # 运行应用程序
