a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]
b = {}
for key, value in a():
    if type(key) == str:
        b[key] = []
        
print(b)
