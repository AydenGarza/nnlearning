
class Value:
    def __init__ (self, data, _children = (), _op = ""):
        self.data = data
        self._prev = set(_children)
    
    def __add__ (self, other):
        outVal = Value(self.data + other.data, (self, other), "+")
        return outVal
    
    def __mul__ (self, other):
        outVal = Value(self.data * other.data, (self, other), "*")
        return outVal
    
    def __repr__(self):
        return f"Value(data={self.data})"
    