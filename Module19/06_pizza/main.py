quantity = int(input('Введите количество заказов: '))
total_order = {}

for i in range(quantity):
    order = input(f'{i + 1} заказ: ')
    words = order.split()
    client_name = words[0]
    pizza_name = words[1]
    pizz_quan = int(words[2])
    if not client_name in total_order:
        total_order[client_name] = {pizza_name: pizz_quan}
    else:
        if pizza_name in total_order[client_name]:
            total_order[client_name][pizza_name] += pizz_quan
        else:
            total_order[client_name][pizza_name] = pizz_quan

for client in sorted(total_order):
    print(f'{client}:')
    for pizza in sorted(total_order[client]):
        print(f'     {pizza}: {total_order[client][pizza]}')
