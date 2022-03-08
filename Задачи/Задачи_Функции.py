weight = 85
year = 0
for year in range(1,16):
    print('лунный вес ' + str(weight * 165 / 1000) + ' в ' + str(year) + ' году')
    weight += 1
    if year == 15:
        break
def moon_weight():
    