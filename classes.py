import math
class Point:
    pass
    """Represents a point in 2-D space."""

blank = Point()    
blank.x = 3.0
blank.y = 4.0

hugo = Point()
hugo.x = -3.0
hugo.y = -4.0  
    

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(hugo)
print_point(blank)
    
def distance_between_two_points(p,q):
    return math.sqrt((p.x - q.x)**2 + (p.y - q.y)**2)
    

s = distance_between_two_points(blank,hugo)
print("distance between Hugo and Blank: ", s)

#----

class Triangle:
    pass
    """calc the area and perimeter of a triangle"""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
        
    def area(self):
        s = Triangle.perimeter(self) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area

willi = Triangle(3, 4, 5)
print(dir())
willi.a = 4.0
willi.c = 3.0
willi.b = 5.0

print(dir())
print('Umfang: ',Triangle.perimeter(willi))
print('Fläche: ',Triangle.area(willi))

