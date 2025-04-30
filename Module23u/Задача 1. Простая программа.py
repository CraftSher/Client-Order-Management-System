file_name = input('Введите имя файла: ')
line = input('Введите текст: ')
file = None

try:
    file = open(file_name, 'w', encoding= 'utf-8')
    file.write(line)
    file.close()
except (IOError, FileNotFoundError, PermissionError):
    print('Проблема при открытии файла.')
except ValueError:
    print('Нельзя преобразовать данные в целое.')
except  Exception as e:
    print('Неожиданная ошибка.')
else:
    print('Программа выполнилась без ошибок.')
finally:
    if file is not None:  # Проверяем, что файл был открыт
        file.close()
        print(f'Файл закрыт: {file.closed}')
    else:
        print('Файл не был открыт, поэтому закрытие не требуется.')