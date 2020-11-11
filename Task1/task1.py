#Convert this pseudocode into actual code.
"""
x = 0
y = 1
Print the value of x
Print the value of y
x = x + 3
y = y + x
Print the value of x
Print the value of y

"""

# Declare variables x and y
x = 0
y = 1

#print the variables to standard output

print(x)
print(y)

#change the value of x by adding 3. change the value of y by adding the new value of x to it.
x = x + 3  # x is now equal to 3
y = y + x  # y is now equal to 4

#print the new values to standard output.
print(x)
print(y)

#the expected output should be
# 0
# 1
# 3
# 4
