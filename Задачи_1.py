#1. Любимые вещи
from email import message
from re import S
from tkinter.font import families


games = ['chees', 'football']
foods = ['apple', 'banana']
favorites = (games + foods)
print(favorites)
#2. Подсчет воинов
samuraes = int(3 * 25)
tunnels = int(2 * 40)
warriors = samuraes + tunnels
print(warriors)
#3. Приветствие
name = 'Sergey'
surname = 'Kozlov'
message = 'Привет, %s %s!'
print(message % (name, surname) )