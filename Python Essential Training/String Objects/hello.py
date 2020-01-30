print('Hello, World.'.upper())

print('Hello, World.'.swapcase())

print('Hello, World. {}'.format(42 * 7))

s = 'Hello World. {}'

print(s.format(4*6))


class MyString(str):
    def __str__(self):
        return self[::-1]


backward_string = MyString('Giovanni')

print(backward_string)
