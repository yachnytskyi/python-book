# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
paper_x, paper_y = 9, 8
paper_x, paper_y = 6, 8
paper_x, paper_y = 8, 6
paper_x, paper_y = 3, 4
paper_x, paper_y = 11, 9
paper_x, paper_y = 9, 11

if envelop_x > paper_x and envelop_y > paper_y:
    print("Yes")

elif envelop_x < paper_x or envelop_y < paper_y:
    if envelop_x > paper_y and envelop_y > paper_x:
        print("Yes")
    else:
        print("No")

else:
    print("No")

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
brick_x, brick_y, brick_z = 11, 2, 10
brick_x, brick_y, brick_z = 10, 11, 2
brick_x, brick_y, brick_z = 10, 2, 11
brick_x, brick_y, brick_z = 2, 10, 11
brick_x, brick_y, brick_z = 2, 11, 10
brick_x, brick_y, brick_z = 3, 5, 6
brick_x, brick_y, brick_z = 3, 6, 5
brick_x, brick_y, brick_z = 6, 3, 5
brick_x, brick_y, brick_z = 6, 5, 3
brick_x, brick_y, brick_z = 5, 6, 3
brick_x, brick_y, brick_z = 5, 3, 6
brick_x, brick_y, brick_z = 11, 3, 6
brick_x, brick_y, brick_z = 11, 6, 3
brick_x, brick_y, brick_z = 6, 11, 3
brick_x, brick_y, brick_z = 6, 3, 11
brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6

if hole_x > brick_x and hole_y > brick_y and hole_x > brick_z and hole_y > brick_x:
    print("Yes")

if hole_x < brick_x or hole_y < brick_y or hole_x < brick_z or hole_y < brick_x:
    if hole_x > brick_y and hole_y > brick_x and hole_x > brick_z and hole_y > brick_z:
        print("Yes")
    else:
        print("No")