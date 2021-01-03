#Write a function that takes in three numbers. 
#These numbers represent the lengths of the sides of a triangle.
#The function should return the area of a triangle.
from math import sqrt

def area_of_triangle(x,y,z):
    half = 0.5
    s = half * (x + y + z)
    area1 = s - x
    area2 = s - y
    area3 = s - z
    area4 = area1 * area2 * area3
    area5 = s * area4
    area = sqrt(area5)
    return area