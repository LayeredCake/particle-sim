

#A two-dimensional vector
class Vec():
    
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    #Returns a string representation of the vector as "(x, y)"
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
            
    #Returns true if a vector other is equal to this vector. Two vectors are equal if their x and y values are both equal.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    #Returns a vector that is the sum of this vector and the vector other.
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    #If other is a number, return a vector that is the result of this vector scaled by other. If other is a vector, return the dot product
    #of this vector with other.
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vec(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    #Returns a vector that is this vector summed with inverse of the vector other.
    def __sub__(self, other):
        return self + other * -1
        
    #Returns the length of this vector.
    def length(self):
        return (self * self) ** 0.5

    #Returns a unit vector in the direction of this vector. 
    def unit(self):
        if self.length() != 0:
            return self * ( 1 / self.length())
        else:
            return self

    #Returns a vector that is normal to this vector and with the same length as this vector.
    def normal(self):
        return Vec(self.y, self.x * -1)

    #Returns the angle (in radians) between this vector and the vector other.
    def angle(self, other):
        if (self.length() * other.length()) != 0:
            s = (self * other) * (1 / (self.length() * other.length()))
            if s > 1:
                s = 1
            elif s < -1:
                s = -1
            return math.acos(s)
        else:
            return 0
            
            