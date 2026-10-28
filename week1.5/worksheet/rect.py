# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, (int)):
            raise TypeError("Width must be an integer.")
        if not isinstance(height, (int)):
            raise TypeError("Height must be an integer.")
        
        if width <= 0 or height <= 0:
            raise ValueError("Parameters must be greater than 0.")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here

    def is_square(self):
        '''
        Determines whether the shape is a square
        '''

        if self.width == self.height:
            return 'True'
        else:
            return 'False'

    def area(self):
        '''
        Calculates the area of the rectangle
        '''

        return self.width * self.height
    
    def perimeter(self):
        '''
        Calculates the perimeter of the rectangle
        '''

        return ((self.width * 2) + (self.height * 2))
    # (See README.md for details of what they should do)

""" rectangle_test = Rectangle(3, 5)

print(rectangle_test.is_square())
print(rectangle_test.area())
print(rectangle_test.perimeter()) """