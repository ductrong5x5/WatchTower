import sys
import os
from PySide2 import *

from qt_material import* 
from ui_interface import *

class MainWindow (QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            #apply_stylesheet(app, theme='dark_cyan.xml')
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(50)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,92,157,550))

            self.ui.centralwidget.setGraphicsEffect(self.shadow)

            self.setWindowIcon(QtGui.QIcon(":/image/icons8-ecg-64.png"))
            self.setWindowTitle("Monitoring Aplication")
            QSizeGrip(self.ui.size_grip)

            self.ui.Minimize_window_button.clicked.connect(lambda:self.showMinimized())
            self.ui.Close_window_button.clicked.connect(lambda:self.close())
            self.ui.resize_window_button.clicked.connect(lambda:self.restore_or_maximize_window())

            self.ui.cpu_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
            self.ui.battery_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
            self.ui.systeminformation_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.systeminfo))
            self.ui.activity_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
            self.ui.storage_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
            self.ui.sensor_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
            self.ui.network_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.battery))


            self.show()

        def restore_or_maximize_window(self):
            if self.isMaximized():
                self.showNormal()
                self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/image/icons8-restore-down-16.png"))
            else:
                self.showMaximized()
                self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/image/icons8-restore-down-16.png"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())