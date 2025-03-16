# -*- coding: utf-8 -*-
from circle import *
from math import pi

def test_circle_calculate_perimeter():
    circle = Circle(5)

    assert circle.calculate_perimeter() == 2 * pi * 5


def test_circle_calculate_area():
    circle = Circle(5)

    assert circle.calculate_area() == pi * (5 ** 2)