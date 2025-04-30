small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}
big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
print('Товары малого склада:', small_storage)
print('Товары большого склада:', big_storage)
big_storage.update(small_storage)
print('Объединенные товары:', big_storage)
good = (input('Введите наименование товара: ')).lower()
print(f'Товар {good} в количестве: {big_storage.get(good)}')