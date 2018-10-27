## @file Data.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

from CurveADT import *

MAX_SIZE = 10
## @brief Data is a class that takes in data of a polynomial into a list.
#  @details Data
#  @details Data uses the classes CurveT, and SeqServices for interLin and index.
class Data(object):

    ## @brief Initializes two empty lists.
    #  @param S is a sequence of CurveT
    #  @param Z a sequence of real numbers
    def __init__(self):
        self.S = []
        self.Z = []

    ## @brief Mutates two lists S and Z and concactenates elements s and z.
    #  @details Checks if list S is full and if the last element in Z is bigger or equal to element z
    #  @param s is an element being added to list S
    #  @param z is an element being added to list Z
    def Data_add(self, s, z):
        if len(self.S) == MAX_SIZE:
            raise Full("The sequence full. Cannot add anymore data")
        elif len(self.Z) > 0 and z <= self.Z[len(self.Z) - 1]:
            raise IndepVarNotAscending("Element %f is smaller than the last value of Z, %f" % (z, self.Z[len(self.Z) - 1]))
        else:
            self.S.append(s)
            self.Z.append(z)

    ## @brief Accesses list S of index i.
    #  @details Checks if list S has index i.
    #  @param i is the index being accessed.
    def Data_getC(self, i):
        if (0 <= i & i <= len(self.S)):
            return self.S[i]
        else:
            raise InvalidIndex("Index (%d) does not exist" % i)

    ## @brief Returns an estimated y value for a given z value using Interpolation.
    #  @param x is the
    #  @param z is the value used to determine the approximate index of list Z.
    def Data_eval(self, x, z):
        if isInBounds(self.Z, z):
            j = index(self.Z, z)
            return interpLin(self.Z[j], self.S[j].eval(x), self.Z[j + 1],
                             self.S[j + 1].eval(x), z)
        else:
            raise OutOfDomain("z is out of the domain of Z")


    ## @brief Returns CurveT with list Z as the x data and maps .
    #  @param x is the
    #  @param z is the value used to determine the approximate index of list Z.
    def Data_slice(self, x, i):
        Y = []
        for a in range(0, len(self.Z), 1):
            Y.append(self.S[a].eval(x))
        return CurveT(self.Z, Y, i)


