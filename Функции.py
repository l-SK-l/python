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

