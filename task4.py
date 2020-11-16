#Write a function that takes 2 numbers as input. 
#If either of the numbers is 3, OR if the sum of the numbers contains a 3 then return true. 
#Otherwise return false

def func():
    print("Please enter a number")
    x = int(input())
    print("please enter another number")
    y = int(input())
    sum = (x + y)
    sum_str = str(sum)
    sumcheck = "no"
    i = 0

    while i < len(sum_str):
        if sum_str[i] == "3":
            sumcheck = "yes"
        else:
            sumcheck = sumcheck
        i += 1
    
    if x == 3 or y == 3 or sumcheck == "yes":
        return(True)
    else:
        return(False)

print(func())