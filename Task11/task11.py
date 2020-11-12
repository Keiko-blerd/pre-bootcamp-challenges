#Make a function that takes two strings as input, and outputs the common characters/letters that they share. 
#(For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

def common(str1, str2):
    result = []
    i = 0
    j = 0
    while i < len(str1):
        while j < len(str2):
            if str1[i] == str2[j]:
                result.append(str2[j])
            j += 1
        i += 1
    print(result)

print("Type a String")
str1 = input()
print("Type another string")
str2 = input()
common(str1, str2)