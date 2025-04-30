sym_sum = 0
line_count = 0
try:
    people_file = open('people.txt', 'r')
    for i_line in people_file:
        length = len(i_line)
        line_count += 1
        if i_line.endswith('\n'):
            length -= 1
        if length < 4:
            raise BaseException('Длина {} строки меньше 4 символов!!!'.format(line_count))
        sym_sum += length
    people_file.close()
except FileNotFoundError:
    print('Файл не найден!!!')

finally:
    print('Найденная сумма символов:', sym_sum)

# names = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#             raise BaseException('Ты сломал программу!!!')
#         if not name.isalpha():
#             raise TypeError
#         names.append(name)
#         if len(names) == 5:
#             print('Место закончилось!!!')
#             break
#
#     except TypeError:
#         print('Ты чего ввёл???')
#     except BaseException:
#         names = []
#         print('Введено стоп-слово.')
#         raise ValueError('Пожалуйста не вводите стоп-слово.')
# names_file = open('names.txt', 'w')
# names_file.write('\n'.join(names))
# names_file.close()
# print('Программа завершена. Запись законченна.')