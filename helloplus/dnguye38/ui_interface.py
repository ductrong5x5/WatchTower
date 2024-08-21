# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceGcFxZM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1053, 792)
        MainWindow.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border:none	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header_frame = QFrame(self.centralwidget)
        self.Header_frame.setObjectName(u"Header_frame")
        self.Header_frame.setStyleSheet(u"")
        self.Header_frame.setFrameShape(QFrame.StyledPanel)
        self.Header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/image/icons8-menu-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.Header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/image/icons8-ecg-64.png"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.Name_app = QLabel(self.frame_2)
        self.Name_app.setObjectName(u"Name_app")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.Name_app.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Name_app)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.Header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Minimize_window_button = QPushButton(self.frame)
        self.Minimize_window_button.setObjectName(u"Minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/image/icons8-minimize-window-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.Minimize_window_button)

        self.resize_window_button = QPushButton(self.frame)
        self.resize_window_button.setObjectName(u"resize_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/image/icons8-restore-down-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_window_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.resize_window_button)

        self.Close_window_button = QPushButton(self.frame)
        self.Close_window_button.setObjectName(u"Close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/image/icons8-close-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close_window_button.setIcon(icon3)
        self.Close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.Close_window_button)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Header_frame)

        self.Main_frame = QFrame(self.centralwidget)
        self.Main_frame.setObjectName(u"Main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_frame.sizePolicy().hasHeightForWidth())
        self.Main_frame.setSizePolicy(sizePolicy)
        self.Main_frame.setStyleSheet(u"")
        self.Main_frame.setFrameShape(QFrame.StyledPanel)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Main_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Left_main_frame = QFrame(self.Main_frame)
        self.Left_main_frame.setObjectName(u"Left_main_frame")
        self.Left_main_frame.setMinimumSize(QSize(40, 0))
        self.Left_main_frame.setMaximumSize(QSize(20, 16777215))
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cpu_button_page = QPushButton(self.Menu_frame)
        self.cpu_button_page.setObjectName(u"cpu_button_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cpu_button_page.sizePolicy().hasHeightForWidth())
        self.cpu_button_page.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/image/icons8-microchip-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_button_page.setIcon(icon4)
        self.cpu_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.cpu_button_page, 0, 0, 1, 1, Qt.AlignLeft)

        self.battery_label = QLabel(self.Menu_frame)
        self.battery_label.setObjectName(u"battery_label")
        font2 = QFont()
        font2.setPointSize(12)
        self.battery_label.setFont(font2)
        self.battery_label.setMargin(5)

        self.gridLayout.addWidget(self.battery_label, 1, 1, 1, 1, Qt.AlignLeft)

        self.systeminfo_label = QLabel(self.Menu_frame)
        self.systeminfo_label.setObjectName(u"systeminfo_label")
        self.systeminfo_label.setFont(font2)
        self.systeminfo_label.setMargin(5)

        self.gridLayout.addWidget(self.systeminfo_label, 2, 1, 1, 1, Qt.AlignLeft)

        self.cpu_label = QLabel(self.Menu_frame)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setMinimumSize(QSize(280, 0))
        self.cpu_label.setFont(font2)

        self.gridLayout.addWidget(self.cpu_label, 0, 1, 1, 1)

        self.activity_button_page = QPushButton(self.Menu_frame)
        self.activity_button_page.setObjectName(u"activity_button_page")
        sizePolicy1.setHeightForWidth(self.activity_button_page.sizePolicy().hasHeightForWidth())
        self.activity_button_page.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u":/image/icons8-online-activity-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_button_page.setIcon(icon5)
        self.activity_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.activity_button_page, 3, 0, 1, 1, Qt.AlignLeft)

        self.storage_button_page = QPushButton(self.Menu_frame)
        self.storage_button_page.setObjectName(u"storage_button_page")
        sizePolicy1.setHeightForWidth(self.storage_button_page.sizePolicy().hasHeightForWidth())
        self.storage_button_page.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/image/icons8-stack-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_button_page.setIcon(icon6)
        self.storage_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.storage_button_page, 4, 0, 1, 1, Qt.AlignLeft)

        self.storage_label = QLabel(self.Menu_frame)
        self.storage_label.setObjectName(u"storage_label")
        self.storage_label.setFont(font2)
        self.storage_label.setMargin(5)

        self.gridLayout.addWidget(self.storage_label, 4, 1, 1, 1, Qt.AlignLeft)

        self.systeminformation_button_page = QPushButton(self.Menu_frame)
        self.systeminformation_button_page.setObjectName(u"systeminformation_button_page")
        sizePolicy1.setHeightForWidth(self.systeminformation_button_page.sizePolicy().hasHeightForWidth())
        self.systeminformation_button_page.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u":/image/icons8-system-information-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.systeminformation_button_page.setIcon(icon7)
        self.systeminformation_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.systeminformation_button_page, 2, 0, 1, 1, Qt.AlignLeft)

        self.activity_label = QLabel(self.Menu_frame)
        self.activity_label.setObjectName(u"activity_label")
        self.activity_label.setFont(font2)
        self.activity_label.setMargin(5)

        self.gridLayout.addWidget(self.activity_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.battery_button_page = QPushButton(self.Menu_frame)
        self.battery_button_page.setObjectName(u"battery_button_page")
        sizePolicy1.setHeightForWidth(self.battery_button_page.sizePolicy().hasHeightForWidth())
        self.battery_button_page.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u":/image/icons8-full-battery-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_button_page.setIcon(icon8)
        self.battery_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.battery_button_page, 1, 0, 1, 1, Qt.AlignLeft)

        self.sensor_button_page = QPushButton(self.Menu_frame)
        self.sensor_button_page.setObjectName(u"sensor_button_page")
        sizePolicy1.setHeightForWidth(self.sensor_button_page.sizePolicy().hasHeightForWidth())
        self.sensor_button_page.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u":/image/icons8-proximity-sensor-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sensor_button_page.setIcon(icon9)
        self.sensor_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.sensor_button_page, 5, 0, 1, 1, Qt.AlignLeft)

        self.sensor_label = QLabel(self.Menu_frame)
        self.sensor_label.setObjectName(u"sensor_label")
        self.sensor_label.setFont(font2)
        self.sensor_label.setMargin(5)

        self.gridLayout.addWidget(self.sensor_label, 5, 1, 1, 1, Qt.AlignLeft)

        self.network_label = QLabel(self.Menu_frame)
        self.network_label.setObjectName(u"network_label")
        self.network_label.setFont(font2)
        self.network_label.setMargin(5)

        self.gridLayout.addWidget(self.network_label, 6, 1, 1, 1, Qt.AlignLeft)

        self.network_button_page = QPushButton(self.Menu_frame)
        self.network_button_page.setObjectName(u"network_button_page")
        sizePolicy1.setHeightForWidth(self.network_button_page.sizePolicy().hasHeightForWidth())
        self.network_button_page.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u":/image/icons8-wi-fi-connected-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button_page.setIcon(icon10)
        self.network_button_page.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.network_button_page, 6, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.Menu_frame, 0, Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.Left_main_frame)

        self.Center_main_frame = QFrame(self.Main_frame)
        self.Center_main_frame.setObjectName(u"Center_main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Center_main_frame.sizePolicy().hasHeightForWidth())
        self.Center_main_frame.setSizePolicy(sizePolicy2)
        self.Center_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Center_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Center_main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.Center_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.cpu_info_frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgb(63, 63, 63);")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.cpu_info_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.cpu_info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.cpu_info_frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_7 = QLabel(self.cpu_info_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.cpu_info_frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.ram_info_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_16 = QLabel(self.ram_info_frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_14 = QLabel(self.ram_info_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_17 = QLabel(self.ram_info_frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_13 = QLabel(self.ram_info_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_18 = QLabel(self.ram_info_frame)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 2, 1, 1, 1)

        self.label_15 = QLabel(self.ram_info_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_19 = QLabel(self.ram_info_frame)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 3, 1, 1, 1)

        self.label_12 = QLabel(self.ram_info_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_20 = QLabel(self.ram_info_frame)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.gridLayout_6 = QGridLayout(self.battery)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_21 = QLabel(self.battery)
        self.label_21.setObjectName(u"label_21")
        font4 = QFont()
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_21.setFont(font4)

        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)

        self.batery_frame = QFrame(self.battery)
        self.batery_frame.setObjectName(u"batery_frame")
        self.batery_frame.setFrameShape(QFrame.StyledPanel)
        self.batery_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.batery_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_26 = QLabel(self.batery_frame)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_25 = QLabel(self.batery_frame)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_29 = QLabel(self.batery_frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 3, 1, 1, 1)

        self.label_27 = QLabel(self.batery_frame)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 1, 1, 1, 1)

        self.label_24 = QLabel(self.batery_frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 2, 0, 1, 1)

        self.label_22 = QLabel(self.batery_frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.batery_frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_28 = QLabel(self.batery_frame)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.batery_frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.battery)
        self.systeminfo = QWidget()
        self.systeminfo.setObjectName(u"systeminfo")
        self.verticalLayout_4 = QVBoxLayout(self.systeminfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.system_info_frame = QFrame(self.systeminfo)
        self.system_info_frame.setObjectName(u"system_info_frame")
        self.system_info_frame.setFrameShape(QFrame.StyledPanel)
        self.system_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.system_info_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self.system_info_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 1, Qt.AlignBottom)

        self.label_36 = QLabel(self.system_info_frame)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_7.addWidget(self.label_36, 2, 1, 1, 1)

        self.label_31 = QLabel(self.system_info_frame)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 1, 0, 1, 1, Qt.AlignTop)

        self.label_37 = QLabel(self.system_info_frame)
        self.label_37.setObjectName(u"label_37")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_37.setFont(font5)

        self.gridLayout_7.addWidget(self.label_37, 2, 2, 1, 1)

        self.label_35 = QLabel(self.system_info_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)

        self.gridLayout_7.addWidget(self.label_35, 4, 0, 1, 1)

        self.label_33 = QLabel(self.system_info_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)

        self.gridLayout_7.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_34 = QLabel(self.system_info_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)

        self.gridLayout_7.addWidget(self.label_34, 3, 0, 1, 1)

        self.label_38 = QLabel(self.system_info_frame)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 2, 3, 1, 1)

        self.label_39 = QLabel(self.system_info_frame)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_7.addWidget(self.label_39, 3, 1, 1, 1)

        self.label_40 = QLabel(self.system_info_frame)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_7.addWidget(self.label_40, 4, 1, 1, 1)

        self.label_41 = QLabel(self.system_info_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.gridLayout_7.addWidget(self.label_41, 3, 2, 1, 1)

        self.label_42 = QLabel(self.system_info_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font5)

        self.gridLayout_7.addWidget(self.label_42, 4, 2, 1, 1)

        self.label_43 = QLabel(self.system_info_frame)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_7.addWidget(self.label_43, 3, 3, 1, 1)

        self.label_44 = QLabel(self.system_info_frame)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_7.addWidget(self.label_44, 4, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.system_info_frame)

        self.stackedWidget.addWidget(self.systeminfo)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_5 = QVBoxLayout(self.activities)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_32.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_32)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        icon11 = QIcon()
        icon11.addFile(u":/image/icons8-search-more-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.verticalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setPointSize(15)
        self.lineEdit.setFont(font7)
        self.lineEdit.setStyleSheet(u"background-color: rgb(144, 144, 144);")

        self.verticalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.activities)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(163, 163, 163);")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.activities)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_10.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_10.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_10.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_10.addWidget(self.pushButton_7)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_8 = QVBoxLayout(self.storage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_45 = QLabel(self.storage)
        self.label_45.setObjectName(u"label_45")
        sizePolicy2.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy2)
        self.label_45.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_45)

        self.tableWidget_2 = QTableWidget(self.storage)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(173, 173, 173);")

        self.verticalLayout_8.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_9 = QVBoxLayout(self.sensors)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_46 = QLabel(self.sensors)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_46)

        self.tableWidget_3 = QTableWidget(self.sensors)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setKerning(False)
        self.tableWidget_3.setFont(font8)
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")

        self.verticalLayout_9.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.sensors)
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.verticalLayout_10 = QVBoxLayout(self.network)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.network)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 239, 953))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font6)

        self.verticalLayout_11.addWidget(self.label_48)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(199, 199, 199);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_47 = QLabel(self.frame_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_47)

        self.tableWidget_4 = QTableWidget(self.frame_8)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font7);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_12.addWidget(self.tableWidget_4)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_49 = QLabel(self.frame_9)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_49)

        self.tableWidget_5 = QTableWidget(self.frame_9)
        if (self.tableWidget_5.columnCount() < 9):
            self.tableWidget_5.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.verticalLayout_13.addWidget(self.tableWidget_5)


        self.verticalLayout_11.addWidget(self.frame_9, 0, Qt.AlignBottom)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 200))
        self.frame_10.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_50 = QLabel(self.frame_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_50)

        self.tableWidget_6 = QTableWidget(self.frame_10)
        if (self.tableWidget_6.columnCount() < 6):
            self.tableWidget_6.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        sizePolicy5.setHeightForWidth(self.tableWidget_6.sizePolicy().hasHeightForWidth())
        self.tableWidget_6.setSizePolicy(sizePolicy5)
        self.tableWidget_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_14.addWidget(self.tableWidget_6)


        self.verticalLayout_11.addWidget(self.frame_10, 0, Qt.AlignBottom)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(193, 193, 193);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_51 = QLabel(self.frame_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_51)

        self.tableWidget_7 = QTableWidget(self.frame_11)
        if (self.tableWidget_7.columnCount() < 8):
            self.tableWidget_7.setColumnCount(8)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, __qtablewidgetitem50)
        self.tableWidget_7.setObjectName(u"tableWidget_7")

        self.verticalLayout_15.addWidget(self.tableWidget_7)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.network)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.Center_main_frame)

        self.Right_main_frame = QFrame(self.Main_frame)
        self.Right_main_frame.setObjectName(u"Right_main_frame")
        sizePolicy2.setHeightForWidth(self.Right_main_frame.sizePolicy().hasHeightForWidth())
        self.Right_main_frame.setSizePolicy(sizePolicy2)
        self.Right_main_frame.setMinimumSize(QSize(200, 0))
        self.Right_main_frame.setMaximumSize(QSize(100, 16777215))
        self.Right_main_frame.setStyleSheet(u"background-color: rgb(32, 244, 255);")
        self.Right_main_frame.setFrameShape(QFrame.StyledPanel)
        self.Right_main_frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.Right_main_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 40, 131, 361))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setMinimumSize(QSize(100, 50))
        self.label_10.setMaximumSize(QSize(60, 30))
        font9 = QFont()
        font9.setPointSize(25)
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(8, 8, 8);")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.Right_main_frame)


        self.verticalLayout.addWidget(self.Main_frame)

        self.Footer_frame = QFrame(self.centralwidget)
        self.Footer_frame.setObjectName(u"Footer_frame")
        self.Footer_frame.setFrameShape(QFrame.StyledPanel)
        self.Footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Footer_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.Footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.footer_left_frame)
        self.label_2.setObjectName(u"label_2")
        font10 = QFont()
        font10.setPointSize(10)
        self.label_2.setFont(font10)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.Footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon12 = QIcon()
        icon12.addFile(u":/image/icons8-questions-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon12)
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
        self.menubar.setGeometry(QRect(0, 0, 1053, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.Name_app.setText(QCoreApplication.translate("MainWindow", u"WATCH TOWER", None))
        self.Minimize_window_button.setText("")
        self.resize_window_button.setText("")
        self.Close_window_button.setText("")
        self.cpu_button_page.setText("")
        self.battery_label.setText(QCoreApplication.translate("MainWindow", u"BATTERY", None))
        self.systeminfo_label.setText(QCoreApplication.translate("MainWindow", u"SYSTEM INFORMATION", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u" CPU", None))
        self.activity_button_page.setText("")
        self.storage_button_page.setText("")
        self.storage_label.setText(QCoreApplication.translate("MainWindow", u"STORAGE", None))
        self.systeminformation_button_page.setText("")
        self.activity_label.setText(QCoreApplication.translate("MainWindow", u"ACTIVITY", None))
        self.battery_button_page.setText("")
        self.sensor_button_page.setText("")
        self.sensor_label.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        self.network_label.setText(QCoreApplication.translate("MainWindow", u"NETWORK", None))
        self.network_button_page.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPU_Per", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Used Ram", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Free Ram", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Plugged in", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.pushButton_3.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Disk Storage", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Mount point", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u" MAX FILE", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MAX PATH", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Total storage", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free storage", None));
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"SENSORS", None))
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"NETWORK", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Network IO counters", None))
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"BYTES SENT", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"PACKETS SENT", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"PACKETS RECEIVED", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"ERR IN", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR OUT", None));
        ___qtablewidgetitem31 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"DROP IN", None));
        ___qtablewidgetitem32 = self.tableWidget_5.horizontalHeaderItem(8)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"DROP OUT", None));
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Network Adresses", None))
        ___qtablewidgetitem33 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"NET MASK", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"ROADCAS", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_51.setText(QCoreApplication.translate("MainWindow", u" Network Connections", None))
        ___qtablewidgetitem38 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem39 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem40 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem41 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem42 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem43 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem44 = self.tableWidget_7.horizontalHeaderItem(7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"App designed by Team", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright of CS340 group team", None))
        self.pushButton_2.setText("")
    # retranslateUi

