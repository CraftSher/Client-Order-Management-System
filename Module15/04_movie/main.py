films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_movies = []

add_movies = int(input('Сколько фильмов хотите добавить? '))

for _ in range(add_movies):
    movie_title = input('Введите название фильма: ')
    if movie_title in films:
        favorite_movies.append(movie_title)
    else:
        print('Ошибка: фильма', movie_title, 'у нас нет :(')
print()
print('Ваш список любимых фильмов:', ', '.join(favorite_movies))
