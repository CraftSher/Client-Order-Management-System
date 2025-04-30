user_name = input('Введите имя пользователя: ')
file_name = input('Введите имя файла: ')

path = 'C:/{user}/dogs/folder/{new_file}.txt'.format(
    user=user_name,
    new_file= file_name
    )
path2 = 'C:/{0}/dogs/folder/{1}.txt'.format(
    user_name,
    file_name
    )
path3 = f'C:/{user_name}/dogs/folder/{file_name}.txt'
print('Путь к файлу:', path3)