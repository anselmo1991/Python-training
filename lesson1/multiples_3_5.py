# sum = 0
# for i in range(100000000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print('The sum of all multiples=', sum)


N = 100000000


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


print(several_for_loops())


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


print(iterate_over_fifteen())


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


print(math_formula())