## @file Plot.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

from CurveADT import *
import matplotlib.pyplot as win

## @brief Returns a x-y graph.
#  @details Data points are in sequences X and Y.
#  @param X is a sequence filled with x data points
#  @param Y is a sequence filled with y data points
def PlotSeq(X, Y):
    if len(X) != len(Y):
        raise SeqSizeMismatch("The sequences are not the same size")
    win.plot(X, Y, 'b')
    win.xlabel("x-axis")
    win.ylabel("y-axis")
    win.show()

## @brief Returns a x-y graph of curve c.
#  @details plots c at n equally spaced points
#  @param c is a curve of CurveT
#  @param n is the number of points inbetween each plotted data point of c
def PlotCurve(c, n):
    interval = (c.maxD() - c.minD()) / n
    X_data = []
    Y_data = []
    if c.order() == 1:
        for i in range(c.minD(), c.maxD(), interval):
            Y_data.append(c.eval(i))
    elif c.order() == 2:
        for i in range(c.minD(), c.maxD(), interval):
            Y_data.append(c.eval(i))
    X_data += range(c.minD(), c.maxD(), interval)
    PlotSeq(X_data, Y_data)