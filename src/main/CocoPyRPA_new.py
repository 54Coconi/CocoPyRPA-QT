# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CocoPyRPA.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 651)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.frame_list = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_list.sizePolicy().hasHeightForWidth())
        self.frame_list.setSizePolicy(sizePolicy)
        self.frame_list.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_list.setObjectName("frame_list")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_list)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setStyleSheet("")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.frame_tableAndLog = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_tableAndLog.sizePolicy().hasHeightForWidth())
        self.frame_tableAndLog.setSizePolicy(sizePolicy)
        self.frame_tableAndLog.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_tableAndLog.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tableAndLog.setObjectName("frame_tableAndLog")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_tableAndLog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_tableAndLog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(1)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_table = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_table.sizePolicy().hasHeightForWidth())
        self.frame_table.setSizePolicy(sizePolicy)
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_table)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setItalic(False)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(32)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.frame_log = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_log.sizePolicy().hasHeightForWidth())
        self.frame_log.setSizePolicy(sizePolicy)
        self.frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log.setObjectName("frame_log")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_log)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.logBrowser = QtWidgets.QTextBrowser(self.frame_log)
        self.logBrowser.setAccessibleName("")
        self.logBrowser.setAccessibleDescription("")
        self.logBrowser.setStyleSheet("")
        self.logBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logBrowser.setReadOnly(False)
        self.logBrowser.setSearchPaths([])
        self.logBrowser.setObjectName("logBrowser")
        self.verticalLayout_6.addWidget(self.logBrowser)
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.verticalLayout_4.addWidget(self.splitter)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_operation = QtWidgets.QMenu(self.menubar)
        self.menu_operation.setObjectName("menu_operation")
        self.menu_mouse = QtWidgets.QMenu(self.menu_operation)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/icons/mouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_mouse.setIcon(icon)
        self.menu_mouse.setObjectName("menu_mouse")
        self.menu_os = QtWidgets.QMenu(self.menu_operation)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/icons/os.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_os.setIcon(icon1)
        self.menu_os.setObjectName("menu_os")
        self.menu_keyboard = QtWidgets.QMenu(self.menu_operation)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/icons/keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_keyboard.setIcon(icon2)
        self.menu_keyboard.setObjectName("menu_keyboard")
        self.menu_cmd = QtWidgets.QMenu(self.menu_operation)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/icons/cmd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_cmd.setIcon(icon3)
        self.menu_cmd.setObjectName("menu_cmd")
        self.menu_other = QtWidgets.QMenu(self.menu_operation)
        self.menu_other.setObjectName("menu_other")
        self.menu_run = QtWidgets.QMenu(self.menubar)
        self.menu_run.setObjectName("menu_run")
        self.menu_tool = QtWidgets.QMenu(self.menubar)
        self.menu_tool.setObjectName("menu_tool")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_theme = QtWidgets.QMenu(self.menubar)
        self.menu_theme.setObjectName("menu_theme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setMouseTracking(False)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_file = QtWidgets.QToolBar(MainWindow)
        self.toolBar_file.setEnabled(True)
        self.toolBar_file.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar_file.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_file.setIconSize(QtCore.QSize(28, 28))
        self.toolBar_file.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar_file.setObjectName("toolBar_file")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_file)
        self.toolBar_run = QtWidgets.QToolBar(MainWindow)
        self.toolBar_run.setIconSize(QtCore.QSize(28, 28))
        self.toolBar_run.setObjectName("toolBar_run")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_run)
        self.toolBar_funcs = QtWidgets.QToolBar(MainWindow)
        self.toolBar_funcs.setObjectName("toolBar_funcs")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_funcs)
        self.toolBar_operation = QtWidgets.QToolBar(MainWindow)
        self.toolBar_operation.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar_operation.setIconSize(QtCore.QSize(28, 28))
        self.toolBar_operation.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar_operation.setObjectName("toolBar_operation")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_operation)
        self.action_menu_NewDir = QtWidgets.QAction(MainWindow)
        self.action_menu_NewDir.setCheckable(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/icons/new-dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_NewDir.setIcon(icon4)
        self.action_menu_NewDir.setObjectName("action_menu_NewDir")
        self.action_menu_Open = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("C:/Users/Administrator/res/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_menu_Open.setIcon(icon5)
        self.action_menu_Open.setObjectName("action_menu_Open")
        self.action_menu_Save = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("res/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("C:/Users/Administrator/res/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_menu_Save.setIcon(icon6)
        self.action_menu_Save.setObjectName("action_menu_Save")
        self.action_menu_SaveToExcel = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("res/icons/save-to-excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_SaveToExcel.setIcon(icon7)
        self.action_menu_SaveToExcel.setObjectName("action_menu_SaveToExcel")
        self.action_menu_OpenExcel = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("res/icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_OpenExcel.setIcon(icon8)
        self.action_menu_OpenExcel.setObjectName("action_menu_OpenExcel")
        self.action_menu_LClickOne = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("res/icons/click-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_LClickOne.setIcon(icon9)
        self.action_menu_LClickOne.setObjectName("action_menu_LClickOne")
        self.action_menu_LClickDou = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("res/icons/click-double.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_LClickDou.setIcon(icon10)
        self.action_menu_LClickDou.setObjectName("action_menu_LClickDou")
        self.action_menu_RClickOne = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("res/icons/click-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_RClickOne.setIcon(icon11)
        self.action_menu_RClickOne.setObjectName("action_menu_RClickOne")
        self.action_menu_Scroll = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("res/icons/wheel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_Scroll.setIcon(icon12)
        self.action_menu_Scroll.setObjectName("action_menu_Scroll")
        self.action_menu_MouseMoveTo = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("res/icons/mouse-move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_MouseMoveTo.setIcon(icon13)
        self.action_menu_MouseMoveTo.setObjectName("action_menu_MouseMoveTo")
        self.action_menu_MouseRelMove = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("res/icons/mouse-rel-move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_MouseRelMove.setIcon(icon14)
        self.action_menu_MouseRelMove.setObjectName("action_menu_MouseRelMove")
        self.action_menu_KeyStroke = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("res/icons/keystroke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_KeyStroke.setIcon(icon15)
        self.action_menu_KeyStroke.setObjectName("action_menu_KeyStroke")
        self.action_menu_HotkeyCombi = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("res/icons/hotkey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_HotkeyCombi.setIcon(icon16)
        self.action_menu_HotkeyCombi.setObjectName("action_menu_HotkeyCombi")
        self.action_menu_EntTxtOnKeyboard = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("res/icons/txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_EntTxtOnKeyboard.setIcon(icon17)
        self.action_menu_EntTxtOnKeyboard.setObjectName("action_menu_EntTxtOnKeyboard")
        self.action_menu_Delay = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("res/icons/delay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_Delay.setIcon(icon18)
        self.action_menu_Delay.setObjectName("action_menu_Delay")
        self.action_menu_Timing = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("res/icons/timing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_Timing.setIcon(icon19)
        self.action_menu_Timing.setObjectName("action_menu_Timing")
        self.action_menu_Input = QtWidgets.QAction(MainWindow)
        self.action_menu_Input.setObjectName("action_menu_Input")
        self.action_menu_RunAll = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("res/icons/allrun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_RunAll.setIcon(icon20)
        self.action_menu_RunAll.setObjectName("action_menu_RunAll")
        self.action_menu_RunOne = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("res/icons/run1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_menu_RunOne.setIcon(icon21)
        self.action_menu_RunOne.setObjectName("action_menu_RunOne")
        self.action_menu_SelfCmd = QtWidgets.QAction(MainWindow)
        self.action_menu_SelfCmd.setObjectName("action_menu_SelfCmd")
        self.action_RefreshDir = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("res/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_RefreshDir.setIcon(icon22)
        self.action_RefreshDir.setObjectName("action_RefreshDir")
        self.action_tool_Copy = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("res/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_Copy.setIcon(icon23)
        self.action_tool_Copy.setObjectName("action_tool_Copy")
        self.action_tool_Paste = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("res/icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_Paste.setIcon(icon24)
        self.action_tool_Paste.setObjectName("action_tool_Paste")
        self.action_tool_Delete = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("res/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_Delete.setIcon(icon25)
        self.action_tool_Delete.setObjectName("action_tool_Delete")
        self.action_tool_Add = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("res/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_Add.setIcon(icon26)
        self.action_tool_Add.setObjectName("action_tool_Add")
        self.action_tool_InsertDown = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("res/icons/insert-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_InsertDown.setIcon(icon27)
        self.action_tool_InsertDown.setObjectName("action_tool_InsertDown")
        self.action_tool_InsertUp = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("res/icons/insert-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_InsertUp.setIcon(icon28)
        self.action_tool_InsertUp.setObjectName("action_tool_InsertUp")
        self.action_tool_MoveUp = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("res/icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_MoveUp.setIcon(icon29)
        self.action_tool_MoveUp.setObjectName("action_tool_MoveUp")
        self.action_tool_MoveDown = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("res/icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_MoveDown.setIcon(icon30)
        self.action_tool_MoveDown.setObjectName("action_tool_MoveDown")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_cmdDesc = QtWidgets.QAction(MainWindow)
        self.action_cmdDesc.setObjectName("action_cmdDesc")
        self.action_tool_screenShot = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("res/icons/screen_shot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_tool_screenShot.setIcon(icon31)
        self.action_tool_screenShot.setObjectName("action_tool_screenShot")
        self.action_menu_defaultTheme = QtWidgets.QAction(MainWindow)
        self.action_menu_defaultTheme.setObjectName("action_menu_defaultTheme")
        self.action_menu_darkTheme = QtWidgets.QAction(MainWindow)
        self.action_menu_darkTheme.setObjectName("action_menu_darkTheme")
        self.action_menu_lightTheme = QtWidgets.QAction(MainWindow)
        self.action_menu_lightTheme.setObjectName("action_menu_lightTheme")
        self.action_menu_protectEyesTheme = QtWidgets.QAction(MainWindow)
        self.action_menu_protectEyesTheme.setObjectName("action_menu_protectEyesTheme")
        self.action_menu_checkUpdate = QtWidgets.QAction(MainWindow)
        self.action_menu_checkUpdate.setObjectName("action_menu_checkUpdate")
        self.menu_file.addAction(self.action_menu_NewDir)
        self.menu_file.addAction(self.action_menu_Open)
        self.menu_file.addAction(self.action_menu_Save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_menu_SaveToExcel)
        self.menu_file.addAction(self.action_menu_OpenExcel)
        self.menu_mouse.addAction(self.action_menu_LClickOne)
        self.menu_mouse.addAction(self.action_menu_LClickDou)
        self.menu_mouse.addAction(self.action_menu_RClickOne)
        self.menu_mouse.addAction(self.action_menu_Scroll)
        self.menu_mouse.addAction(self.action_menu_MouseMoveTo)
        self.menu_mouse.addAction(self.action_menu_MouseRelMove)
        self.menu_os.addAction(self.action_menu_Delay)
        self.menu_os.addAction(self.action_menu_Timing)
        self.menu_keyboard.addAction(self.action_menu_KeyStroke)
        self.menu_keyboard.addAction(self.action_menu_HotkeyCombi)
        self.menu_keyboard.addAction(self.action_menu_EntTxtOnKeyboard)
        self.menu_cmd.addAction(self.action_menu_SelfCmd)
        self.menu_other.addAction(self.action_menu_Input)
        self.menu_operation.addAction(self.menu_mouse.menuAction())
        self.menu_operation.addAction(self.menu_keyboard.menuAction())
        self.menu_operation.addAction(self.menu_os.menuAction())
        self.menu_operation.addSeparator()
        self.menu_operation.addAction(self.menu_cmd.menuAction())
        self.menu_operation.addAction(self.menu_other.menuAction())
        self.menu_run.addAction(self.action_menu_RunAll)
        self.menu_run.addAction(self.action_menu_RunOne)
        self.menu_help.addAction(self.action_cmdDesc)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_menu_checkUpdate)
        self.menu_theme.addAction(self.action_menu_defaultTheme)
        self.menu_theme.addAction(self.action_menu_darkTheme)
        self.menu_theme.addAction(self.action_menu_lightTheme)
        self.menu_theme.addAction(self.action_menu_protectEyesTheme)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_operation.menuAction())
        self.menubar.addAction(self.menu_run.menuAction())
        self.menubar.addAction(self.menu_tool.menuAction())
        self.menubar.addAction(self.menu_theme.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolBar_file.addAction(self.action_RefreshDir)
        self.toolBar_file.addAction(self.action_menu_NewDir)
        self.toolBar_file.addAction(self.action_menu_Open)
        self.toolBar_file.addAction(self.action_menu_Save)
        self.toolBar_run.addAction(self.action_menu_RunAll)
        self.toolBar_run.addAction(self.action_menu_RunOne)
        self.toolBar_funcs.addAction(self.action_menu_LClickOne)
        self.toolBar_funcs.addAction(self.action_menu_LClickDou)
        self.toolBar_funcs.addAction(self.action_menu_RClickOne)
        self.toolBar_funcs.addAction(self.action_menu_Scroll)
        self.toolBar_funcs.addAction(self.action_menu_MouseMoveTo)
        self.toolBar_funcs.addAction(self.action_menu_MouseRelMove)
        self.toolBar_funcs.addSeparator()
        self.toolBar_funcs.addAction(self.action_menu_KeyStroke)
        self.toolBar_funcs.addAction(self.action_menu_HotkeyCombi)
        self.toolBar_funcs.addAction(self.action_menu_EntTxtOnKeyboard)
        self.toolBar_funcs.addSeparator()
        self.toolBar_funcs.addAction(self.action_menu_Delay)
        self.toolBar_funcs.addAction(self.action_menu_Timing)
        self.toolBar_operation.addAction(self.action_tool_Copy)
        self.toolBar_operation.addAction(self.action_tool_Paste)
        self.toolBar_operation.addAction(self.action_tool_Delete)
        self.toolBar_operation.addSeparator()
        self.toolBar_operation.addAction(self.action_tool_Add)
        self.toolBar_operation.addAction(self.action_tool_InsertUp)
        self.toolBar_operation.addAction(self.action_tool_InsertDown)
        self.toolBar_operation.addAction(self.action_tool_MoveUp)
        self.toolBar_operation.addAction(self.action_tool_MoveDown)
        self.toolBar_operation.addSeparator()
        self.toolBar_operation.addAction(self.action_tool_screenShot)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setStatusTip(_translate("MainWindow", "指令表"))
        self.tableWidget.setSortingEnabled(False)
        self.logBrowser.setStatusTip(_translate("MainWindow", "日志区"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_operation.setTitle(_translate("MainWindow", "操作"))
        self.menu_mouse.setTitle(_translate("MainWindow", "鼠标"))
        self.menu_os.setTitle(_translate("MainWindow", "系统"))
        self.menu_keyboard.setTitle(_translate("MainWindow", "键盘"))
        self.menu_cmd.setTitle(_translate("MainWindow", "cmd指令"))
        self.menu_other.setTitle(_translate("MainWindow", "其它"))
        self.menu_run.setTitle(_translate("MainWindow", "运行"))
        self.menu_tool.setTitle(_translate("MainWindow", "工具"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.menu_theme.setTitle(_translate("MainWindow", "主题"))
        self.toolBar_file.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_run.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_funcs.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar_operation.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_menu_NewDir.setText(_translate("MainWindow", "新建任务"))
        self.action_menu_NewDir.setToolTip(_translate("MainWindow", "新建任务"))
        self.action_menu_NewDir.setStatusTip(_translate("MainWindow", "新建任务目录"))
        self.action_menu_NewDir.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_menu_Open.setText(_translate("MainWindow", "打开"))
        self.action_menu_Open.setToolTip(_translate("MainWindow", "打开"))
        self.action_menu_Open.setStatusTip(_translate("MainWindow", "打开任务目录"))
        self.action_menu_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_menu_Save.setText(_translate("MainWindow", "保存"))
        self.action_menu_Save.setToolTip(_translate("MainWindow", "保存"))
        self.action_menu_Save.setStatusTip(_translate("MainWindow", "保存任务配置"))
        self.action_menu_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_menu_SaveToExcel.setText(_translate("MainWindow", "另存为 Excel 表格"))
        self.action_menu_SaveToExcel.setToolTip(_translate("MainWindow", "另存为 Excel 表格"))
        self.action_menu_SaveToExcel.setStatusTip(_translate("MainWindow", "将指令配置保存到 Excel 表格"))
        self.action_menu_OpenExcel.setText(_translate("MainWindow", "加载 Excel 数据"))
        self.action_menu_OpenExcel.setToolTip(_translate("MainWindow", "加载 Excel 数据"))
        self.action_menu_OpenExcel.setStatusTip(_translate("MainWindow", "加载 Excel 指令内容"))
        self.action_menu_LClickOne.setText(_translate("MainWindow", "单击左键"))
        self.action_menu_LClickOne.setToolTip(_translate("MainWindow", "单击左键"))
        self.action_menu_LClickOne.setStatusTip(_translate("MainWindow", "模拟鼠标左键单击"))
        self.action_menu_LClickOne.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.action_menu_LClickDou.setText(_translate("MainWindow", "双击左键"))
        self.action_menu_LClickDou.setToolTip(_translate("MainWindow", "双击左键"))
        self.action_menu_LClickDou.setStatusTip(_translate("MainWindow", "模拟鼠标双击左键"))
        self.action_menu_LClickDou.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action_menu_RClickOne.setText(_translate("MainWindow", "单击右键"))
        self.action_menu_RClickOne.setToolTip(_translate("MainWindow", "单击右键"))
        self.action_menu_RClickOne.setStatusTip(_translate("MainWindow", "模拟鼠标右键单击"))
        self.action_menu_RClickOne.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_menu_Scroll.setText(_translate("MainWindow", "滚轮"))
        self.action_menu_Scroll.setToolTip(_translate("MainWindow", "滚轮"))
        self.action_menu_Scroll.setStatusTip(_translate("MainWindow", "鼠标滚轮滚动指令,负数上滑，正数下滑，0不滑动"))
        self.action_menu_Scroll.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.action_menu_MouseMoveTo.setText(_translate("MainWindow", "鼠标定点移动"))
        self.action_menu_MouseMoveTo.setToolTip(_translate("MainWindow", "鼠标定点移动"))
        self.action_menu_MouseMoveTo.setStatusTip(_translate("MainWindow", "鼠标移动到指定的绝对坐标"))
        self.action_menu_MouseMoveTo.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.action_menu_MouseRelMove.setText(_translate("MainWindow", "鼠标相对移动"))
        self.action_menu_MouseRelMove.setToolTip(_translate("MainWindow", "鼠标相对移动"))
        self.action_menu_MouseRelMove.setStatusTip(_translate("MainWindow", "鼠标相对当前坐标移动"))
        self.action_menu_MouseRelMove.setShortcut(_translate("MainWindow", "Ctrl+6"))
        self.action_menu_KeyStroke.setText(_translate("MainWindow", "按键"))
        self.action_menu_KeyStroke.setToolTip(_translate("MainWindow", "按键"))
        self.action_menu_KeyStroke.setStatusTip(
            _translate("MainWindow", "模拟键盘【单个按钮】按下和释放（如“enter”、“a”、“F11”等）"))
        self.action_menu_HotkeyCombi.setText(_translate("MainWindow", "热键组合"))
        self.action_menu_HotkeyCombi.setToolTip(_translate("MainWindow", "热键组合"))
        self.action_menu_HotkeyCombi.setStatusTip(_translate("MainWindow", "热键之间的组合，如（Ctrl+V、win+R等等）"))
        self.action_menu_EntTxtOnKeyboard.setText(_translate("MainWindow", "键盘输入TXT内容"))
        self.action_menu_EntTxtOnKeyboard.setToolTip(_translate("MainWindow", "键盘输入TXT内容"))
        self.action_menu_EntTxtOnKeyboard.setStatusTip(
            _translate("MainWindow", "根据txt文本内容【不支持中文内容】依次执行<按键>操作，即模拟连续的按键"))
        self.action_menu_Delay.setText(_translate("MainWindow", "延时"))
        self.action_menu_Delay.setToolTip(_translate("MainWindow", "延时"))
        self.action_menu_Delay.setStatusTip(_translate("MainWindow", "等待--时间/秒，可以为小数"))
        self.action_menu_Timing.setText(_translate("MainWindow", "定时"))
        self.action_menu_Timing.setToolTip(_translate("MainWindow", "定时"))
        self.action_menu_Timing.setStatusTip(_translate("MainWindow", "定时到指定时间执行任务"))
        self.action_menu_Input.setText(_translate("MainWindow", "（从剪贴板）输入"))
        self.action_menu_Input.setToolTip(_translate("MainWindow", "（从剪贴板）输入"))
        self.action_menu_Input.setStatusTip(_translate("MainWindow", "复制指令中要输入的文本后，从剪贴板粘贴到目标位置"))
        self.action_menu_RunAll.setText(_translate("MainWindow", "运行一次"))
        self.action_menu_RunAll.setToolTip(_translate("MainWindow", "运行一次"))
        self.action_menu_RunAll.setStatusTip(_translate("MainWindow", "将所有的功能指令从头到尾执行一次"))
        self.action_menu_RunAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+F5"))
        self.action_menu_RunOne.setText(_translate("MainWindow", "指定运行"))
        self.action_menu_RunOne.setToolTip(_translate("MainWindow", "指定运行"))
        self.action_menu_RunOne.setStatusTip(_translate("MainWindow", "指定一个功能运行一次"))
        self.action_menu_RunOne.setShortcut(_translate("MainWindow", "Ctrl+Shift+F6"))
        self.action_menu_SelfCmd.setText(_translate("MainWindow", "自定义cmd指令"))
        self.action_menu_SelfCmd.setToolTip(_translate("MainWindow", "自定义cmd指令"))
        self.action_menu_SelfCmd.setStatusTip(_translate("MainWindow", "自定义cmd指令（保证指令可以在cmd窗口正常执行）"))
        self.action_RefreshDir.setText(_translate("MainWindow", "刷新任务列表"))
        self.action_RefreshDir.setToolTip(_translate("MainWindow", "刷新任务列表"))
        self.action_RefreshDir.setStatusTip(_translate("MainWindow", "刷新任务列表的目录"))
        self.action_tool_Copy.setText(_translate("MainWindow", "复制"))
        self.action_tool_Copy.setToolTip(_translate("MainWindow", "复制"))
        self.action_tool_Copy.setStatusTip(_translate("MainWindow", "复制一行指令"))
        self.action_tool_Copy.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.action_tool_Paste.setText(_translate("MainWindow", "粘贴"))
        self.action_tool_Paste.setToolTip(_translate("MainWindow", "粘贴"))
        self.action_tool_Paste.setStatusTip(_translate("MainWindow", "粘贴一行指令"))
        self.action_tool_Paste.setShortcut(_translate("MainWindow", "Ctrl+Shift+V"))
        self.action_tool_Delete.setText(_translate("MainWindow", "删除"))
        self.action_tool_Delete.setToolTip(_translate("MainWindow", "删除"))
        self.action_tool_Delete.setStatusTip(_translate("MainWindow", "删除一行指令"))
        self.action_tool_Delete.setShortcut(_translate("MainWindow", "Del"))
        self.action_tool_Add.setText(_translate("MainWindow", "增加"))
        self.action_tool_Add.setToolTip(_translate("MainWindow", "增加"))
        self.action_tool_Add.setStatusTip(_translate("MainWindow", "增加一行指令"))
        self.action_tool_InsertDown.setText(_translate("MainWindow", "插入下方"))
        self.action_tool_InsertDown.setToolTip(_translate("MainWindow", "插入下方"))
        self.action_tool_InsertDown.setStatusTip(_translate("MainWindow", "在当前选中的指令下方插入一行"))
        self.action_tool_InsertUp.setText(_translate("MainWindow", "插入上方"))
        self.action_tool_InsertUp.setStatusTip(_translate("MainWindow", "在当前选中的指令上方插入一行"))
        self.action_tool_MoveUp.setText(_translate("MainWindow", "上移"))
        self.action_tool_MoveUp.setStatusTip(_translate("MainWindow", "将当前选中指令上移一行"))
        self.action_tool_MoveUp.setShortcut(_translate("MainWindow", "Up"))
        self.action_tool_MoveDown.setText(_translate("MainWindow", "下移"))
        self.action_tool_MoveDown.setStatusTip(_translate("MainWindow", "将当前选中指令下移一行"))
        self.action_tool_MoveDown.setShortcut(_translate("MainWindow", "Down"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_cmdDesc.setText(_translate("MainWindow", "功能说明"))
        self.action_tool_screenShot.setText(_translate("MainWindow", "截图"))
        self.action_tool_screenShot.setShortcut(_translate("MainWindow", "Ctrl+Shift+F4"))
        self.action_menu_defaultTheme.setText(_translate("MainWindow", "默认"))
        self.action_menu_defaultTheme.setToolTip(_translate("MainWindow", "默认主题"))
        self.action_menu_darkTheme.setText(_translate("MainWindow", "深色"))
        self.action_menu_darkTheme.setToolTip(_translate("MainWindow", "深色主题"))
        self.action_menu_lightTheme.setText(_translate("MainWindow", "明亮"))
        self.action_menu_lightTheme.setToolTip(_translate("MainWindow", "明亮主题"))
        self.action_menu_protectEyesTheme.setText(_translate("MainWindow", "护眼"))
        self.action_menu_protectEyesTheme.setToolTip(_translate("MainWindow", "护眼主题"))
        self.action_menu_checkUpdate.setText(_translate("MainWindow", "检查更新"))
        self.action_menu_checkUpdate.setToolTip(_translate("MainWindow", "检查更新"))
