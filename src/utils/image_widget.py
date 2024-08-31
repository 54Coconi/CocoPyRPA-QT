"""
在表格单元格内显示图片的模块
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDialog


class ImageWidget(QWidget):
    """
    自定义 QWidget 子类，用于显示图片
    """

    def __init__(self, image_path):
        super().__init__()
        self._image_path = image_path

        # 创建一个 QLabel 用于显示图片
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # 设置图片并显示
        self.set_image(self._image_path)

        # 创建垂直布局管理器
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # 将布局管理器设置为窗口的布局
        self.setLayout(layout)

    @property
    def image_path(self):
        """
        :return: action_list._image_path
        """
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value

        # 设置图片并显示
        self.set_image(self._image_path)

    def set_image(self, image_path):
        """
        设置图片的方法
        :param image_path:
        """
        pixmap = QPixmap(image_path)
        # 检查图片大小，如果超过 (100x100)，则缩小图片
        if pixmap.width() > 100 or pixmap.height() > 100:
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        # 将 QPixmap 设置到 QLabel 中显示
        self.label.setPixmap(pixmap)

    def set_image_for_preview(self, image_path):
        """
        设置预览窗口显示图片的方法
        :param image_path:
        """
        pixmap = QPixmap(image_path)
        # 检查图片大小，如果超过 (500x500)，则缩小图片
        if pixmap.width() > 500 or pixmap.height() > 500:
            pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def preview_image(self):
        """
        用户双击图像时的预览方法
        """
        # 创建一个新窗口
        preview_window = QDialog(self)
        preview_window.setWindowTitle("图片预览")
        # 创建一个 QLabel 用于显示图像
        preview_label = QLabel(preview_window)
        preview_label.setAlignment(Qt.AlignCenter)
        # 设置图像并显示
        self.set_image_for_preview(self._image_path)
        # 创建垂直布局管理器
        preview_layout = QVBoxLayout(preview_window)
        preview_layout.addWidget(preview_label)
        # 将布局管理器设置为窗口的布局
        preview_window.setLayout(preview_layout)
        # 设置窗口的大小
        preview_window.resize(500, 500)
        # 显示窗口
        preview_window.show()

