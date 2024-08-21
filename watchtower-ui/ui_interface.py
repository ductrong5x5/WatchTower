# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacefhcgkZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 664)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border:none	\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header_frame = QFrame(self.centralwidget)
        self.Header_frame.setObjectName(u"Header_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header_frame.sizePolicy().hasHeightForWidth())
        self.Header_frame.setSizePolicy(sizePolicy)
        self.Header_frame.setMaximumSize(QSize(16777215, 77))
        self.Header_frame.setStyleSheet(u"\n"
"border-style: solid;\n"
"border-width:2px;\n"
"\n"
"\n"
"")
        self.Header_frame.setFrameShape(QFrame.StyledPanel)
        self.Header_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.Header_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(114, 107))
        self.frame.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(255,255,255);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Minimize_window_button = QPushButton(self.frame)
        self.Minimize_window_button.setObjectName(u"Minimize_window_button")
        self.Minimize_window_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        icon = QIcon()
        icon.addFile(u":/image/icons8-minimize-window-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize_window_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.Minimize_window_button)

        self.resize_window_button = QPushButton(self.frame)
        self.resize_window_button.setObjectName(u"resize_window_button")
        self.resize_window_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/image/icons8-restore-down-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.resize_window_button)

        self.Close_window_button = QPushButton(self.frame)
        self.Close_window_button.setObjectName(u"Close_window_button")
        self.Close_window_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/image/icons8-close-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_window_button.setIcon(icon2)
        self.Close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.Close_window_button)


        self.gridLayout_5.addWidget(self.frame, 0, 4, 1, 1)

        self.frame_12 = QFrame(self.Header_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(400, 16777215))
        self.frame_12.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(255,255,255);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setIndent(0)

        self.horizontalLayout_11.addWidget(self.label_4, 0, Qt.AlignRight)

        self.Userid = QLabel(self.frame_12)
        self.Userid.setObjectName(u"Userid")
        self.Userid.setMinimumSize(QSize(335, 5))
        self.Userid.setMaximumSize(QSize(114, 41))
        self.Userid.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.horizontalLayout_11.addWidget(self.Userid)


        self.gridLayout_5.addWidget(self.frame_12, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.Header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(100, 50))
        self.frame_3.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(255,255,255);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_menu_button = QPushButton(self.frame_3)
        self.open_menu_button.setObjectName(u"open_menu_button")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.open_menu_button.setFont(font)
        self.open_menu_button.setStyleSheet(u"color: rgb(0, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/image/icons8-menu-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_menu_button.setIcon(icon3)
        self.open_menu_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.open_menu_button, 0, Qt.AlignLeft)


        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.Header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(9999999, 9999999))
        self.frame_2.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(255,255,255);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Name_app = QLabel(self.frame_2)
        self.Name_app.setObjectName(u"Name_app")
        self.Name_app.setMaximumSize(QSize(225, 108))
        self.Name_app.setFont(font)
        self.Name_app.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.Name_app, 0, Qt.AlignHCenter)


        self.gridLayout_5.addWidget(self.frame_2, 0, 2, 1, 2)


        self.verticalLayout.addWidget(self.Header_frame)

        self.Main_frame = QFrame(self.centralwidget)
        self.Main_frame.setObjectName(u"Main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Main_frame.sizePolicy().hasHeightForWidth())
        self.Main_frame.setSizePolicy(sizePolicy1)
        self.Main_frame.setToolTipDuration(-7)
        self.Main_frame.setStyleSheet(u"\n"
"\n"
"border-style: solid;\n"
"border-width:1px;\n"
"\n"
"\n"
"")
        self.Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Main_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Left_main_frame = QFrame(self.Main_frame)
        self.Left_main_frame.setObjectName(u"Left_main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Left_main_frame.sizePolicy().hasHeightForWidth())
        self.Left_main_frame.setSizePolicy(sizePolicy2)
        self.Left_main_frame.setMinimumSize(QSize(50, 0))
        self.Left_main_frame.setMaximumSize(QSize(50, 16777215))
        self.Left_main_frame.setStyleSheet(u"")
        self.Left_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Left_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Left_main_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Menu_frame = QFrame(self.Left_main_frame)
        self.Menu_frame.setObjectName(u"Menu_frame")
        self.Menu_frame.setMinimumSize(QSize(100, 0))
        self.Menu_frame.setFrameShape(QFrame.StyledPanel)
        self.Menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.systeminformation_button_page = QPushButton(self.Menu_frame)
        self.systeminformation_button_page.setObjectName(u"systeminformation_button_page")
        sizePolicy.setHeightForWidth(self.systeminformation_button_page.sizePolicy().hasHeightForWidth())
        self.systeminformation_button_page.setSizePolicy(sizePolicy)
        self.systeminformation_button_page.setToolTipDuration(-2)
        self.systeminformation_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/image/icons8-system-information-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.systeminformation_button_page.setIcon(icon4)
        self.systeminformation_button_page.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.systeminformation_button_page, 2, 0, 1, 1, Qt.AlignLeft)

        self.systeminfo_label = QLabel(self.Menu_frame)
        self.systeminfo_label.setObjectName(u"systeminfo_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.systeminfo_label.setFont(font1)
        self.systeminfo_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.systeminfo_label.setMargin(5)

        self.gridLayout.addWidget(self.systeminfo_label, 2, 1, 1, 1, Qt.AlignLeft)

        self.network_label = QLabel(self.Menu_frame)
        self.network_label.setObjectName(u"network_label")
        self.network_label.setFont(font1)
        self.network_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.network_label.setMargin(5)

        self.gridLayout.addWidget(self.network_label, 5, 1, 1, 1, Qt.AlignLeft)

        self.storage_button_page = QPushButton(self.Menu_frame)
        self.storage_button_page.setObjectName(u"storage_button_page")
        sizePolicy.setHeightForWidth(self.storage_button_page.sizePolicy().hasHeightForWidth())
        self.storage_button_page.setSizePolicy(sizePolicy)
        self.storage_button_page.setToolTipDuration(-2)
        self.storage_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/image/icons8-stack-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_button_page.setIcon(icon5)
        self.storage_button_page.setIconSize(QSize(42, 50))

        self.gridLayout.addWidget(self.storage_button_page, 4, 0, 1, 1, Qt.AlignLeft)

        self.network_button_page = QPushButton(self.Menu_frame)
        self.network_button_page.setObjectName(u"network_button_page")
        sizePolicy.setHeightForWidth(self.network_button_page.sizePolicy().hasHeightForWidth())
        self.network_button_page.setSizePolicy(sizePolicy)
        self.network_button_page.setToolTipDuration(-2)
        self.network_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/image/icons8-wi-fi-connected-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button_page.setIcon(icon6)
        self.network_button_page.setIconSize(QSize(40, 50))

        self.gridLayout.addWidget(self.network_button_page, 5, 0, 1, 1)

        self.storage_label = QLabel(self.Menu_frame)
        self.storage_label.setObjectName(u"storage_label")
        self.storage_label.setFont(font1)
        self.storage_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.storage_label.setMargin(5)

        self.gridLayout.addWidget(self.storage_label, 4, 1, 1, 1, Qt.AlignLeft)

        self.battery_label = QLabel(self.Menu_frame)
        self.battery_label.setObjectName(u"battery_label")
        self.battery_label.setFont(font1)
        self.battery_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.battery_label.setMargin(5)

        self.gridLayout.addWidget(self.battery_label, 1, 1, 1, 1, Qt.AlignLeft)

        self.cpu_button_page = QPushButton(self.Menu_frame)
        self.cpu_button_page.setObjectName(u"cpu_button_page")
        sizePolicy.setHeightForWidth(self.cpu_button_page.sizePolicy().hasHeightForWidth())
        self.cpu_button_page.setSizePolicy(sizePolicy)
        self.cpu_button_page.setToolTipDuration(-2)
        self.cpu_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/image/icons8-microchip-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_button_page.setIcon(icon7)
        self.cpu_button_page.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.cpu_button_page, 0, 0, 1, 1)

        self.cpu_label = QLabel(self.Menu_frame)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setMinimumSize(QSize(280, 0))
        self.cpu_label.setFont(font1)
        self.cpu_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.cpu_label, 0, 1, 1, 1)

        self.battery_button_page = QPushButton(self.Menu_frame)
        self.battery_button_page.setObjectName(u"battery_button_page")
        sizePolicy.setHeightForWidth(self.battery_button_page.sizePolicy().hasHeightForWidth())
        self.battery_button_page.setSizePolicy(sizePolicy)
        self.battery_button_page.setToolTipDuration(-2)
        self.battery_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/image/icons8-full-battery-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_button_page.setIcon(icon8)
        self.battery_button_page.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.battery_button_page, 1, 0, 1, 1, Qt.AlignLeft)

        self.activity_button_page = QPushButton(self.Menu_frame)
        self.activity_button_page.setObjectName(u"activity_button_page")
        sizePolicy2.setHeightForWidth(self.activity_button_page.sizePolicy().hasHeightForWidth())
        self.activity_button_page.setSizePolicy(sizePolicy2)
        self.activity_button_page.setToolTipDuration(-2)
        self.activity_button_page.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/image/icons8-ecg-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_button_page.setIcon(icon9)
        self.activity_button_page.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.activity_button_page, 3, 0, 1, 1, Qt.AlignLeft)

        self.activity_label = QLabel(self.Menu_frame)
        self.activity_label.setObjectName(u"activity_label")
        self.activity_label.setFont(font1)
        self.activity_label.setStyleSheet(u"\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.activity_label.setMargin(5)

        self.gridLayout.addWidget(self.activity_label, 3, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.Menu_frame)


        self.horizontalLayout_8.addWidget(self.Left_main_frame)

        self.Center_main_frame = QFrame(self.Main_frame)
        self.Center_main_frame.setObjectName(u"Center_main_frame")
        sizePolicy2.setHeightForWidth(self.Center_main_frame.sizePolicy().hasHeightForWidth())
        self.Center_main_frame.setSizePolicy(sizePolicy2)
        self.Center_main_frame.setStyleSheet(u"")
        self.Center_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Center_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Center_main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Center_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setToolTipDuration(1)
        self.stackedWidget.setStyleSheet(u"background-color:#98D8AA;")
        self.stackedWidget.setLineWidth(0)
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setStyleSheet(u"\n"
"background-color: #FF6D60;\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setMaximumSize(QSize(402, 400))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.cpu_count.setFont(font2)
        self.cpu_count.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.cpu_count, 0, 3, 1, 1)

        self.label_5 = QLabel(self.cpu_info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_7 = QLabel(self.cpu_info_frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(200, 100))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_3 = QLabel(self.cpu_info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setFont(font2)
        self.cpu_per.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.cpu_per, 1, 3, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setMaximumSize(QSize(100, 100))
        self.cpu_main_core.setFont(font2)
        self.cpu_main_core.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.cpu_main_core, 2, 3, 1, 1)

        self.label_12 = QLabel(self.cpu_info_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"\n"
"")

        self.gridLayout_3.addWidget(self.label_12, 3, 2, 1, 1)

        self.cpu_chart = roundProgressBar(self.cpu_info_frame)
        self.cpu_chart.setObjectName(u"cpu_chart")
        self.cpu_chart.setMinimumSize(QSize(200, 200))
        self.cpu_chart.setMaximumSize(QSize(300, 300))
        self.cpu_chart.setStyleSheet(u"background-color: #126782;")

        self.gridLayout_3.addWidget(self.cpu_chart, 0, 1, 4, 1)

        self.clockspeed = QLabel(self.cpu_info_frame)
        self.clockspeed.setObjectName(u"clockspeed")
        self.clockspeed.setFont(font2)

        self.gridLayout_3.addWidget(self.clockspeed, 3, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setStyleSheet(u"background-color: #F7D060;\n"
"\n"
"border-width:0px;\n"
"\n"
"\n"
"")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.ram_info_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(200, 100))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setFont(font2)
        self.available_ram.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_14 = QLabel(self.ram_info_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setMaximumSize(QSize(100, 100))
        self.total_ram.setFont(font2)
        self.total_ram.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.total_ram, 0, 1, 1, 1)

        self.ram_used = QLabel(self.ram_info_frame)
        self.ram_used.setObjectName(u"ram_used")
        self.ram_used.setFont(font2)
        self.ram_used.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.ram_used, 2, 1, 1, 1)

        self.label_13 = QLabel(self.ram_info_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.ram_chart = roundProgressBar(self.ram_info_frame)
        self.ram_chart.setObjectName(u"ram_chart")
        self.ram_chart.setMinimumSize(QSize(150, 150))
        self.ram_chart.setMaximumSize(QSize(300, 300))
        self.ram_chart.setStyleSheet(u"background-color: #126782;")

        self.gridLayout_4.addWidget(self.ram_chart, 0, 2, 3, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_6 = QVBoxLayout(self.battery)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.battery)
        self.label_20.setObjectName(u"label_20")
        font3 = QFont()
        font3.setPointSize(45)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.verticalLayout_6.addWidget(self.label_20, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.battery)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 44))
        self.frame_4.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setMinimumSize(QSize(96, 33))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.horizontalLayout_3.addWidget(self.label_22)

        self.battery_status = QLabel(self.frame_4)
        self.battery_status.setObjectName(u"battery_status")
        sizePolicy.setHeightForWidth(self.battery_status.sizePolicy().hasHeightForWidth())
        self.battery_status.setSizePolicy(sizePolicy)
        self.battery_status.setMinimumSize(QSize(200, 50))
        self.battery_status.setMaximumSize(QSize(16777215, 60))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.battery_status.setFont(font5)
        self.battery_status.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.horizontalLayout_3.addWidget(self.battery_status)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.battery)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border-width:0;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.batery_frame = QFrame(self.frame_6)
        self.batery_frame.setObjectName(u"batery_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.batery_frame.sizePolicy().hasHeightForWidth())
        self.batery_frame.setSizePolicy(sizePolicy5)
        self.batery_frame.setStyleSheet(u"background-color: #F7D060;\n"
"\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"\n"
"    \n"
"    \n"
"")
        self.batery_frame.setFrameShape(QFrame.StyledPanel)
        self.batery_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.batery_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_15 = QFrame(self.batery_frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-width:0;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_23 = QLabel(self.frame_15)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.verticalLayout_8.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_15)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.verticalLayout_8.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_15)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 14px;\n"
