#White a function that takes in three numbers and returns the maximum number. 
#Do this without using any builtin methods. Write your own logic from scratch.

def maximum():
    #ask user to enter a number
    print("Please enter a number")
    x = int(input())    #store the number in variable x and convert it to an interger
    #ask user to enter another number
    print("please enter another number")
    y = int(input())

    print("please enter the last number")
    z = int(input())

    #use controll statements to print the largest number
    if (x >= y and x >= z):
        return(x)
    elif (y >= x and y >= z):
        return(y)
    elif (z >= x and z >= y):
        return(z)
    else:
        return(False)

print("The max num is", maximum())