#Write a function that takes 2 numbers as input. 
#If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. 
#Otherwise return false

def func():
    #ask user to enter a number
    print("Please enter a number")
    x = int(input())    #store the number in variable x and convert it to an interger
    #ask user to enter another number
    print("please enter another number")
    y = int(input())    #store the number in variable y and convert it to an interger
    sum = (x + y)       #create a sum of both numbers and store it inside sum variable
    if (x == 65 or y == 65 or sum == 65):   #use controle statements If and if and else to print desired outcome
        return(True)
    else:
        return(False)

print(func())