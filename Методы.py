# Метод — это функция, применяемая к объекту, в данном случае — к строке.
# Метод вызывается в виде Имя_объекта.Имя_метода(параметры). 
# Например, S.find("e") — это применение к строке S метода find с одним 
# параметром "e".

# Методы find и rfind

# Функция возвращает индекс первого вхождения искомой подстроки. 
S = 'Hello'
print(S.find('e')) # вернёт 1
print(S.find('ll')) # вернёт 2
print(S.find('L')) # вернёт -1
#А налогично, метод  rfind возвращает индекс 
# последнего вхождения данной строки (“поиск справа”). 
S = 'Hello'
print(S.find('H')) # вернёт 0
print(S.rfind('H')) # вернёт 0
# Если вызвать метод find с тремя параметрами S.find(T, a, b), 
# то поиск будет осуществляться в срезе S[a:b]. 
# Если указать только два параметра S.find(T, a), 
# то поиск будет осуществляться в срезе S[a:], 
# то есть начиная с символа с индексом a и до конца строки. 
# Метод S.find(T, a, b) возращает индекс в строке S, 
# а не индекс относительно среза. 

# Метод replac

# Метод replace заменяет все вхождения одной строки на другую. 
# Формат: S.replace(old, new) — заменить в строке S все вхождения 
# подстроки old на подстроку new
print('Hello'.replace('l', 'L')) # вернёт 'HeLLo'
# Если методу replace задать еще один параметр: S.replace(old, new, count), 
# то заменены будут не все вхождения, а только не больше, чем первые count из них. 
print('Abrakadabra'.replace('a', 'A', 2)) # вернёт 'AbrAkAdabra'

# Метод count

# Подсчитывает количество вхождений одной строки в другую строку. 
# Простейшая форма вызова S.count(T) возвращает число вхождений 
# строки T внутри строки S. При этом подсчитываются только 
# непересекающиеся вхождения, например: 
print('Abracadabra'.count('a')) # вернёт 4
print(('a' * 10).count('aa')) # вернёт 5
# При указании трех параметров S.count(T, a, b), 
# будет выполнен подсчет числа вхождений строки T в срезе S[a:b].
