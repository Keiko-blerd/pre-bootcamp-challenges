#Make a function that takes two strings as input, and outputs the common characters/letters that they share. 
#(For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

def common(str1, str2):
    result = []
    s = ', '
    i = 0
    while i < len(str1):
        for j in str2:
            if j == str1[i]:
                if str1[i] in result:
                    continue
                else: 
                    result.append(str1[i])
        i += 1
    print("Common Letters:", s.join(result))
        

print("Type a String")
str1 = input()
print("Type another string")
str2 = input()
common(str1, str2)