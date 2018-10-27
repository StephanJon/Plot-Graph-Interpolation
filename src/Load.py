## @file Load.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

import csv
from Data import *

## @brief Load is a class that reads a csv file.
#  @details The csv file contains data on a set of curves and loads each curve into Data
#  @details z stores the value of each curve.
#  @details o stores the order of each curve
#  @details x stores the x-points of each curve
#  @details y stores the y-points of each curve
#  @param s is the name of the csv file (expected .csv extension)
def Load(s):
    Data.__init__()
    z = []
    o = []
    x = []
    y = []
    with open(s) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        count = 0
        for row in readCSV:
            if count == 0:
                for i in range(0, len(row), 1):
                    z.append(float(row[i]))
                m = len(z)
                x = [[0 for a in range(1)] for b in range(m)]
                y = [[0 for a in range(1)] for b in range(m)]
                count += 1
            elif count == 1:
                for i in range(0, len(row), 1):
                    o.append(float(row[i]))
                count += 1
            else:
                data_list = 0
                for i in range(0, 2*m - 1, 2):
                    add_x = row[i]
                    add_y = row[i + 1]
                    if add_x != '' or add_y != '':
                        x[data_list].append(float(add_x))
                        y[data_list].append(float(add_y))
                    data_list += 1
            for i in range (0, m, 1):
                Data.Data_add(CurveT(x[i],y[i],o[i]), z[i])









