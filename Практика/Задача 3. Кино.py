films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня', 'Проклятый остров', 'Начало', 'Матрица']

film_quantity = int(input('Сколько фильмов выбрать? '))
your_films = []

for i in range(film_quantity):
    print("Ваш текущий топ фильмов:", your_films)
    film_name = input("Имя фильма: ")
    print("Команды: добавить, вставить, удалить")
    command = input("Введите команду: ")
    if film_name not in your_films:
        if command == "добавить":
            your_films.append(film_name)
        elif command == 'вставить':
            insert_index = int(input('Введите индекс для вставки: '))
            insert_index %= len(your_films)
            your_films.insert(insert_index, film_name)
    else:
        if command == 'удалить':
            your_films.remove(film_name)
        elif command == 'добавить' or command == 'вставить':
            print('Этот фильм уже есть в вашем списке.')
print('Ваш текущий топ фильмов:', your_films)

