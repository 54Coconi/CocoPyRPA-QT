"""
定时模块
"""
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTimeEdit


class TimingDialog(QDialog):
    """
    定时设置弹窗类
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('设置定时')
        layout = QVBoxLayout(self)

        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat('HH:mm:ss')

        layout.addWidget(QLabel('目标时间:', self))
        layout.addWidget(self.time_edit)

        confirm_button = QPushButton('确认', self)
        confirm_button.clicked.connect(self.accept)

        layout.addWidget(confirm_button)
