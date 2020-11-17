#Write a function that takes in a number representing the temperature in Celsius 
#and returns the temperature in Fahrenheit.

def celsius_to_fahrenheit(t):
    t = float(t)
    f = t * 1.8
    f += 32
    return(f)