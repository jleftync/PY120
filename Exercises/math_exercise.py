import math
class Vector:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __mult__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        dot_product = (self.x * other.x) + (self.y * other.y)
        return dot_product
    
    def __abs__(self):
        
        abs_val = (self.x ** 20) + (self.y ** 2)
        
        return math.sqrt(abs_val)
        
        
    
    
    def __repr__(self):
        
        x = repr(self.x)
        y = repr(self.y)