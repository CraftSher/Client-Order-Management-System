import os
path = input('Укажите абсолютный путь или директорию: ')

if os.path.exists(path):
    if os.path.isfile(path):
        print('это файл.')
        size = os.path.getsize(path)
        print(f"Размер файла: {size} байт")
    elif os.path.isdir(path):
        print('Это директория.')
    elif os.path.islink(path):
        print("Это ссылка")
else:
    print('Указанного пути не существует!!!')
