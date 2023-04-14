l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

# with for
l1 = []
for i in l:
    if type(i) == int:
        l1.append(i)

print('With for:', l1)


# with list comprehentions
l3 = [i for i in l if type(i) == int]
print('With list comprehention', l3)


# with filter() + lambda
l2 = filter(lambda i: type(i) == int, l)
print('With lambda:', list(l2))
