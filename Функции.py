def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3, 4) # прямая передача значений

x = 5
y = 7

printMax(x, y) # передача переменных в качестве аргументов

# При первом вызове функции printMax мы напрямую передаём числа в качестве аргументов. 
# Во втором случае мы вызываем функцию с переменными в качестве аргументов. 
# printMax(x, y) назначает значение аргумента x параметру a, 
# а значение аргумента y – параметру b. В обоих случаях функция printMax работает одинаково

# Ключевые аргументы
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

# Вывод:
# a равно 3, b равно 7, а c равно 10
# a равно 25, b равно 5, а c равно 24
# a равно 100, b равно 5, а c равно 50




from re import S
from this import s


def testfunc(myname):
    print('Привет, %s' % myname)
testfunc('Мэри')

def testfunc(fname, lname):
    print('Привет, %s %s' % (fname, lname))
testfunc('Мэри', 'Смит')

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(10, 10, 5))

# Переменные созданные в функции, не работают за её пределами
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
print(variable_test())

# Можно использовать переменные вне вункции
another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
print(variable_test2())

# def spaceship_building(cans):
#     total_cans = 0 
#     for week in range(1, 53):
#         total_cans = total_cans + cans
#         print('Неделя %s, банок: %s' % (week, total_cans))
# spaceship_building(2)

# import time
import sys

# print(time.asctime())
# print(sys.stdin.readline())

def silly_age_joke():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')
silly_age_joke()

