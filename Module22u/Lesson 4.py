# speakers_file = open('speakers.txt', 'r', encoding= 'utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end= '')
#     sym_count.append(str(len(i_line)))
# print()
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
# print(sym_count_str)
#=================================================================
# speakers_file = open('speakers.txt', 'r', encoding= 'utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end= '')
#     sym_count.append(str(len(i_line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
# count_file = open('sym_count.txt', 'w')
# count_file.write(sym_count_str)
# count_file.close()
#=================================================================
import os

def find_file(cur_path, file_name):
    print('переходим', cur_path)
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('   смотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('это директория.')
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result

file_path = find_file(os.path.abspath(os.path.join('..', '..', 'PythonProject')), 'Lesson 3.py')
history_file = open('search_history.txt', 'a')
if file_path:
    print('Абсолютный путь к файлу:', file_path)
    history_file.write(file_path)
else:
    print('Файл не найден!!!')
history_file.close()