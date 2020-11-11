#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


#make a variable that starts from 0
sum = 0

#make a loop that will count from 1 up to 999 using the range function
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0): #if the number at that index is divisible by 3 or 5 add the number to sum
        sum += i
print("Sum of all the multiples of 3 or 5 below 1000 is", sum)