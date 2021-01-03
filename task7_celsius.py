#Write a function that takes in a number representing the temperature in Fahrenheit
#and returns the temperature in Celsius.

def fahrenheit_to_celsius(t):
    t = float(t)
    c = t - 32
    c *= (5 / 9)
    return(c)
