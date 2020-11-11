#Write a function that takes in three numbers. 
#These numbers represent the lengths of the sides of a triangle.
#The function should return the area of a triangle.
from math import sqrt

def area():
        #ask user to enter a number
    print("Please enter a number")
    x = int(input())    #store the number in variable x and convert it to an interger
    #ask user to enter another number
    print("please enter another number")
    y = int(input())

    print("please enter the last number")
    z = int(input())

    #Calculate the semiperimeter of the triangle.
    #The semi-perimeter of a figure is equal to half its perimeter. 
    #To find the semiperimeter, first calculate the perimeter of a triangle by adding up the length of its three sides. 
    #Then, multiply by 0.5
    half = 0.5
    s = half * (x + y + z)
    area1 = s - x
    area2 = s - y
    area3 = s - z
    area4 = area1 * area2 * area3
    area5 = s * area4
    area = sqrt(area5)
    return(area)

print("The Area of the triangle is", area(), "square centimeters.")