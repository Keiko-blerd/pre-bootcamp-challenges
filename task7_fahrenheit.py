#Write a function that takes in a number representing the temperature in Celsius 
#and returns the temperature in Fahrenheit.

def fahrenheit():
    print("Enter the temperature in Celsius")
    t = float(input())
    f = t * 1.8
    f += 32
    return(f)

print(fahrenheit(), "F")