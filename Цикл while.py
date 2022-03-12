# step = 0
# while step < 10000:
#     print(step)
#     if tired == True:
#         break
#     elif badweather == True:
#         break
#     else:
#         step = step + 1

# Несколько условия
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)

# Задание вопроса в цикле
number = 23
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
    # Здесь можете выполнить всё что вам ещё нужно

print('Завершение.')