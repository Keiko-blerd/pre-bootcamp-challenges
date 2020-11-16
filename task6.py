#White a function that takes in three numbers and returns the maximum number. 
#Do this without using any builtin methods. Write your own logic from scratch.

def maximum():
    print("Please enter a number")
    x = int(input())
    print("please enter another number")
    y = int(input())
    print("please enter the last number")
    z = int(input())
    if (x >= y and x >= z):
        return(x)
    elif (y >= x and y >= z):
        return(y)
    elif (z >= x and z >= y):
        return(z)
    else:
        return(False)

print("The max num is", maximum())