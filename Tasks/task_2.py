import math

sites = iter({
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
})

distances = {}
distances['Moscow-London'] = (math.sqrt((550 - 510) ** 2 + (370 - 510) ** 2))
distances['Moscow-Paris'] = (math.sqrt((550 - 480) ** 2 + (370 - 480) ** 2))
distances['London-Paris'] = (math.sqrt((510 - 480) ** 2 + (510 - 480) ** 2))
print(distances)

radius = 42
area = radius * 3.1415926 ** 2
print(round(area))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
print(math.sqrt(23 ** 2 + 34 ** 2) <= area)

point_2 = (30, 30)
print(math.sqrt(30 ** 2 + 30 ** 2) <= area)