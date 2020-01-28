from decimal import *

x = 'Seven'

# Multiline strings
y = '''
this is a multiline string
'''
# All strings are objects, you can run format(), upper(), lower(), etc..
z = "this will be capitilized".capitalize()

print('x is {}'.format(x))

# This is an f string, same as the above .format().
print(f'x is {x}')

# Type is a function that displays a class.

print(type(x))

# Numeric types

a = 7/3

# Using decimal helps protect against computer floating point efficency for accuracy with floating points. You have to put floating points into a string. As displayed below.
b = Decimal('.10')
c = Decimal('.30')

d = b + b + b - c

print(f'{d}')

print(f'A is {a}')
print(type(a))

# Bool types

# Rules: None = false, 0 = false, "" = flase, everything else is true.

e = True

print(f'E is {e}')
print(type(e))

if e:
    print('True')
else:
    print('False')
