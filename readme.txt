threadqt5.py是最终给老师看的版本，用了双线程，qt5画图，存在问题：开始时画图效率挺快，但是越到后面，用的时间越长，导致到后面存在延时。
danxiancheng.py用matplotlib.animation画图，必须设置xy轴的坐标范围，否则出不来图，而且一个图中只能展示一条曲线。
dataView最初的单线程+matplotlib版本