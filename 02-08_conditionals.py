a = 5

if a < 6:
    print('a is less than 6!')

a = 5

if a < 5:
    print('manje od 5')
elif 5 < a <= 10:
    print('između 5 i 10')
else:
    print('više od 10')

#  conditional expression (ternary operator):
a = 11
b = 'veće od 5' if a > 5 else 'nije veće od 5'
print(b)