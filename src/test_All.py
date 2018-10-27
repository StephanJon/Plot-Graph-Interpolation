from CurveADT import *
from CurveADT import __interp__
from Data import *
from SeqServices import *

# Tests for CurveT methods
Curve1 = CurveT([1,2,3,4], [1,2,3,4], 1)
Curve2 = CurveT([1,2,3,4,5], [1,4,9,16,25], 2)
def test_minD():
    assert Curve1.minD() == 1
    assert Curve2.minD() == 1
    print("test_minD: \t\t\tPass")

def test_maxD():
    assert Curve1.maxD() == 4
    assert Curve2.maxD() == 5
    print("test_maxD: \t\t\tPass")

def test_order():
    assert Curve1.order() == 1
    assert Curve2.order() == 2
    print("test_order: \t\t\tPass")

def test_eval():
    assert Curve1.eval(2) == 2
    assert Curve2.eval(3) == 9
    print("test_eval: \t\t\tPass")

def test_dfdx():
    assert round(Curve1.dfdx(2)) == 1.0
    assert round(Curve2.dfdx(2)) == 4.0
    print("test_dfdx: \t\t\tPass")

def test_dfdx2():
    assert round(Curve1.dfdx2(2)) == 0.0
    assert round(Curve2.dfdx2(2)) == 2.0
    print("test_dfdx2: \t\t\tPass")

def test___interp__():

    assert __interp__(Curve1.x_data, Curve1.y_data, Curve1.order(), 2) == 2
    assert __interp__(Curve2.x_data, Curve2.y_data, Curve2.order(), 2) == 4
    print("test___interp__: \t\tPass")

# Tests for Data methods
Test_Data = Data()

def test_data___init__():
    Test_Data.S = [1, 4, 9]
    Test_Data.Z = [1, 2, 3]
    Test_Data.__init__()
    assert Test_Data.S == [] and Test_Data.Z == []
    print("test_data___init__: \t\tPass")

def test_data_add():
    Test_Data.S = [1, 4, 9]
    Test_Data.Z = [1, 2, 3]
    Test_Data.Data_add(16, 4)
    assert Test_Data.S == [1, 4, 9, 16]
    assert Test_Data.Z == [1, 2, 3, 4]
    print("test_data_add: \t\t\tPass")

def test_data_getC():
    assert Test_Data.Data_getC(2) == 9
    assert Test_Data.Data_getC(3) == 16
    print("test_data_getC: \t\tPass")

def test_data_eval():
    curve1 = CurveT([1, 2, 3], [1, 2, 3], 1)
    curve2 = CurveT([1, 2, 3], [1, 4, 9], 2)
    test_Data2 = Data()
    test_Data2.Data_add(curve1, 1)
    test_Data2.Data_add(curve2, 3)
    assert test_Data2.Data_eval(1.5, 1) == 1.5
    print("test_data_eval: \t\tPass")

def test_data_slice():
    curve1 = CurveT([1, 2, 3, 4], [1, 2, 3, 4], 1)
    curve2 = CurveT([1, 2, 3, 4], [1, 4, 9, 16], 2)
    test_Data3 = Data()
    test_Data3.Data_add(curve1, 2)
    test_Data3.Data_add(curve2, 3)
    assert test_Data3.Data_slice(2, 1).order() == 1
    assert test_Data3.Data_slice(2, 1).maxD() == 3
    assert test_Data3.Data_slice(2, 1).minD() == 2
    print("test_data_slice: \t\tPass")

# Tests for SeqServices methods
def test_isAscending():
    assert isAscending([1, 2, 3])
    assert isAscending([1, 2, 2, 3, 10])
    assert not isAscending([10, 3, 2, 5, 6])
    print("test_isAscending: \t\tPass")

def test_isInBounds():
    assert not isInBounds([1, 2, 3, 4], 5)
    assert isInBounds([1, 2, 6, 8], 4)
    assert isInBounds([1, 2, 3, 4], 4)
    print("test_isInBounds: \t\tPass")

def test_interpLin():
    assert interpLin(2, -5, 6, -17, 3) == -8
    assert interpLin(3, 3, 5, 5, 4.5) == 4.5
    assert interpLin(1, 1, 2, 2, 100) == 100
    print("test_interpLin: \t\tPass")

def test_interpQuad():
    assert interpQuad(1, 1, 2, 4, 3, 9, 2.5) == 6.25
    assert interpQuad(-1, 1, -2, 4, -3, 9, -6) == 36
    print("test_interpQuad: \t\tPass")

def test_index():
    assert index([1, 3, 4, 5], 3) == 1
    assert index([1, 3, 4, 5, 6, 10, 16], 12.5) == 5
    print("test_index: \t\t\tPass")

# Main method

def main():
    print("CurveADT test methods:")
    test_minD()
    test_maxD()
    test_order()
    test_eval()
    test_dfdx()
    test_dfdx2()
    test___interp__()

    print("\nData test methods:")
    test_data___init__()
    test_data_add()
    test_data_getC()
    test_data_eval()
    test_data_slice()

    print("\nSeqServices test methods:")
    test_isAscending()
    test_isInBounds()
    test_interpLin()
    test_interpQuad()
    test_index()

main()