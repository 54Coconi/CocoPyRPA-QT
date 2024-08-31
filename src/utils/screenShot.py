"""
截图模块
"""
import os

from PyQt5.QtCore import Qt, qAbs, QRect, QDateTime, QMimeData  # 用于处理核心的常量，函数和类
from PyQt5.QtGui import QPen, QPainter, QColor, QGuiApplication  # 用于处理图形，绘画，颜色和屏幕相关的功能
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem, QPushButton, QMessageBox  # 用于创建应用程序和窗口


# 截屏窗口类
class CaptureScreen(QWidget):
    """
    捕捉屏幕类
    """
    # 初始化变量
    beginPosition = None  # 记录鼠标开始位置
    endPosition = None  # 记录鼠标结束位置
    fullScreenImage = None  # 保存全屏图像
    captureImage = None  # 保存截图区域的图像
    isMousePressLeft = None  # 记录鼠标是否按下左键
    painter = QPainter()  # 创建一个绘画对象

    # 初始化方法，无参数
    def __init__(self):
        super(QWidget, self).__init__()  # 调用父类的构造函数
        self.initWindow()  # 初始化窗口
        self.captureFullScreen()  # 获取全屏

    # 初始化窗口的方法，无参数
    def initWindow(self):
        """
        初始化窗口的方法
        """
        self.setMouseTracking(True)  # 开启鼠标追踪
        self.setCursor(Qt.CrossCursor)  # 设置光标为十字形
        self.setWindowFlag(Qt.FramelessWindowHint)  # 窗口无边框
        self.setWindowState(Qt.WindowFullScreen)  # 窗口全屏

    # 获取全屏的方法，无参数
    def captureFullScreen(self):
        """
        捕获全屏的方法
        """
        # 获取全屏图像
        self.fullScreenImage = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

    # 重写鼠标按下事件的方法，接受一个 event 参数，表示事件对象
    def mousePressEvent(self, event):
        """
        鼠标按下事件的方法
        :param event:
        """
        if event.button() == Qt.LeftButton:  # 如果按下的是左键
            self.beginPosition = event.pos()  # 记录鼠标开始位置
            self.isMousePressLeft = True  # 设置鼠标是否按下左键为 True

        if event.button() == Qt.RightButton:  # 如果按下的是右键
            # 如果选取了图片,则按一次右键开始重新截图
            if self.captureImage is not None:  # 如果截图区域的图像不为空
                self.captureImage = None  # 将截图区域的图像设为空
                self.paintBackgroundImage()  # 绘制模糊背景图
                self.update()  # 更新窗口
            else:  # 如果截图区域的图像为空
                self.close()  # 关闭窗口

    # 重写鼠标移动事件的方法，接受一个 event 参数，表示事件对象
    def mouseMoveEvent(self, event):
        """
        鼠标移动事件的方法
        :param event:
        """
        if self.isMousePressLeft is True:  # 如果鼠标按下了左键
            self.endPosition = event.pos()  # 记录鼠标结束位置
            self.update()  # 更新窗口

    # 重写鼠标释放事件的方法，接受一个 event 参数，表示事件对象
    def mouseReleaseEvent(self, event):
        """
        鼠标释放事件的方法
        :param event:
        """
        self.endPosition = event.pos()  # 记录鼠标结束位置
        self.isMousePressLeft = False  # 设置鼠标是否按下左键为 False
        if event.button() == Qt.LeftButton:  # 如果释放的是左键
            # 如果只是单击而没有拖动
            if self.beginPosition == self.endPosition:
                # 获取点击处的坐标
                click_position = self.beginPosition
                # 复制到系统粘贴板
                clipboard = QGuiApplication.clipboard()
                mime_data = QMimeData()
                mime_data.setText(f"({click_position.x()},{click_position.y()})")
                clipboard.setMimeData(mime_data)

                # 给用户一个提示信息
                QMessageBox.information(self, "提示",
                                        f"坐标已复制到剪贴板：({click_position.x()}, {click_position.y()})")
            if self.beginPosition != self.endPosition and self.captureImage is not None:  # 如果截图区域的图像不为空
                self.showImagePreview()  # 保存图片

    # 重写鼠标双击事件的方法，接受一个 event 参数，表示事件对象
    def mouseDoubleClickEvent(self, event):
        """
        鼠标双击事件的方法
        :param event:
        """
        if self.captureImage is not None:  # 如果截图区域的图像不为空
            self.showImagePreview()  # 保存图片
            # self.close()  # 关闭窗口

    # 重写键盘按下事件的方法，接受一个 event 参数，表示事件对象
    def keyPressEvent(self, event):
        """
        键盘按下事件的方法
        :param event:
        """
        if event.key() == Qt.Key_Escape:  # 如果按下的是 Esc 键
            self.close()  # 关闭窗口
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 如果按下的是 Enter 键或 Return 键
            if self.captureImage is not None:  # 如果截图区域的图像不为空
                self.showImagePreview()  # 保存图片
                # self.close()  # 关闭窗口

    # 绘制模糊背景图的方法，无参数
    def paintBackgroundImage(self):
        """
        绘制模糊背景图的方法
        """
        shadowColor = QColor(0, 0, 0, 100)  # 黑色半透明
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
        if self.isMousePressLeft is True:  # 如果鼠标按下了左键
            pickRect = self.getRectangle(self.beginPosition, self.endPosition)  # 获得要截图的矩形框
            self.captureImage = self.fullScreenImage.copy(pickRect)  # 捕获截图矩形框内的图片
            self.painter.drawPixmap(pickRect.topLeft(), self.captureImage)  # 填充截图的图片
            self.painter.drawRect(pickRect)  # 画矩形边框
        self.painter.end()  # 结束重绘

    # 获取截图区域的矩形框的方法，接受两个参数，表示鼠标开始位置和结束位置
    def getRectangle(self, beginPoint, endPoint):
        """
        获取截图区域的矩形框的方法，接受两个参数，表示鼠标开始位置和结束位置
        :param beginPoint: 鼠标开始位置
        :param endPoint: 鼠标结束位置
        :return: pickRect -- 返回矩形对象
        """
        pickRectWidth = int(qAbs(beginPoint.x() - endPoint.x()))  # 计算截图区域的宽度
        pickRectHeight = int(qAbs(beginPoint.y() - endPoint.y()))  # 计算截图区域的高度
        pickRectTop = beginPoint.x() if beginPoint.x() < endPoint.x() else endPoint.x()  # 计算截图区域左上角的 x 坐标
        pickRectLeft = beginPoint.y() if beginPoint.y() < endPoint.y() else endPoint.y()  # 计算截图区域左上角的 y 坐标
        pickRect = QRect(pickRectTop, pickRectLeft, pickRectWidth, pickRectHeight)  # 创建一个矩形对象
        # 避免高度宽度为0时候报错
        if pickRectWidth == 0:  # 如果宽度为 0
            pickRect.setWidth(2)  # 将宽度设为 2
        if pickRectHeight == 0:  # 如果高度为 0
            pickRect.setHeight(2)  # 将高度设为 2

        return pickRect  # 返回矩形对象

    #
    def showImagePreview(self):
        """
        显示图片预览窗口的方法
        """
        # 创建一个对话框
        dialog = QDialog(self)
        dialog.setWindowTitle("图像预览")

        # 创建一个布局
        layout = QVBoxLayout(dialog)

        # 创建一个QGraphicsView用于显示图片
        view = QGraphicsView(dialog)
        scene = QGraphicsScene(dialog)
        item = QGraphicsPixmapItem(self.captureImage)
        scene.addItem(item)
        view.setScene(scene)

        # 将QGraphicsView添加到布局中
        layout.addWidget(view)

        # 创建保存和取消按钮
        save_button = QPushButton("保存", dialog)
        cancel_button = QPushButton("取消", dialog)

        # 保存按钮的点击事件
        save_button.clicked.connect(lambda: self.saveImage(dialog))

        # 取消按钮的点击事件
        cancel_button.clicked.connect(dialog.reject)

        # 将按钮添加到布局中
        layout.addWidget(save_button)
        layout.addWidget(cancel_button)

        # 显示对话框
        dialog.exec_()

    # 保存图片的方法，无参数
    def saveImage(self, dialog):
        """
        保存图片的方法
        """
        # 获取当前系统时间
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd-hhmmss")
        # 获取目录路径
        directory = os.path.dirname('work/IMAGES/')
        # 检查目录是否存在，如果不存在则创建
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 构造保存文件名
        file_name = os.path.join(directory, "IMAGE_{}.png".format(current_time))

        try:
            # 保存图片
            self.captureImage.save(file_name, quality=100)
            # 关闭对话框
            dialog.accept()
            # 复制到系统粘贴板
            clipboard = QGuiApplication.clipboard()
            mime_data = QMimeData()
            mime_data.setText(file_name)
            clipboard.setMimeData(mime_data)
            QMessageBox.information(self, "提示", "图片路径已保存到粘贴板", QMessageBox.Ok)

        except Exception as e:
            # 弹窗提示保存出错
            QMessageBox.critical(dialog, "错误！", f"保存图片出错：{str(e)}")

# if __name__ == "__main__":
#     # keyboard.wait(hotkey='f4')  # 按 F4 开始截图
#     app = QApplication(sys.argv)  # 创建一个应用程序对象
#     windows = CaptureScreen()  # 创建一个截屏窗口对象
#     windows.show()  # 显示窗口
#     sys.exit(app.exec_())  # 运行应用程序
