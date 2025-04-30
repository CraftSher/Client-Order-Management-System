# import os
#
# def print_dirs(project):
#     print('n\Содержимое директории', project)
#     if os.path.exists(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('    ', path)
#     else:
#         print('Каталога проекта не существует!!!')
# projects_list = ['PythonProject', 'Python_Basic', 'Prod']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)
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

file_path = find_file(os.path.abspath
                      (os.path.join('..', '..', 'PythonProject')),
                      'Lesson 2.py')
if file_path:
    print('Абсолютный путь к файлу:', file_path)
else:
    print('Файл не найден!!!')