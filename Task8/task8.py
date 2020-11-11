#Make a function to convert any number into hours and minutes. 
#(For example, 71 will become “1 hour, 11 minutes”; 133 will become “2 hours, 13 minutes”.)

def convert_time():
    print("Enter any number")
    number = int(input())
    hour = int(number / 60)         # the hour is equal to the rounded off number of what the user inputs divided by 60
    minute = number % 60            #the minutes are whatever remains when you divide the user input by 60
    if number < 60:
        print(minute, "minutes")
    elif hour > 1:
        print(hour,"hours,", minute,"minutes")
    else:
        print(hour,"hour,", minute,"minutes")

convert_time()