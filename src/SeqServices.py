## @file SeqServices.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

## @brief Checks if sequence X consists of ascending data points.
#  @param X is the sequence being checked
def isAscending(X):
    if sorted(X) == X:
        return True
    else:
        return False

## @brief Checks if the value x is within sequence X.
#  @param X is the sequence being checked
#  @param x is the value being checked
def isInBounds(X, x):
    if (X[0] <= x & x <= X[len(X)-1]):
        return True
    else:
        return False

## @brief Estimates a y value for a given x value using linear interpolation.
#  @details SeqServices
#  @param x1 is a known data point; either smaller or exactly equal to x
#  @param y1 is the corresponding y value for x1
#  @param x2 is a known data point; either exactly equal of larger than x
#  @param y2 is the corresponding y value for x2
#  @param x is the value used to estimate y
def interpLin(x1, y1, x2, y2, x):
    return (y2-y1)*(x - x1)/(x2 - x1) + y1

## @brief Estimates a y value for a given x value using quadratic interpolation.
#  @param x0 is a known data point; smaller than x
#  @param y0 is the corresponding y value for x0
#  @param x1 is a known data point; either smaller or exactly equal to x
#  @param y1 is the corresponding y value for x1
#  @param x2 is a known data point; either exactly equal of larger than x
#  @param y2 is the corresponding y value for x2
#  @param x is the value used to estimate y
def interpQuad(x0, y0, x1, y1, x2, y2, x):
    t1 = (y2-y0)*(x-x1)/(x2-x0)
    t2 = (y2-2*y1+y0)*((x-x1)**2)/(2*(x2-x1)**2)
    return y1 + t1 + t2

## @brief Estimates the index of a value x in sequence X.
#  @details Assumes that sequence X is sorted with ascending order.
#  @param X is the sequence being checked
#  @param x is the value
def index(X, x):
    for i in range(0, len(X)-1):
        if (X[i] <= x and x < X[i+1]):
            return i
    return None