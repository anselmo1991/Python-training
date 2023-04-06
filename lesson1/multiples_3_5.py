sum = 0
for i in range(100000000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print('The sum of all multiples=', sum)
