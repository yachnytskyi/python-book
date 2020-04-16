# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Please enter a number of the month ")
month = int(user_input)
print('You entered', month)

if user_input == '1':
    print(f"In January we have 31 days")

if user_input == '2':
    print(f"In February we have 28 days")

if user_input == '3':
    print(f"In March we have 31 days")

if user_input == '4':
    print(f"In April we have 30 days")

if user_input == '5':
    print(f"In May we have 31 days")

if user_input == '6':
    print(f"In June we have 31 days")

if user_input == '7':
    print(f"In July we have 31 days")

if user_input == '8':
    print(f"In August we have 30 days")

if user_input == '9':
    print(f"In September we have 31 days")

if user_input == '10':
    print(f"In October we have 30 days")

if user_input == '11':
    print(f"In November we have 31 days")

if user_input == '12':
    print(f"In December we have 31 days")

else:
    print("Unknown error")








