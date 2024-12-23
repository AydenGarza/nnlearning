import numpy as np


class Value:
    def __init__ (self, data, _children = (), _op = "", label=""):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label
    
    def __add__ (self, other):
        outVal = Value(self.data * other.data, (self, other), "+")
        print("Llds")
        return outVal
    
    def __mul__ (self, other):
        outVal = Value(self.data * other.data, (self, other), "*")
        return outVal
    
    def __repr__(self):
        return f"Value(data={self.data})"

a = Value(2)
b = Value(3)
c = a*b
print(c._op)