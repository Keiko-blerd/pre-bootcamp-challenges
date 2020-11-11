#Write a function that takes 2 numbers as input. 
#If either of the numbers is 3, OR if the sum of the numbers contains a 3 then return true. 
#Otherwise return false

def func():
    #ask user to enter a number
    print("Please enter a number")
    x = int(input())    #store the number in variable x and convert it to an interger
    #ask user to enter another number
    print("please enter another number")
    y = int(input())    #store the number in variable y and convert it to an interger
    sum = (x + y)       #create a sum of both numbers and store it inside sum variable

    #convert the sum to a string so you can check the values one by one if they contain a 3
    sum_str = str(sum)  #converted value of sum
    sumcheck = "no"     #this variable will be used to determine if the string contains a 3
    

    #iterate through the string with a while loop using the length of sum_str as the delimeter
    i = 0
    while i <= len(sum_str):
        if (i == "3"):          #if at any point the string contains the character 3 sumcheck value turns to "yes"
            sumcheck = "yes"
        else:
            sumcheck = sumcheck
        i += 1
    
    if (x == 3 or y == 3 or sumcheck == "yes"):   #use controle statements If and if and else to print desired outcome
        return(True)
    else:
        return(False)

print(func())