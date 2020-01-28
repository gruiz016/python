x = [1, 2, 3, 4, 5]

# List are mutable

x[2] = 42

# Tuples are immutable, meaning you can not change after its assignment

y = (1, 2, 3, 4, 5)

# y[0] = 45 - this can not work.

# Range has 3 paramaters range(start, end, step). Range is also immutable.

z = range(100)

for i in x:
    print('i is {}'.format(i))

# Dictionaries, keys and value can be any type. Dic are mutable.

a = {'one': 1, 'two': 2}
for k, v in a.items():
    print(f'Key is: {k}, Value is: {v}, in A dictionary.')


b = (1, 2, 3, 4, 5)
c = [1, 2, 3, 4, 5]

print(type(b))
print(type(c))

print(id(b))
print(id(c))

# Use isinstance to determine if a variable is a certain type.

if isinstance(b, tuple):
    print('Tuple')
elif isinstance(b, list):
    print('List')
else:
    print('Neither')

if isinstance(c, tuple):
    print('Tuple')
elif isinstance(c, list):
    print('List')
else:
    print('Neither')
