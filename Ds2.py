from decimal import Decimal

names = ['Семён', 'Иван', 'Дима']
salaries = [14000, 25000, 41000]
bonuses = ['10.25%', '12.50%', '14.45%']

salaries = {elem[0]: elem[1] + elem[1] * Decimal(elem[2].replace('%', '')) / 100
            for elem in zip(names, salaries, bonuses)}

for k, v in salaries.items():
    print(f'{k} => {v}')