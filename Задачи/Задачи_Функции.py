#1. Функция лунного веса
# Создайте функцию, которая принимает начальный вес и величину, на которую
# вес увеличивается каждый год. Вызывать эту новую функ-
# цию нужно будет примерно так:
# moon_weight(30, 0.25)

# year = 2000
# def moon_weight(weight, multiplier):
#     new_year = int(weight * multiplier)
#     print('Лунный вес в ' + str(year) + ' Году равен ' + str(new_year))
# moon_weight(80, 0.25)

#2. Функция лунного веса и количество лет
# Измените функцию из предыдущего задания так, чтобы с ее помощью
# можно было рассчитывать вес для разного количества лет, например 5
# или 20 лет. Пусть эта функция принимает три аргумента: начальный вес,
# прибавку веса в год и количество лет:
# moon_weight(90, 0.25, 5)

# def moon_weight(weight, multiplier, all_year):
#     year = 0
#     for all_year in range(year, all_year):
#         new_weight = float(weight + multiplier)
#         year += 1
#         multiplier += multiplier
#         print('Лунный вес в ' + str(year) + ' Году равен ' + str(new_weight))
# moon_weight(80, 0.25, 5)

#3. Программа для лунного веса
# Вместо простой функции, принимающей значения в виде аргументов,
# можно написать мини-программу, которая будет запрашивать эти зна-
# чения с помощью sys.stdin.readline(). Тогда этой функции вообще
# не нужны аргументы:
# moon_weight()
# Функция должна запросить начальный вес, потом прибавку веса
# в год и количество лет.

import sys

print('Введите ваш нынешний земной вес')
weight = int(sys.stdin.readline())
print('Введите ежегодный прирост вашего веса')
multiplier = float(sys.stdin.readline())
print('Введите количество лет')
years = int(sys.stdin.readline())
for all_years in range(2000, 2000 + years):
    weight += multiplier
    moon_weight1 = float(weight * multiplier)
    print('Лунный вес в ' + str(all_years) + ' Году равен ' + str(moon_weight1))