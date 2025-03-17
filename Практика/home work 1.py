def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Повышение на первый год: '))
second_percent = int(input('Повышение на второй год: '))

prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]

print('Сумма цен за каждый год:', sum(prices_now), sum(prices_first), sum(prices_second))
