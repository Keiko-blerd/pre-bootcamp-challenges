#Write a function that takes in a number representing the temperature in Fahrenheit
#and returns the temperature in Celsius.

def celsius():
    print("Enter the temperature in Fahrenheit")
    t = int(input())
    #The temperature t in degrees Celsius (°C) is equal to the temperature t in degrees Fahrenheit (°F) minus 32, times 5 / 9
    c = t - 32
    c *= (5 / 9)
    return(c)

print(celsius(), "C")