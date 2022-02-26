
wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
print(wizard_list)
#показыкает элемент из списка
print(wizard_list[2])
# заменяем элемент в списке
wizard_list[2] = 'язык улитки'
print(wizard_list[2])
# показываем список элементов
print(wizard_list[2:5])
# числа
some_numbers = [1, 2, 5, 10, 20]
# строки
some_strings = ['Нож', 'отточен', 'точен', 'очень']
numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь']
print(numbers_and_strings)
# список со списками
my_list = [some_numbers, some_strings]
print(my_list)
# добавляем элемент в список
wizard_list.append('медвежий коготь')
print(wizard_list)
wizard_list.append('мандрагора')
wizard_list.append('болиголов')
wizard_list.append('болотный газ')
print(wizard_list)
# удаляем элемент из списка
del wizard_list[5]
print(wizard_list)
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)
# списковая орифметика
print(some_numbers + some_strings)
list1 = [1, 2]
print(list1 * 5)