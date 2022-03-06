for x in range(0, 5):
    print('Привет')

print(list(range(10, 20)))

for x in range(0, 5):
    print('привет %s' % x)

wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки',
'крыло летучей мыши', 'жир слизня', 'медвежий коготь']
for i in wizard_list:
    print(i)

hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coints = found_coins
for week in range(1, 53):
    coints = coints + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coints))

i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep = '')
    i += 1 # Сокращение от i = i + 1

# range выполняется от первого числа до последнего -1, 
# если первое больше второго, то не выполнится совсем
sum = 0
n = 5
for i in range(1, n + 1):
    sum += i
print(sum)

# сделать цикл по всем нечетным числам от 1 до 99 можно при помощи функции 
range(1, 100, 2)

# сделать цикл по всем числам от 100 до 1 можно при помощи 
range(100, 0, -1)

# Более формально, цикл for i in range(a, b, d) 
# при d > 0 задает значения индексной переменной 
# i = a, i = a + d, i = a + 2 * d и так для всех значений,
# для которых i < b. Если же d < 0, то переменная цикла принимает все значения i > b. 

# По умолчанию функция print() принимает несколько аргументов, 
# выводит их через пробел, после чего ставит перевод строки. 
# Это поведение можно изменить, используя именованные параметры sep (разделитель) и end (окончание). 
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ') # Ставлю запятую после каждой цифры, не нажимаю enter
print(4, 5, 6, sep=', ', end='. ') # Продолжаю писать в туже строку
print() # нажимаю Enter
print(1, 2, 3, sep='', end=' -- ') # Убираю пробелы между цифрами
print(4, 5, 6, sep=' * ', end='.') # Продолжаю писать в туже строку без Enter в конце