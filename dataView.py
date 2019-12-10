#coding:utf-8
#画了4个子图，分别展示了CorrectedGyroRate、RawGyroscopeRate、CorrectedAccelerometerVector、RawAccelerometerData
import matplotlib.pyplot as plt
import time
from threespace import threespace_api as tsapi

imu = tsapi.TSDLSensor(com_port='COM3', baudrate=115200)
plt.ion()
plt.figure(figsize=(12, 8))
t = []
x_len = 10
y = []
y1 = []
y2 = []

t_g_raw = []
g_raw_x = []
g_raw_y = []
g_raw_z = []

t_a_corr = []
a_corr_x = []
a_corr_y = []
a_corr_z = []

t_a_raw = []
a_raw_x = []
a_raw_y = []
a_raw_z = []
# plt.ylim(-2,2) #设置y轴范围

def setData():
    s_t = time.time()
    gyroRate = imu.getCorrectedGyroRate(timestamp=True)
    gyroRaw = imu.getRawGyroscopeRate(timestamp=True)
    acc_corr = imu.getCorrectedAccelerometerVector(timestamp=True)
    accRaw = imu.getRawAccelerometerData(timestamp=True)


    gyroRate_x = gyroRate[0][0]
    gyroRate_y = gyroRate[0][1]
    gyroRate_z = gyroRate[0][2]
    time_ms = gyroRate[1]

    gyroRaw_x = gyroRaw[0][0]
    gyroRaw_y = gyroRaw[0][1]
    gyroRaw_z = gyroRaw[0][2]
    time_graw = gyroRaw[1]

    a_c_x = acc_corr[0][0]
    a_c_y = acc_corr[0][1]
    a_c_z = acc_corr[0][2]
    t_a_c = acc_corr[1]

    a_r_x = accRaw[0][0]
    a_r_y = accRaw[0][1]
    a_r_z = accRaw[0][2]
    t_a_r = accRaw[1]
    if len(y) < x_len:
        t.append(time_ms)
        y.append(gyroRate_x)
        y1.append(gyroRate_y)
        y2.append(gyroRate_z)

        t_g_raw.append(time_graw)
        g_raw_x.append(gyroRaw_x)
        g_raw_y.append(gyroRaw_y)
        g_raw_z.append(gyroRaw_z)

        t_a_corr.append(t_a_c)
        a_corr_x.append(a_c_x)
        a_corr_y.append(a_c_y)
        a_corr_z.append(a_c_z)

        t_a_raw.append(t_a_r)
        a_raw_x.append(a_r_x)
        a_raw_y.append(a_r_y)
        a_raw_z.append(a_r_z)

    else:
        t[:-1] = t[1:]
        y[:-1] = y[1:]
        y1[:-1] = y1[1:]
        y2[:-1] = y2[1:]
        t[-1] = time_ms
        y[-1] = gyroRate_x
        y1[-1] = gyroRate_y
        y2[-1] = gyroRate_z

        t_g_raw[:-1] = t_g_raw[1:]
        g_raw_x[:-1] = g_raw_x[1:]
        g_raw_y[:-1] = g_raw_y[1:]
        g_raw_z[:-1] = g_raw_z[1:]
        t_g_raw[-1] = time_graw
        g_raw_x[-1] = gyroRaw_x
        g_raw_y[-1] = gyroRaw_y
        g_raw_z[-1] = gyroRaw_z

        t_a_corr[:-1] = t_a_corr[1:]
        a_corr_x[:-1] = a_corr_x[1:]
        a_corr_y[:-1] = a_corr_y[1:]
        a_corr_z[:-1] = a_corr_z[1:]
        t_a_corr[-1] = t_a_c
        a_corr_x[-1] = a_c_x
        a_corr_y[-1] = a_c_y
        a_corr_z[-1] = a_c_z

        t_a_raw[:-1] = t_a_raw[1:]
        a_raw_x[:-1] = a_raw_x[1:]
        a_raw_y[:-1] = a_raw_y[1:]
        a_raw_z[:-1] = a_raw_z[1:]
        t_a_raw[-1] = t_a_r
        a_raw_x[-1] = a_r_x
        a_raw_y[-1] = a_r_y
        a_raw_z[-1] = a_r_z

    plt.subplot(221)
    plt.plot(t, y, '.--r')
    plt.plot(t, y1, '.--b')
    plt.plot(t, y2, '.--y')
    plt.legend(['x axis', 'y axis', 'z axis'])
    plt.title('Corrected Gyro Rate', fontsize=10)
    plt.xlabel('time/ms')
    plt.ylabel('gyroRate')

    plt.subplot(222)
    plt.plot(t_g_raw, g_raw_x, '.--r')
    plt.plot(t_g_raw, g_raw_y, '.--b')
    plt.plot(t_g_raw, g_raw_z, '.--y')
    plt.legend(['x axis', 'y axis', 'z axis'])
    plt.title('Raw Gyro Rate', fontsize=10)
    plt.xlabel('time/ms')
    plt.ylabel('rawRate')

    plt.subplot(223)
    plt.plot(t_a_corr, a_corr_x, '.--r')
    plt.plot(t_a_corr, a_corr_y, '.--b')
    plt.plot(t_a_corr, a_corr_z, '.--y')
    plt.legend(['x axis', 'y axis', 'z axis'])
    plt.title('Corrected Acc Rate', fontsize=10)
    plt.xlabel('time/ms')
    plt.ylabel('correctedRate')

    plt.subplot(224)
    plt.plot(t_a_raw, a_raw_x, '.--r')
    plt.plot(t_a_raw, a_raw_y, '.--b')
    plt.plot(t_a_raw, a_raw_z, '.--y')
    plt.legend(['x axis', 'y axis', 'z axis'])
    plt.title('Raw Acc Rate', fontsize=10)
    plt.xlabel('time/ms')
    plt.ylabel('rawRate')
    plt.tight_layout()
    plt.pause(0.0000004) #s  250HZ
    e_d = time.time()
    print(e_d-s_t)
def loop_fun(fun,secs):
    while True:
        fun()
        time.sleep(secs)
loop_fun(setData,0)





