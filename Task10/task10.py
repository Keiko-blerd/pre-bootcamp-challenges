#Write a function that takes in a string and then prints out all the vowels in the string. 
#Make sure it can deal with capital letters and small letters.

def printVowels(str):
    result = []
    s = ''
    i = 0
    j = 0
    while i < len(str):
        if (str[i] == 'A' or str[i] == 'a' or str[i] == 'E' or str[i] == 'e' or str[i] == 'I' or str[i] == 'i' 
            or str[i] == 'O' or str[i] == 'o' or str[i] == 'U' or str[i] == 'u'):
            result.append(str[i])
        i += 1
    print(s.join(result))
    


print("Enter Any String")
str = input()
printVowels(str)