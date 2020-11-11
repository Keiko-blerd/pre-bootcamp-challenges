#Write a function that takes in a number representing the temperature in Celsius 
#and returns the temperature in Fahrenheit.

def fahrenheit():
    print("Enter the temperature in Celsius")
    t = int(input())
    #The temperature t in degrees Fahrenheit (°F) is equal to the temperature t in degrees Celsius (°C) times 1.8 plus 32:
    f = t * 1.8
    f += 32
    return(f)

print(fahrenheit(), "F")