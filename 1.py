# weight = 85
# year = 0
# for year in range(1,16):
#     print('лунный вес ' + str(weight * 165 / 1000) + ' в ' + str(year) + ' году')
#     weight += 1
#     if year == 15:
#         break

weight = 85
for year in range(16):
    weight += 1
    moon_weight = str(weight * 165 / 1000)
    print(moon_weight + ' Лунный вес в ' + str(year) + ' Году')