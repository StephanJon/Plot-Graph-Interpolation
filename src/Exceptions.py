## @file Exceptions.py
#  @author Stephanus Jonatan
#  @date February 20, 2018

class IndepVarNotAscending(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class SeqSizeMismatch(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class InvalidInterpOrder(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Full(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class InvalidIndex(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class OutOfDomain(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)