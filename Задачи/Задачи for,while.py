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
x = 1
y = 0
while ingredients:
    print(str(x) + ' ' + ingredients[y])
    x += 1
    y += 1
    if x == 6:
        break
# или ПРАВИЛЬНЕЕ
i = 1
for ingredients in 'лист', 'катлета', 'соус', 'сыр', 'горчица':
    print(i, ingredients)
    i += 1

# Ваш лунный вес
weight = 85
year = 0
for year in range(1,16):
    print('лунный вес ' + str(weight * 165 / 1000) + ' в ' + str(year) + ' году')
    weight += 1
    if year == 15:
        break
# ИЛИ
weight = 85
for year in range(16):
    weight += 1
    moon_weight = str(weight * 165 / 1000)
    print(moon_weight + ' Лунный вес в ' + str(year) + ' Году')

# По данному целому числу N распечатайте все квадраты 
# натуральных чисел, не превосходящие N, в порядке возрастания. 

n = int(input())
i = 1 # переменая аккумулятор
while i ** 2 <= n: #Все квадратные корни не превосходящие N
    print(i ** 2) 
    i += 1

# Дано целое число, не меньшее 2. 
# Выведите его наименьший натуральный делитель, отличный от 1. 
