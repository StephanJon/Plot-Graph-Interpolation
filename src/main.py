from Plot import *
from Load import *

def main():
    # x = [1, 2, 3, 4, 5, 6]
    # y = [1, 4, 9, 16, 25, 36]
    # c = CurveT(x, y, 2)
    # PlotSeq(x, y)
    # PlotCurve(c, 2)
    # loadtest = Load("glass.csv")
    # print (loadtest.z)
    # print ("\n")
    # print (loadtest.o)
    # print ("\n")
    # print (loadtest.x)
    # print ("\n")
    # print (loadtest.y)
    # print ()
    data = Data()
    data.S = [1, 4, 9, 16]
    data.Z = [1, 2, 3, 4]
    print(data.Data_eval(1, 1))
    print(data.Data_eval(2, 3))

    # def test_data_slice():
    #     assert data.Data_slice(3, 2) ==
    #     assert x.Data_slice(3, 2) ==

main()