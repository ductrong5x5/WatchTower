import sys
import os
import time
from PySide2 import *
import pandas as pd

from qt_material import* 
from ui_interface import *
from multiprocessing import cpu_count
from time import sleep
import platform
import pynvml
from psutil._common import bytes2human
import psutil
import PySide2extn
import datetime
import shutil
import pyopencl as cl
import wmi
from time import sleep

import winreg
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
value = winreg.QueryValueEx(key, "MachineGuid")
import mysql.connector


class WorketSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int) 
class Worker(object):
    """docstring for worker"""
    def __init__(self, fn, *args, **kwargs):
        super(Worker,self).__init__()

        self.fn=fn
        self.args=args
        self.kwargs=kwargs
        self.signals = WorketSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result=self.fn(*self.args,**self.kwargs)
        except:
            traceback.print_exc()
            exctype, value =sys.exc_info()[:2]
            self.signals.error.emit((exctype.value,traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()
class WorkerRunnable(QRunnable):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    def run(self):
        self.worker.run()
def get_size(bytes):

    #Returns size of bytes in a nice format

    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


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
        self.ui.network_button_page.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.Header_frame.mouseMoveEvent = moveWindow

        self.ui.open_menu_button.clicked.connect(lambda: self.slideLeftMenu())

        self.ui.pushButton_2.clicked.connect(lambda: self.helpmenu())

        self.threadpool=QThreadPool()
        self.ui.Userid.setText(value[0])
        self.psutil_thread()

        
        


    def psutil_thread(self):
        worker =Worker(self.cpu_ram)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        runnable = WorkerRunnable(worker)
        self.threadpool.start(runnable)

        battery_check = psutil.sensors_battery()
        is_laptop =  battery_check is not None
        if is_laptop:
            battery_worker=Worker(self.battery)
            battery_worker.signals.result.connect(self.print_output)
            battery_worker.signals.finished.connect(self.thread_complete)
            battery_worker.signals.progress.connect(self.progress_fn)
            runnable2 = WorkerRunnable(battery_worker)
            self.threadpool.start(runnable2)
        else:
            self.ui.battery_status.setText("There is no battery")
            self.ui.battery_plugged.setText("Is Plugged")
            self.ui.battery_chart.rpb_setValue(100)
            self.ui.battery_chart.rpb_setLineColor((255, 109, 96))
            self.ui.battery_chart.rpb_setPieColor((255, 109, 96))
            self.ui.battery_chart.rpb_setTextColor((0,0,0))
        
        worker3 =Worker(self.systemin)

        worker3.signals.result.connect(self.print_output)
        worker3.signals.finished.connect(self.thread_complete)
        worker3.signals.progress.connect(self.progress_fn)
        runnable3 = WorkerRunnable(worker3)
        self.threadpool.start(runnable3)

        gpu_worker = Worker(self.gpu)
        gpu_worker.signals.result.connect(self.print_output)
        gpu_worker.signals.finished.connect(self.thread_complete)
        gpu_worker.signals.progress.connect(self.progress_fn)
        runnable4 = WorkerRunnable(gpu_worker)
        self.threadpool.start(runnable4)

        net_worker = Worker(self.network)
        net_worker.signals.result.connect(self.print_output)
        net_worker.signals.finished.connect(self.thread_complete)
        net_worker.signals.progress.connect(self.progress_fn)
        runnable5 = WorkerRunnable(net_worker)
        self.threadpool.start(runnable5)

        storeage_worker = Worker(self.storage)
        storeage_worker.signals.result.connect(self.print_output)
        storeage_worker.signals.finished.connect(self.thread_complete)
        storeage_worker.signals.progress.connect(self.progress_fn)
        runnable6 = WorkerRunnable(storeage_worker)
        self.threadpool.start(runnable6)
        
    def print_output(self,s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def progress_fn(self,n):
        print("%d%% done" % n)


    def secs2hours(self,secs):
        mm, ss = divmod(secs,60)
        hh, mm = divmod(mm,60)
        return "%d:%02d:%02d" % (hh,mm,ss)

    def systemin(self, progress_callback):

        

        while True:
            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',  
            )
            mycursor = mydb.cursor()
            # mycursor.execute("SELECT * FROM machines.machines;")
            # myresult = mycursor.fetchall()
            time=datetime.datetime.now().strftime("%I:%M:%S %p")
            self.ui.systime.setText(str(time))

            date=datetime.datetime.now().strftime("%Y-%m-%d")
            self.ui.sysdate.setText(str(date))
            # table="SELECT * FROM cpu.`"+value[0]+"` ORDER BY timestamp DESC LIMIT 1;"
            
            table="SELECT * FROM machines.machines";
            mycursor.execute(table)
            myresult = mycursor.fetchall()
            for x in myresult:
                if x[1] == value[0]:
                    # print()
                    self.ui.machine11.setText(x[2])
                    self.ui.version.setText(x[3])
                    self.ui.Platform.setText(x[4])
                    self.ui.system.setText(platform.system())
                    self.ui.Processor.setText(platform.processor())
                    if x[6] =="True":  
                        self.ui.battery_2.setText("YES")
                    else:
                        self.ui.battery_2.setText("NO")
                    self.ui.bitness.setText(x[5])

            sleep(1)



    def gpu(self, progress_callback):
        import platform
        while True:
            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',  
            )
            mycursor = mydb.cursor()
            table="SELECT * FROM machines.machines";
            mycursor.execute(table)
            myresult = mycursor.fetchall()
            for x in myresult:
                if x[1] == value[0]:
                    # print()
                    self.ui.gpu_info.setText(x[11])
                    if (platform.system() == "Windows"):
                        pynvml.nvmlInit()
                        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                        name = pynvml.nvmlDeviceGetName(handle)
                        temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
                        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                        memory_used = memory_info.used
                        memory_used = memory_used / (1024*1024)
                        self.ui.gpu_info.setText(name)
                        self.ui.widget_3.rpb_setMaximum(100)
                        self.ui.widget_3.rpb_setValue(temperature)
                        self.ui.widget_3.rpb_setBarStyle('Hybrid2')
                        self.ui.widget_3.rpb_setLineColor((255,30,99))
                        self.ui.widget_3.rpb_setPieColor((45,74,83))
                        self.ui.widget_3.rpb_setTextColor((0,0,0))
                        self.ui.widget_3.rpb_setInitialPos('North')
                        self.ui.widget_3.rpb_setTextFormat('Value' )
                        self.ui.widget_3.rpb_setLineWidth(15)
                        self.ui.widget_3.rpb_setPathWidth(15)
                        self.ui.widget_3.rpb_setLineCap('RoundCap')

                        self.ui.widget_2.rpb_setMaximum(memory_info.total)
                        self.ui.widget_2.rpb_setValue(memory_info.used)
                        self.ui.widget_2.rpb_setBarStyle('Hybrid2')
                        self.ui.widget_2.rpb_setLineColor((255,30,99))
                        self.ui.widget_2.rpb_setPieColor((45,74,83))
                        self.ui.widget_2.rpb_setTextColor((0,0,0))
                        self.ui.widget_2.rpb_setInitialPos('North')
                        self.ui.widget_2.rpb_setTextFormat('Percentage')
                        self.ui.widget_2.rpb_setLineWidth(15)
                        self.ui.widget_2.rpb_setPathWidth(15)
                        self.ui.widget_2.rpb_setLineCap('RoundCap')
                        self.ui.tolmem.setText(str("{:.2f}".format((memory_info.total )/1024/1024/1024)+' GB'))
                        self.ui.freemem.setText(str("{:.2f}".format((memory_info.total - memory_info.used )/1024/1024/1024)+' GB'))
            sleep(1)

    def battery(self, progress_callback):
        while True:
            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',
               
            )
            mycursor = mydb.cursor()
            table="SELECT * FROM battery.`"+value[0]+"`ORDER BY timestamp DESC LIMIT 1;"
            mycursor.execute(table)
            myresult = mycursor.fetchone()
             # = mycursor.fetchall()
            batt = psutil.sensors_battery()
            if not hasattr(psutil,"sensors_battery"):
                self.ui.battery_status.setText("Not supported")
            
            if batt is None:
                self.ui.battery_status.setText("No battery")

            if batt.power_plugged:
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
                self.ui.battery_timeleft.setText("No idea")
                if batt.percent <100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")

                self.ui.battery_plugged.setText("Is plugged")
            else:
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
                self.ui.battery_timeleft.setText(self.secs2hours(batt.secsleft))
                if batt.percent <100:
                    self.ui.battery_status.setText("Not Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")
                    self.ui.battery_plugged.setText("Not Plugged ")

            self.ui.battery_chart.rpb_setMaximum(100)
            if myresult[2] > 100:
                chartbatt=11
            else:
                chartbatt =myresult[2]
            self.ui.battery_chart.rpb_setValue(chartbatt)
            self.ui.battery_chart.rpb_setBarStyle('Hybrid2')
            self.ui.battery_chart.rpb_setLineColor((255, 109, 96))
            self.ui.battery_chart.rpb_setPieColor((255, 109, 96))
            self.ui.battery_chart.rpb_setTextColor((0,0,0))
            self.ui.battery_chart.rpb_setInitialPos('North')
            self.ui.battery_chart.rpb_setTextFormat('Percentage')
            self.ui.battery_chart.rpb_setLineWidth(15)
            self.ui.battery_chart.rpb_setPathWidth(15)
            self.ui.battery_chart.rpb_setLineCap('RoundCap')
            sleep(1)


    def cpu_ram(self, progress_callback):
        while True:
            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',
               
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM machines.machines;")
            myresult = mycursor.fetchall()

            # print the results
            for x in myresult:
                if x[1]== value[0]:    
                    totalRam = x[10]/ (1024*1024*1024)
           
            self.ui.total_ram.setText(str("{:.2f}".format(totalRam)+' GB'))
            table="SELECT * FROM ram.`"+value[0]+"`ORDER BY timestamp DESC LIMIT 1;"
            mycursor.execute(table)
            myresult = mycursor.fetchone()


            ramUsed = myresult[2]
            ramUsed = ramUsed /  (1024*1024*1024)
            self.ui.ram_used.setText(str("{:.1f}".format(ramUsed)+' GB'))


            availableRam = totalRam - ramUsed

            self.ui.available_ram.setText(str ("{:.1f}".format(availableRam) + ' GB'))
            self.ui.ram_chart.rpb_setMaximum(totalRam)
            self.ui.ram_chart.rpb_setValue(ramUsed)
            self.ui.ram_chart.rpb_setBarStyle('Hybrid2')
            self.ui.ram_chart.rpb_setLineColor((238,118,0))     
            self.ui.ram_chart.rpb_setTextColor((0,0,0)) 
            self.ui.ram_chart.rpb_setInitialPos('North')
            self.ui.ram_chart.rpb_setTextFormat('Percentage')
            self.ui.ram_chart.rpb_setTextFont('Arial')
            self.ui.ram_chart.rpb_setLineWidth(15)
            self.ui.ram_chart.rpb_setPathWidth(15)
            self.ui.ram_chart.rpb_setLineCap('RoundCap')

            table="SELECT * FROM cpu.`"+value[0]+"`ORDER BY timestamp DESC LIMIT 1;"
            mycursor.execute(table)
            myresult = mycursor.fetchone()
            cpuPer = myresult[2]
            self.ui.cpu_per.setText(str(cpuPer) + " %")

            self.ui.clockspeed.setText(str(myresult[3]))
            self.ui.cpu_chart.rpb_setMaximum(100)
            self.ui.cpu_chart.rpb_setValue(myresult[2])
            self.ui.cpu_chart.rpb_setBarStyle('Hybrid2')
            self.ui.cpu_chart.rpb_setLineColor((152, 216, 170))
            self.ui.cpu_chart.rpb_setTextColor((0,0,0))
            self.ui.cpu_chart.rpb_setInitialPos('North')
            self.ui.cpu_chart.rpb_setTextFormat('Percentage')
            self.ui.cpu_chart.rpb_setTextFont('Arial')
            self.ui.cpu_chart.rpb_setLineWidth(15)
            self.ui.cpu_chart.rpb_setPathWidth(15)
            self.ui.cpu_chart.rpb_setLineCap('RoundCap')

            table="SELECT * FROM machines.machines";
            mycursor.execute(table)
            myresult = mycursor.fetchall()
            for x in myresult:
                if x[1] == value[0]:
                    core=x[7]
                    self.ui.cpu_count.setText(str(core))

                    cpuMaincore = x[8]
                    self.ui.cpu_main_core.setText(str(cpuMaincore))


            



            
            sleep(0.5)
    def storage(self, progress_callback):
        while True:
            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',
               
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM machines.machines;")
            myresult = mycursor.fetchall()


            Total = 0
            Used = 0
            self.ui.tableWidget.setRowCount(0)
            for part in psutil.disk_partitions(all=False):
                rowPosition = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowPosition)
                if os.name == 'nt':
                    if 'cdrom' in part.opts or part.fstype == '':
                        # skip cd-rom drives with no disk in it; they may raise
                        # ENOENT, pop-up a Windows GUI error for a non-ready
                        # partition or just hang.
                        continue
                usage = psutil.disk_usage(part.mountpoint)
                self.create_table_widget(rowPosition,0,part.device,"tableWidget")
                self.create_table_widget(rowPosition,1,bytes2human(usage.total),"tableWidget")
                self.create_table_widget(rowPosition,2,bytes2human(usage.used),"tableWidget")
                self.create_table_widget(rowPosition,3,bytes2human(usage.free),"tableWidget")
                self.create_table_widget(rowPosition,4,str(usage.percent),"tableWidget")
                self.create_table_widget(rowPosition,5,part.fstype,"tableWidget")
                int_value_total = round(int(bytes2human(usage.total).replace('.', '').replace('G', ''))/10)
                int_value_used  = round(int(bytes2human(usage.used).replace('.', '').replace('G', ''))/10)
                Total += int_value_total
                Used += int_value_used

            self.ui.storagechart.rpb_setMaximum(Total)
            self.ui.storagechart.rpb_setValue(Used)
            self.ui.storagechart.rpb_setBarStyle('Hybrid2')
            self.ui.storagechart.rpb_setLineColor((238,118,0))     
            self.ui.storagechart.rpb_setTextColor((0,0,0)) 
            self.ui.storagechart.rpb_setInitialPos('North')
            self.ui.storagechart.rpb_setTextFormat('Percentage')
            self.ui.storagechart.rpb_setTextFont('Arial')
            self.ui.storagechart.rpb_setLineWidth(15)
            self.ui.storagechart.rpb_setPathWidth(15)
            self.ui.storagechart.rpb_setLineCap('RoundCap')
            sleep(1)

   
    def network(self, progress_callback):
        io = psutil.net_io_counters(pernic=True)
        row2=0
        while True:

            data=[]
            io_2 = psutil.net_io_counters(pernic=True)
            self.ui.networktable.setRowCount(0)
            for iface, iface_io in io.items():

                rowPosition = self.ui.networktable.rowCount()
                self.ui.networktable.insertRow(rowPosition)

                upload_speed, download_speed = io_2[iface].bytes_sent - iface_io.bytes_sent, io_2[iface].bytes_recv - iface_io.bytes_recv
                data.append({
                    "iface": iface, 
                    "Download": get_size(io_2[iface].bytes_recv),
                    "Upload": get_size(io_2[iface].bytes_sent),
                    "Upload Speed": f"{get_size(upload_speed / 1)}/s",
                    "Download Speed": f"{get_size(download_speed / 1)}/s",
                })
                
                self.create_table_widget(rowPosition,0,iface,"networktable")
                self.create_table_widget(rowPosition,1,get_size(io_2[iface].bytes_recv),"networktable")
                self.create_table_widget(rowPosition,2,get_size(io_2[iface].bytes_sent),"networktable")
                self.create_table_widget(rowPosition,3,f"{get_size(upload_speed / 1)}/s","networktable")
                self.create_table_widget(rowPosition,4,f"{get_size(download_speed / 1)}/s","networktable")

            # update the I/O stats for the next iteration
            io = io_2

            mydb = mysql.connector.connect(
                host='104.238.215.106',
                user='root',
                password='Huffmand3coding',
               
            )
            mycursor = mydb.cursor()
            table ="SELECT * FROM net.`"+value[0]+"` WHERE `"+value[0]+"` .timestamp = (SELECT max(timestamp) from net.`"+value[0]+"` ) order by description"
            mycursor.execute(table)
            myresult = mycursor.fetchall()
            rowPosition1 = mycursor.rowcount

            row=0
            self.ui.tableWidget_2.setRowCount(rowPosition1)
            for thing in myresult:
                self.ui.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(thing[1]))
                self.ui.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(thing[2]))
                self.ui.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(thing[3]))
                self.ui.tableWidget_2.setItem(row,3,QtWidgets.QTableWidgetItem(thing[4]))
                self.ui.tableWidget_2.setItem(row,4,QtWidgets.QTableWidgetItem(thing[5]))
                num6= round(thing[6]/1024/1024,1)
                self.ui.tableWidget_2.setItem(row,5,QtWidgets.QTableWidgetItem(str(num6)+' MB'))
                num7= round(thing[7]/1024/1024,1)
                self.ui.tableWidget_2.setItem(row,6,QtWidgets.QTableWidgetItem(str(num7)+' MB'))
                row=row+1

            
            sleep(1)

    def create_table_widget(self,rowPosition,columnPosition,text,tableName):
        table=QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition,columnPosition,table)
        table=getattr(self.ui, tableName).item(rowPosition,columnPosition)
        table.setText(text);

    def slideLeftMenu(self):
        width = self.ui.Left_main_frame.width()
        if width==50:
            newWidth = 300
        else:
            newWidth = 50
        self.animation = QPropertyAnimation(self.ui.Left_main_frame,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def helpmenu(self):
        width = self.ui.Right_main_frame.width()
        if width==1:
            newWidth = 300
        else:
            newWidth = 1
        self.animation = QPropertyAnimation(self.ui.Right_main_frame,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def mousePressEvent(self,event):
        self.clickPosition=event.globalPos()


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
    window.show()
    sys.exit(app.exec_())