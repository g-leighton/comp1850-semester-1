# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to origin.
        """

        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, p1):
        """
        Returns distance from point 1 to point 2.
        """
        self.point1 = p1
        

        return math.hypot(self.x, self.y)



# Finally, add code here to demonstrate use of Point
p = Point(3, 4)
print(p.x, p.y)
print(p.distance())

p2 = Point(0, 0)
print(p2.distance_to(p))