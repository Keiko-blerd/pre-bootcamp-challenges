#Convert this pseudocode into actual code.
"""
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a =  1 + 1 * 2 / 2
b =  (1 + 1 * 2 ) /  2
"""
x = 1 * 2
x += 1
print("x =", x)

y = (1 + 1)
y *= 2
print("y =",y)

z = (1 * 2)
z += 1
print("z =",z)

a = (2 / 2)
a *= 2
print("a =",a)

b = (1 * 2) + 1
b /= 2
print("b =", b)