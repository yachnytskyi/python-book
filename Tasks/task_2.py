import math

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
print(sites['Moscow'][0])

distances = {}
distances['Moscow-London'] = (math.sqrt((sites['Moscow'][0] - sites['London'][0])
                                        ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2))
distances['Moscow-Paris'] = (math.sqrt((sites['Moscow'][0] - sites['Paris'][0])
                                       ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2))
distances['London-Paris'] = (math.sqrt((sites['London'][0] - sites['Paris'][0])
                                       ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2))
print(distances)

radius = 42
area = radius * 3.1415926 ** 2
print(round(area))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
print(math.sqrt(point_1[0] ** 2 + point_1[1] ** 2) <= area)

point_2 = (30, 30)
print(math.sqrt(point_2[0] ** 2 + point_2[1] ** 2) <= area)
