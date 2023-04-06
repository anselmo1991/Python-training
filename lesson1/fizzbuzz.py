"""
for i in range(101):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 ==0:
        print('Buzz')
    else: print(i)
"""

for i in range(1, 101):
    str = ''

    if i%3 == 0:
        str = str + 'Fizz'
    if i%5 == 0:
        str = str + 'Buzz'

    print(str if str else i)


