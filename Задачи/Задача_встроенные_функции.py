# затем напишите небольшую программу, ко-
# торая печатает слова из следующей строки через одно, начиная с первого
# слова («этот»)
a = "этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
arr = a.split(' ')
print(arr)

# Напишите программу для копирования файла. (Подсказка: нужно от-
# крыть файл, который вы собираетесь скопировать, считать из него дан-
# ные, создать новый файл-копию и записать туда считанные данные.)
# Проверьте результат работы программы, напечатав содержимое файла-
# копии на экране.

test_file = open('c:\\Users\\Elfa\\Documents\\Обучение\\python\\test.file') #открываем существующий файл
text = test_file.read() #переносим текст в переменную
# print(text)
test_file2 = open('c:\\Users\\Elfa\\Documents\\Обучение\\python\\test.file2', 'w') #Создаем новый файл
test_file2.write(text) #Записываем из переменной в файл 
test_file2.close #заканчиваем писать
test_file2 = open('c:\\Users\\Elfa\\Documents\\Обучение\\python\\test.file2') #читаем его ещё раз
print(test_file2.read()) #выводис на экран