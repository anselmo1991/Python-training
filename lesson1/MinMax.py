numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
new_numbers = []

for val in numbers:

    try:
        new_numbers.append(int(val))
    except (TypeError, ValueError):
        pass

print(new_numbers)
print('Min value', min(new_numbers))
print('Max value', max(new_numbers))