"    \n"
"    \n"
"")

        self.verticalLayout_8.addWidget(self.label_25)


        self.horizontalLayout_13.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.batery_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border-width:0;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.battery_charge = QLabel(self.frame_16)
        self.battery_charge.setObjectName(u"battery_charge")
        sizePolicy.setHeightForWidth(self.battery_charge.sizePolicy().hasHeightForWidth())
        self.battery_charge.setSizePolicy(sizePolicy)
        self.battery_charge.setMinimumSize(QSize(0, 0))
        self.battery_charge.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(15)
        self.battery_charge.setFont(font6)
        self.battery_charge.setStyleSheet(u"border-width: 0px;")

        self.verticalLayout_12.addWidget(self.battery_charge)

        self.battery_timeleft = QLabel(self.frame_16)
        self.battery_timeleft.setObjectName(u"battery_timeleft")
        sizePolicy2.setHeightForWidth(self.battery_timeleft.sizePolicy().hasHeightForWidth())
        self.battery_timeleft.setSizePolicy(sizePolicy2)
        self.battery_timeleft.setMinimumSize(QSize(0, 0))
        self.battery_timeleft.setFont(font6)
        self.battery_timeleft.setStyleSheet(u"border-width: 0px;")

        self.verticalLayout_12.addWidget(self.battery_timeleft)

        self.battery_plugged = QLabel(self.frame_16)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font6)
        self.battery_plugged.setStyleSheet(u"border-width: 0px;")

        self.verticalLayout_12.addWidget(self.battery_plugged)


        self.horizontalLayout_13.addWidget(self.frame_16)

        self.battery_chart = roundProgressBar(self.batery_frame)
        self.battery_chart.setObjectName(u"battery_chart")
        self.battery_chart.setMinimumSize(QSize(95, 200))
        self.battery_chart.setMaximumSize(QSize(9999, 9999))

        self.horizontalLayout_13.addWidget(self.battery_chart)


        self.horizontalLayout.addWidget(self.batery_frame)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.battery)
        self.systeminfo = QWidget()
        self.systeminfo.setObjectName(u"systeminfo")
        self.verticalLayout_4 = QVBoxLayout(self.systeminfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.system_info_frame = QFrame(self.systeminfo)
        self.system_info_frame.setObjectName(u"system_info_frame")
        self.system_info_frame.setStyleSheet(u"\n"
"border-width: 0px;\n"
"\n"
"    \n"
"")
        self.system_info_frame.setFrameShape(QFrame.StyledPanel)
        self.system_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.system_info_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_26 = QLabel(self.system_info_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_26, 4, 2, 1, 1)

        self.bitness = QLabel(self.system_info_frame)
        self.bitness.setObjectName(u"bitness")
        font7 = QFont()
        font7.setPointSize(13)
        self.bitness.setFont(font7)

        self.gridLayout_7.addWidget(self.bitness, 4, 1, 1, 1)

        self.label_35 = QLabel(self.system_info_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_41 = QLabel(self.system_info_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_41, 3, 2, 1, 1)

        self.label_30 = QLabel(self.system_info_frame)
        self.label_30.setObjectName(u"label_30")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setPointSize(43)
        self.label_30.setFont(font8)
        self.label_30.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 4, Qt.AlignBottom)

        self.machine11 = QLabel(self.system_info_frame)
        self.machine11.setObjectName(u"machine11")
        self.machine11.setFont(font7)

        self.gridLayout_7.addWidget(self.machine11, 3, 3, 1, 1)

        self.sysdate = QLabel(self.system_info_frame)
        self.sysdate.setObjectName(u"sysdate")
        self.sysdate.setFont(font7)

        self.gridLayout_7.addWidget(self.sysdate, 5, 1, 1, 1)

        self.label_15 = QLabel(self.system_info_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_33 = QLabel(self.system_info_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)

        self.systime = QLabel(self.system_info_frame)
        self.systime.setObjectName(u"systime")
        self.systime.setFont(font7)

        self.gridLayout_7.addWidget(self.systime, 5, 3, 1, 1)

        self.label_34 = QLabel(self.system_info_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_34, 3, 0, 1, 1)

        self.label_42 = QLabel(self.system_info_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_42, 5, 2, 1, 1)

        self.Platform = QLabel(self.system_info_frame)
        self.Platform.setObjectName(u"Platform")
        self.Platform.setFont(font7)

        self.gridLayout_7.addWidget(self.Platform, 2, 1, 1, 1)

        self.battery_2 = QLabel(self.system_info_frame)
        self.battery_2.setObjectName(u"battery_2")
        self.battery_2.setFont(font7)

        self.gridLayout_7.addWidget(self.battery_2, 4, 3, 1, 1)

        self.version = QLabel(self.system_info_frame)
        self.version.setObjectName(u"version")
        self.version.setFont(font7)

        self.gridLayout_7.addWidget(self.version, 3, 1, 1, 1)

        self.label_37 = QLabel(self.system_info_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.label_37, 2, 2, 1, 1)

        self.Processor = QLabel(self.system_info_frame)
        self.Processor.setObjectName(u"Processor")
        self.Processor.setFont(font7)
        self.Processor.setWordWrap(True)

        self.gridLayout_7.addWidget(self.Processor, 2, 3, 1, 1)

        self.system = QLabel(self.system_info_frame)
        self.system.setObjectName(u"system")
        self.system.setMinimumSize(QSize(300, 0))
        self.system.setFont(font6)
        self.system.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.gridLayout_7.addWidget(self.system, 1, 0, 1, 4, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.system_info_frame)

        self.stackedWidget.addWidget(self.systeminfo)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_5 = QVBoxLayout(self.activities)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"\n"
"border-width: 0px;\n"
"\n"
"    \n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(299999, 70))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.verticalLayout_7.addWidget(self.label_18)

        self.gpu_info = QLabel(self.frame_5)
        self.gpu_info.setObjectName(u"gpu_info")
        self.gpu_info.setMinimumSize(QSize(300, 0))
        self.gpu_info.setMaximumSize(QSize(16777215, 40))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.gpu_info.setFont(font9)
        self.gpu_info.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.verticalLayout_7.addWidget(self.gpu_info, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: #FF8787;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        font10 = QFont()
        font10.setPointSize(17)
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.widget_2 = roundProgressBar(self.frame_8)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)
        self.widget_2.setMinimumSize(QSize(250, 250))
        self.widget_2.setMaximumSize(QSize(50000, 50000))
        self.widget_2.setSizeIncrement(QSize(0, -15538))
        self.widget_2.setBaseSize(QSize(5000, 5000))
        font11 = QFont()
        font11.setFamily(u"MS Shell Dlg 2")
        font11.setPointSize(35)
        self.widget_2.setFont(font11)
        self.widget_2.setStyleSheet(u"\n"
"border-width: 1px;\n"
"\n"
"    \n"
"")

        self.gridLayout_6.addWidget(self.widget_2, 1, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: #F3E99F;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.verticalLayout_10.addWidget(self.label_16)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.freemem = QLabel(self.frame_11)
        self.freemem.setObjectName(u"freemem")
        self.freemem.setFont(font5)
        self.freemem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.gridLayout_2.addWidget(self.freemem, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 25))
        self.label_10.setMaximumSize(QSize(16777215, 50))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.tolmem = QLabel(self.frame_11)
        self.tolmem.setObjectName(u"tolmem")
        self.tolmem.setFont(font5)
        self.tolmem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:0;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.gridLayout_2.addWidget(self.tolmem, 1, 1, 1, 1)

        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.widget_3 = roundProgressBar(self.frame_11)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"\n"
"border-width: 1px;\n"
"\n"
"    \n"
"")

        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 2, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_11)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.gridLayout_8 = QGridLayout(self.storage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_6 = QLabel(self.storage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 50))
        self.label_6.setMaximumSize(QSize(11111111, 100))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color:;\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 2)

        self.frame_13 = QFrame(self.storage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border-width: 0;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tableWidget = QTableWidget(self.frame_13)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy8)
        self.tableWidget.setMinimumSize(QSize(634, 200))
        self.tableWidget.setStyleSheet(u"background-color:#F3E99F;\n"
"\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.horizontalLayout_12.addWidget(self.tableWidget, 0, Qt.AlignTop)


        self.gridLayout_8.addWidget(self.frame_13, 3, 0, 1, 1)

        self.frame_14 = QFrame(self.storage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border-width: 0;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)
        self.label_8.setMinimumSize(QSize(201, 0))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 12px;\n"
"border-color: rgb(0,0,0);\n"
"font: bold 20px;\n"
"    \n"
"    \n"
"")

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.storagechart = roundProgressBar(self.frame_14)
        self.storagechart.setObjectName(u"storagechart")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(2)
        sizePolicy9.setHeightForWidth(self.storagechart.sizePolicy().hasHeightForWidth())
        self.storagechart.setSizePolicy(sizePolicy9)
        self.storagechart.setMaximumSize(QSize(500, 590))

        self.verticalLayout_11.addWidget(self.storagechart, 0, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.frame_14, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.gridLayout_9 = QGridLayout(self.sensors)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableWidget_2 = QTableWidget(self.sensors)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMaximumSize(QSize(700, 16777215))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:1;\n"
"border-radius:5;\n"
"border-color: #00000;\n"
"    \n"
"")

        self.gridLayout_9.addWidget(self.tableWidget_2, 4, 0, 1, 1)

        self.label_11 = QLabel(self.sensors)
        self.label_11.setObjectName(u"label_11")
        font12 = QFont()
        font12.setPointSize(30)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_11.setFont(font12)
        self.label_11.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color:;\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")

        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)

        self.networktable = QTableWidget(self.sensors)
        if (self.networktable.columnCount() < 5):
            self.networktable.setColumnCount(5)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.networktable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.networktable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.networktable.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.networktable.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.networktable.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        self.networktable.setObjectName(u"networktable")
        self.networktable.setMaximumSize(QSize(700, 16777215))
        self.networktable.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:1;\n"
