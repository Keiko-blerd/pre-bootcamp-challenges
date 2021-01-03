#Write a function that takes 2 numbers as input. 
#If either of the numbers is 3, AND if the sum of the numbers contains a 3 then return true. 
#Otherwise return false

def three_checker(x,y):
    z = str(x + y)
    if x == 3 or y == 3 and '3' in z:
        return True
    else:
        return False