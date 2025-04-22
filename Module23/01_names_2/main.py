sym_count = 0
line_count = 1

try:
    with open('people.txt', 'r', encoding='utf-8') as file:
        for i_line in file:
            cleaned_line = i_line.strip()
            lenght = len(cleaned_line)
            if lenght < 3:
                print('Длина {} строки меньше 3 символов!!!'.format(line_count))
                with open('errors.log', 'w', encoding='utf-8') as error_file:
                    error_file.write(f'Ошибка: менее трёх символов в строке {line_count}. Строка: "{i_line.strip()}"\n')
            sym_count += lenght
            line_count += 1

except FileNotFoundError:
    print('Файл не найден!!!')
except Exception as e:
    print(f'Произошла непредвиденная ошибка: {e}') # Лучше обрабатывать более общие исключения в конце
finally:
    print('Общее количество символов:', sym_count)