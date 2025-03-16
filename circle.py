# -*- coding: utf-8 -*-

from math import pi
from helper import convert_to_float

class NegativeNumError(Exception):
    def __init__(self, message = "Number must be non-negative!"):
        super().__init__(message)
        
def check_positive(number):
    if number < 0:
        raise NegativeNumError(f"Invalid input: {number} is negative")
    return number

class Circle:
    """
    A class representing a circle.

    Attributes:
    -----------
    radius : float
        The radius of the circle.
    """
    
    def __init__(self, radius: float) -> None:
        """
        Initializes a Circle instance with a given radius.
        
        Parameters:
        -----------
        radius : float
            The radius of the circle. It should be a positive number.
            
        Raises:
            ValueError: If value cannot be converted to a float.
            NegativeNumError: If value of radius is lower than zero.
        """
        
        radius = convert_to_float(radius)
        
        radius = check_positive(radius)
        
        self.radius = radius
        
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter (circumference) of the circle.
        
        Returns:
        --------
        float
            The perimeter of the circle, calculated as 2 * pi * radius.
        """
        return 2 * pi * self.radius
    
    def calculate_area(self) -> float:
        """
        Calculates the area of the circle.
        
        Returns:
        --------
        float
            The area of the circle, calculated as pi * radius^2.
        """
        return pi * (self.radius ** 2)
