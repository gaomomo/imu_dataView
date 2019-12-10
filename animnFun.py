#coding=UTF-8
import matplotlib.pyplot as plt
from threespace import threespace_api as tsapi
from matplotlib.animation import FuncAnimation
import numpy as np
import operator
from functools import reduce

data = []
lastData = 0
i = 0
tp = []
def update(frame):
    global i
    if (frame==1):
        data.append(imu.getStreamingBatch(timestamp=True))
        t = data[i][1]
        xdata.append(t)
        tp.append(i)
        d = list(data[i][0])
        to_1 = d[0:1]
        to_2 = d[1:2]
        to_3 = d[2:3]
        to_4 = d[3:4]
        ydata.append(to_1)
        y2data.append(to_1)
        y1 = reduce(operator.add, ydata)
        y2 = reduce(operator.add, y2data)
        ln.set_data(np.array(tp), np.array(y1))
        # ln.set_data(np.array(tp), np.array(y2))
        i = i+1
        return ln,

def init():
    ax.set_xlim(0, 1000)
    ax.set_ylim(-2, 3)
    return ln,
def gen_fun():
    while True:
        yield 1
def showData():
    anim = FuncAnimation(fig, update, frames=gen_fun, init_func=init, interval=5, blit=True)
    plt.show()

if __name__=='__main__':
    fig, ax = plt.subplots()
    xdata, ydata ,y2data = [], [], []
    ln, = ax.plot([], [], 'r-', animated=False)

    imu = tsapi.TSDLSensor(com_port='COM3', baudrate=115200)
    imu.startStreaming()
    imu.setStreamingSlots(slot0='getTaredOrientationAsQuaternion', slot1='getCorrectedGyroRate',
                          slot2='getCorrectedAccelerometerVector', slot3='getRawGyroscopeRate',
                          slot4='getRawAccelerometerData', slot5='null', slot6='null', slot7='null')
    showData();
