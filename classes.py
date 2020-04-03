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
print(s)