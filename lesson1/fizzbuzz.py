"""
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')
    else: print(i)
"""

for i in range(1, 101):
    name = ''

    if i % 3 == 0:
        name = name + 'Fizz'
    if i % 5 == 0:
        name = name + 'Buzz'

    print(name if name else i)