"border-radius:5;\n"
"border-color: rgb(0,0,0);\n"
"    \n"
"")

        self.gridLayout_9.addWidget(self.networktable, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.sensors)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.Center_main_frame)

        self.Right_main_frame = QFrame(self.Main_frame)
        self.Right_main_frame.setObjectName(u"Right_main_frame")
        sizePolicy2.setHeightForWidth(self.Right_main_frame.sizePolicy().hasHeightForWidth())
        self.Right_main_frame.setSizePolicy(sizePolicy2)
        self.Right_main_frame.setMinimumSize(QSize(300, 0))
        self.Right_main_frame.setMaximumSize(QSize(1, 16777215))
        self.Right_main_frame.setStyleSheet(u"background-color:;")
        self.Right_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Right_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Right_main_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.Right_main_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_18 = QFrame(self.frame_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.frame_18)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font13 = QFont()
        font13.setPointSize(26)
        font13.setBold(True)
        font13.setWeight(75)
        self.label.setFont(font13)
        self.label.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color:;\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")
        self.label.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label)

        self.label_21 = QLabel(self.frame_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 60))
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color:;\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")
        self.label_21.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_21)

        self.label_27 = QLabel(self.frame_18)
        self.label_27.setObjectName(u"label_27")
        font14 = QFont()
        font14.setPointSize(13)
        font14.setBold(False)
        font14.setWeight(50)
        self.label_27.setFont(font14)
        self.label_27.setStyleSheet(u"\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 12px;\n"
"border-color:;\n"
"    \n"
"\n"
"\n"
"color:#000000;\n"
"")
        self.label_27.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_27)


        self.verticalLayout_9.addWidget(self.frame_18)


        self.verticalLayout_16.addWidget(self.frame_7)


        self.horizontalLayout_8.addWidget(self.Right_main_frame)


        self.verticalLayout.addWidget(self.Main_frame)

        self.Footer_frame = QFrame(self.centralwidget)
        self.Footer_frame.setObjectName(u"Footer_frame")
        self.Footer_frame.setMaximumSize(QSize(16777215, 16777213))
        self.Footer_frame.setStyleSheet(u"\n"
"border-style: solid;\n"
"border-width:2px;\n"
"\n"
"\n"
"")
        self.Footer_frame.setFrameShape(QFrame.StyledPanel)
        self.Footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Footer_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.Footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setStyleSheet(u"\n"
"border-color: rgb(255,255,255);\n"
"\n"
"    \n"
"")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.footer_left_frame)
        self.label_2.setObjectName(u"label_2")
        font15 = QFont()
        font15.setPointSize(10)
        self.label_2.setFont(font15)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.Footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setStyleSheet(u"\n"
"border-color: rgb(255,255,255);\n"
"\n"
"    \n"
"")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon10 = QIcon()
        icon10.addFile(u":/image/icons8-questions-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer_right_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip)


        self.horizontalLayout_6.addWidget(self.footer_right_frame)


        self.verticalLayout.addWidget(self.Footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Minimize_window_button.setText("")
        self.resize_window_button.setText("")
        self.Close_window_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User Id", None))
        self.Userid.setText("")
        self.open_menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.Name_app.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">WATCH TOWER</span></p></body></html>", None))
        self.systeminformation_button_page.setText("")
        self.systeminfo_label.setText(QCoreApplication.translate("MainWindow", u"SYSTEM INFORMATION", None))
        self.network_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK", None))
        self.storage_button_page.setText("")
        self.network_button_page.setText("")
        self.storage_label.setText(QCoreApplication.translate("MainWindow", u"STORAGE", None))
        self.battery_label.setText(QCoreApplication.translate("MainWindow", u"BATTERY", None))
        self.cpu_button_page.setText("")
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u" CPU", None))
        self.battery_button_page.setText("")
        self.activity_button_page.setText("")
        self.activity_label.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">CPU_Performance</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CPU Main Core</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CPU Count</span></p></body></html>", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Clock Speed</span></p></body></html>", None))
        self.clockspeed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">N/A</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total Ram</span></p></body></html>", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Available Ram</span></p></body></html>", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_used.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Used Ram</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Battery Information</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Status</p></body></html>", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Charge</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Time Left</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Plugged in</span></p></body></html>", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_timeleft.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Battery</span></p></body></html>", None))
        self.bitness.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">System Date</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Machine</p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">System Information</span></p></body></html>", None))
        self.machine11.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.sysdate.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Bitness</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Platform</p></body></html>", None))
        self.systime.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Version</p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">System Time</p></body></html>", None))
        self.Platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Processor</p></body></html>", None))
        self.Processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">N/A</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">GPU Information</span></p></body></html>", None))
        self.gpu_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Memory used</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Temperature</span></p></body></html>", None))
        self.freemem.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Total memory</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Total memory</span></p></body></html>", None))
        self.tolmem.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">TextLabel</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Free memory</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">STORAGE</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Used", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Free", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Used %", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">USAGE</span></p></body></html>", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MAC", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Net Type", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"RX", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TX", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">NETWORK</span></p></body></html>", None))
        ___qtablewidgetitem13 = self.networktable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Iface", None));
        ___qtablewidgetitem14 = self.networktable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Download", None));
        ___qtablewidgetitem15 = self.networktable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Upload", None));
        ___qtablewidgetitem16 = self.networktable.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Download Speed", None));
        ___qtablewidgetitem17 = self.networktable.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Upload Speed", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Watch Tower", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"This app is created by Watch Tower group in CS340 - UTK - Spring 2023", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>User can look at their machine information: CPU, Ram, Information, Disk, Network, Battery. These information are fetched from hosted database.</p><p><br/></p><p>Please let us know if u have any question.</p><p>Email:watchtower@gmail.com</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright of CS340 group team", None))
        self.pushButton_2.setText("")
    # retranslateUi

