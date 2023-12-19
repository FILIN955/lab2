print('Вариант 9')
print('1 task, флаг Финляндии')
WIDTH = 13
WIDTH2 = 20
print(f"\u001b[47m     \u001b[44m  \u001b[47m{' '*WIDTH}\u001b[0m")
print(f"\u001b[47m     \u001b[44m  \u001b[47m{' '*WIDTH}\u001b[0m")
print(f"\u001b[44m{' '*WIDTH2}\u001b[0m")
print(f"\u001b[47m     \u001b[44m  \u001b[47m{' '*WIDTH}\u001b[0m")
print(f"\u001b[47m     \u001b[44m  \u001b[47m{' '*WIDTH}\u001b[0m")

print('2 task, узор i')
x = "\u001b[41m \u001b[0m"
kol = 7
for i in range(4, 6):
    for j in range(kol):
        print(' ' * (6 - i) + (x * (2 * i)) + (' ' * (6 - i)), end='')
    print()
for i in range(6, 3, -1):
    for j in range(kol):
        print(' ' * (6 - i) + (x * (2 * i)) + (' ' * (6 - i)), end='')
    print()

print('3 task, y = x/2')
print('y ↑')
for y in range(12, 0, -1):
    x = y * 2
    print('  |' + x * ' '+'/')
print('  |' + '─ ' * 13 + '→x')

print('task 4, от 5 до 10 и числа от -5 до -10, остальные отбросить')
x1 = 0
x2 = 0
all_digits = 0
with open('sequence.txt') as file:
    for line in file:
        digit = float(line)
        all_digits += 1
        if 5 <= digit <= 10:
            x1 += 1
        elif -10 <= digit <= -5:
            x2 += 1
proc1 = round(x1 / all_digits * 100)
proc2 = round(x2 / all_digits * 100)
print('%')
print('↑')
y1 = u"\u001b[41m \u001b[0m"
y2 = u"\u001b[42m \u001b[0m"
for i in range(100, 0, -1):
    if (proc1 >= i) and (proc2 >= i):
        print('|', y1, y2)
    elif (proc1 >= i):
        print('|', y1)
    elif (proc2 >= i):
        print('|', ' ', y2)
    else:
        print('|')
print("0 " + "- " * 2 + '→')

# Исправление:
'''Префикс u используется для указания, что строковый литерал является строкой в формате Unicode в Python 2. 
Однако в Python 3 все строки по умолчанию интерпретируются как строки в формате Unicode, поэтому префикс u стал необязательным и можно обойтись без него.'''

class Pattern:
    def __init__(self, color, repetitions):
        self.color = color
        self.repetitions = repetitions

    def show(self):
        x = f"\u001b[{self.color} \u001b[0m"
        for i in range(4, 6):
            for j in range(self.repetitions):
                print(' ' * (6 - i) + (x * (2 * i)) + (' ' * (6 - i)), end='')
            print()
        for i in range(6, 3, -1):
            for j in range(self.repetitions):
                print(' ' * (6 - i) + (x * (2 * i)) + (' ' * (6 - i)), end='')
            print()


pattern_instance = Pattern('44m', 10)
pattern_instance.show()
