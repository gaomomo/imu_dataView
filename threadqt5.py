# coding:utf-8
from threespace import threespace_api as tsapi
from PyQt5 import QtWidgets
import pyqtgraph as pg
import sys
import time
import threading
data = []
i = 0
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setWindowTitle("TaredOrientationAsQuaternion")
        self.main_widget = QtWidgets.QWidget()  # 创建一个主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建一个网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置主部件的布局为网格
        self.setCentralWidget(self.main_widget)  # 设置窗口默认部件

        self.plot_widget = QtWidgets.QWidget()  # 实例化一个widget部件作为K线图部件
        self.plot_layout = QtWidgets.QGridLayout()  # 实例化一个网格布局层
        self.plot_widget.setLayout(self.plot_layout)  # 设置线图部件的布局层
        self.plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.plt.showGrid(x=True, y=True)  # 显示图形网格
        self.plot_layout.addWidget(self.plt)  # 添加绘图部件到线图部件的网格布局层
        # 将上述部件添加到布局层中
        self.main_layout.addWidget(self.plot_widget, 1, 0, 3, 3)
        self.setCentralWidget(self.main_widget)
        self.plt.setYRange(max=3, min=-2)
        # self.plot_plt.setXRange(max=50, min=0)
        self.y1, self.y2, self.y3, self.y4, self.x = [], [], [], [], []
        self.timer_start()
        # 启动定时器 时间间隔秒

    def timer_start(self):
        self.timer = pg.QtCore.QTimer(self)
        self.timer.timeout.connect(self.get_show)
        self.timer.start(0.1)

    def get_show(self):
        global i
        if len(data) > i:
            d = data.pop()# d = data[i]  #
        else:
            return
        if len(self.y1) < 30:
            self.y1.append(d[0])
            self.y2.append(d[1])
            self.y3.append(d[2])
            self.y4.append(d[3])
            self.x.append(i)
        else:
            self.x[:-1] = self.x[1:]
            self.x[-1] = i
            self.y1[:-1] = self.y1[1:]
            self.y1[-1] = d[0]
            self.y2[:-1] = self.y2[1:]
            self.y2[-1] = d[1]
            self.y3[:-1] = self.y3[1:]
            self.y3[-1] = d[2]
            self.y4[:-1] = self.y4[1:]
            self.y4[-1] = d[3]
        i += 1
        self.plt.plot().setData(x=self.x, y=self.y1, pen='g')
        self.plt.plot().setData(x=self.x, y=self.y2, pen='r')
        self.plt.plot().setData(x=self.x, y=self.y3, pen='b')
        self.plt.plot().setData(x=self.x, y=self.y4, pen='w')

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
def getData():
    imu = tsapi.TSDLSensor(com_port='COM3', baudrate=115200)
    imu.startStreaming()
    imu.setStreamingSlots(slot0='getTaredOrientationAsQuaternion', slot1='null',
                          slot2='null', slot3='null',
                          slot4='null', slot5='null', slot6='null', slot7='null')
    while True:
        data.append(imu.getStreamingBatch(timestamp=False))
        time.sleep(0.1)

if __name__ == '__main__':
    t1 = threading.Thread(target=getData)
    t1.start()
    t2 = threading.Thread(target=main)
    t2.start()

