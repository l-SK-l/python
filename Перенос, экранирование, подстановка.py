from email import message


found_coins = 20
magic_coins = 13
stolen_coins = 2
all_coins = found_coins + magic_coins * 365 - stolen_coins * 52
print(all_coins)
# перенос строк
text = '''"Тут что-то не так, не будь я д'Артаньян" — 
подумал он.'''
# экранирование
text2 = '"Тут что-то не так, не будь я д\'Артаньян", — подумал он.'
print(text2)
# Подстановка
myscore=1000
message= 'Мой счёт: %s очков'
nums = 'Что сказало число %s числу %s? Славный поясок!'
print(message % myscore)
print(nums % (0, 8))