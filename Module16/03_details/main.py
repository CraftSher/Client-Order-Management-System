shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

det_name = input('Название детали:')
quantity = 0
total_price = 0

for i_team in shop:
    for i_man in i_team:
        if det_name == i_man:
            quantity += 1
            total_price += i_team[1]
print('Кол-во деталей —', quantity)
print('Общая стоимость —', total_price)

