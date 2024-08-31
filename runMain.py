"""
程序入口，主执行程序
"""
# -----------------------------------------------------------|
#    ______                 ____        ____  ____  ___      |
#   / ____/___  _________  / __ \__  __/ __ \/ __ \/   |     |
#  / /   / __ \/ ___/ __ \/ /_/ / / / / /_/ / /_/ / /| |     |
# / /___/ /_/ / /__/ /_/ / ____/ /_/ / _, _/ ____/ ___ |     |
# \____/\____/\___/\____/_/    \__, /_/ |_/_/   /_/  |_|     |
#                             /____/                         |
# -----------------------------------------------------------|

import sys
import qdarkstyle
from os import environ

from PyQt5 import QtWidgets

import src.main.newWindow as newWindow
from src.utils.QSSLoader import QSSLoader as QL

sys.path.append('src/main')


def suppress_qt_warnings():
    """
    禁止显示 Qt 警告
    """
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    window = newWindow.CocoPyRPAApp()

    # 加载主题配置文件
    style_file = 'template/QSS/default.qss'
    style_sheet = QL.read_qss_file(style_file)
    window.setStyleSheet(style_sheet)

    # window.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())

    window.show()
    sys.exit(app.exec_())
