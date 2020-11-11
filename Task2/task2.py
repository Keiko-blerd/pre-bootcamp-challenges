#Convert this pseudocode into actual code.
"""
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a =  1 + 1 * 2 / 2
b =  (1 + 1 * 2 ) /  2
"""
# x is equal to the sum of 1 + 1 * 2 multipication is done before addition
x = 1 * 2
    #x is now equal to 2
x += 1
    #the expexted output is x = 3
print("x =", x)

#y is equal to the sum of (1 + 1) * 2 brackets are to be solved first
y = (1 + 1)
    #y is now eqaul to 2
y *= 2
    #the expectedd output is y = 4
print("y =",y)

# z is equal to the sum of 1 + ( 1 * 2 ) brackets are to be solved first
z = (1 * 2)
    #z is now equal to 2
z += 1
    #the expexted output is z = 3
print("z =",z)

# a is equal to the sum of 1 + 1 * 2 / 2 division is done before multiplication
a = (2 / 2)
    #a is now equal to 1.0
    #1 + 1 = 2
a *= 2
    # the expexted output is a = 2.0
print("a =",a)

# b is equal to the sum of (1 + 1 * 2 ) /  2 the bracket is to be solved first.
        #multiplication is done first.
b = (1 * 2) + 1
        #b is now equal to 3
b /= 2
    #expected output is 1.5
print("b =", b)