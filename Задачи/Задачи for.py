#  Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 
a = int(input())
b = int(input())
for i in range(a, b):
    b += i
    print(i)
if i == 0:
    print(i)
elif a == b:
    print(i)
else:
    print(i + 1)
# Правильнее:
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

# Даны два целых числа A и В. 
# Выведите все числа от A до B включительно, в порядке возрастания, 
# если A < B, или в порядке убывания в противном случае. 
a = int(input())
b = int(input())
if a <= b:
    for i in range(a, b +1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных. 
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)

# Четные числа
x = 0
while x <= 28:
        print(x)
        x = x + 2

# Пять любимых ингредиентов
ingredients = ['лист', 'катлета', 'соус', 'сыр', 'горчица']
x = 0
y = 0
while ingredients:
    print(str(x) + ' ' + ingredients[y])
    x += 1
    y += 1
    if x == 5:
        break

# Ваш лунный вес
weight = 85
year = 0
for year in range(1,16):
    print('лунный вес ' + str(weight * 165 / 1000) + ' в ' + str(year) + ' году')
    weight += 1
    if year == 15:
        break