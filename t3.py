usr = input(str('введите номер месяца'))

time = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима'
}

for x in time:
    if usr == x: u = time.get(x)
print(u)