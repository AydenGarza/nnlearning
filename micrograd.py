import math
from visualization import draw_dot

class Value:
    def __init__ (self, data, _children = (), _op = "", label=""):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label
        self._backward = lambda: None
        self.grad = 0
    
    def __add__ (self, other):
        outVal = Value(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad = outVal.grad
            other.grad = outVal.grad
        outVal._backward = _backward
        return outVal
    
    def __mul__ (self, other):
        outVal = Value(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad = other.data * outVal.grad
            other.grad = self.data * outVal.grad
        outVal._backward = _backward
        return outVal
    
    def __repr__(self):
        return f"Value(data={self.data})"
    
    def tanh(self):
        x = self.data
        tanhx = (math.exp(2*x)-1)/(math.exp(2*x)+1)
        outVal = Value(tanhx, (self,), "tanh")
        def _backward():
            self.grad = (1-tanhx**2) * outVal.grad
        outVal._backward = _backward
        return outVal
    def backward(self):
        self.grad = 1

        ts = []
        visited = set()
        def build_toposort(n):
            if n not in visited:
                visited.add(n)
                for child in n._prev:
                    build_toposort(child)
                ts.append(n)
        build_toposort(self)
        ts = reversed(ts)
        for node in ts:
            node._backward()

t