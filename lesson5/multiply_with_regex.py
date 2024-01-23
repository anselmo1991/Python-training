import re

def my_function(text, multiplier=2):
    def double_digit(match):
        digit = int(match.group(0))
        return str(digit * multiplier)

    pattern = r'\d+'
    result = re.sub(pattern, double_digit, text)
    return result

text1 = 'Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных'
result1 = my_function(text1)
print(result1)