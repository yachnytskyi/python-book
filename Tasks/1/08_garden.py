garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = garden
meadow_set = meadow

allFlowers = garden_set + meadow_set
print(allFlowers)

commonFlowers = set(garden_set) & set(meadow_set)
print(commonFlowers)

print(garden_set)

print(meadow_set)

