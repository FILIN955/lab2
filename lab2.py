print('Вариант 9')
print('1 task, флаг Финляндии')
print(u"\u001b[47m     \u001b[44m  \u001b[47m             \u001b[0m")
print(u"\u001b[47m     \u001b[44m  \u001b[47m             \u001b[0m")
print(u"\u001b[44m                    \u001b[0m")
print(u"\u001b[47m     \u001b[44m  \u001b[47m             \u001b[0m")
print(u"\u001b[47m     \u001b[44m  \u001b[47m             \u001b[0m")

print('2 task, узор i')
x = u"\u001b[41m \u001b[0m"
kol = 7 #количество узора
for i in range(4, 6):
    for j in range(kol):
        print(' ' * (6 - i) + (x * (2 * i)) + (' ' * (6 - i)), end = '')
    print()
for i in range(6, 3, -1):
    for j in range(kol):
        print(' ' * (6 - i) + (x * (2 * i )) + (' ' * (6 - i)), end = '')
    print()

print('3 task, y = x/2')
print('y ↑')
for y in range (12, 0, -1):
    x = y * 2
    print('  |' + x * ' '+ '/')
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
