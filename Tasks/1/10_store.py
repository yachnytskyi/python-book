goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print(lamps_cost)
# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print(f"We have {store[goods['Лампа']][0]['quantity']} lamps in our store. Their general price is {lamps_cost}")

tables_cost_first = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
tables_cost_second = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
tables_cost_general = tables_cost_first + tables_cost_second
print(f"We have {store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']}"
      f" tables in our store. Their general price is {tables_cost_general}")

# sofa 2, chair 3
sofas_cost_first = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofas_cost_second = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofas_cost_general = sofas_cost_first + sofas_cost_second
print(f"We have {store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']}"
      f" sofas in our store. Their general price is {sofas_cost_general}")

chairs_cost_first = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chairs_cost_second = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chairs_cost_third = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
chairs_cost_general = chairs_cost_first + chairs_cost_second + chairs_cost_third
print(f"We have {store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']}"
      f" chairs in our store. Their price is {chairs_cost_general} ")





