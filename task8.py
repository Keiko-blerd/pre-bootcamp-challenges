#Make a function to convert any number into hours and minutes. 
#(For example, 71 will become “1 hour, 11 minutes”; 133 will become “2 hours, 13 minutes”.)

def convert_time(n):
    number = int(n)
    hour = int(number / 60)
    minute = number % 60
    str_hour = "hours"
    str_min = "minutes"

    if minute == 1:
        str_min = "minute"
    if hour == 1:
        str_hour = "hour"

    if number < 60:
        print(minute, str_min)
    else:
        print(hour, str_hour, minute, str_min)
