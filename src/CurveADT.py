## @file CurveADT.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

from scipy import interpolate
from SeqServices import *
from Exceptions import *

MAX_ORDER = 2
DX = 0.001

## @brief Determines which interpolation formula to use
#  @details Returns the estimated y value for a given value
#  @param X is sequence of X-points
#  @param Y is sequence of Y-points
#  @param o is degree of interpolation
#  @param v is the given value
def __interp__(X, Y, o, v):
    i = index(X, v)
    if o == 1:
        return interpLin(X[i], Y[i], X[i+1], Y[i+1], v)
    elif o == 2:
        return interpQuad(X[i-1], Y[i-1], X[i], Y[i], X[i+1], Y[i+1], v)

## @brief CurveT is a class that analyzes data of a polynomial.
#  @details CurveT uses interpolation to estimate a y value for a given x value.
#  @details CurveT the scipy library.
class CurveT(object):

    ## @brief Initializes a interpolation function.
    #  @details Uses a given list of x and y coordinates, and a degree of interpolation to create the interpolation function.
    #  @param X is the list of x coordinates.
    #  @param Y is the list of y coordinates.
    #  @param i is the degree of interpolation.
    def __init__(self, X, Y, i):
        if not isAscending(X):
            raise IndepVarNotAscending("X is not in ascending order")
        if len(X) == len(Y):
            self.x_data = X
            self.y_data = Y
        else:
            raise SeqSizeMismatch("The number of X-points does not equal the number of Y-Points.")
        if i <= MAX_ORDER:
            self.o = i
            self.f = interpolate.interp1d(self.x_data, self.y_data, self.o)
        else:
            raise InvalidInterpOrder("The degree of interpolation is more than %d" % MAX_ORDER)

    ## @brief minD() returns the smallest element in list self.x_data.
    def minD(self):
        return min(self.x_data)

    ## @brief maxD() returns the largest element in list self.x_data.
    def maxD(self):
        return max(self.x_data)

    ## @brief order() returns the degree of interpolation.
    def order(self):
        return self.o

    ## @brief eval(x) returns an approximate y value for a given x value by interpolation.
    #  @details The given x value must be within the list of x_data.
    #  @param x is the given value used to approximate a y value.
    def eval(self, x):
        if self.minD() <= x <= self.maxD():
            y = self.f(x)
            return y
        else:
            raise OutOfDomain("%f is not within the range" % x)

    ## @brief dfdx(x) returns the value y at a given x value for the derivative of the interpolation function.
    #  @param x is the given x value.
    def dfdx(self, x):
        if self.minD() <= x <= self.maxD():
            return (self.f(x + DX) - self.f(x)) / DX
        else:
            raise OutOfDomain("%f is not within the range" % x)

    ## @brief dfdx2(x) returns the value y at a given x for the second derivative of the interpolation function.
    #  @param x is the given x value.
    def dfdx2(self, x):
        if self.minD() <= x <= self.maxD():
            return (self.f(x + 2*DX) - 2*self.f(x + DX) + self.f(x)) / pow(DX, 2)
        else:
            raise OutOfDomain("%f is not within the range" % x)









