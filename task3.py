#Write a function that takes 2 numbers as input. 
#If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. 
#Otherwise return false

def sixty_five_checker(x,y):
    sum = x + y
    if (x == 65 or y == 65 or sum == 65):
        return True
    else:
        return False

print(sixty_five_checker(60,5))