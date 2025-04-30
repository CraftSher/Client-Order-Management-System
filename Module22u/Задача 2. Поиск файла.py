import os
path_dir = input('Укажите абсолютный путь или директорию: ')
file_name = input('Укажите имя файла: ')
find_path = []
for root, dirs, files in os.walk(path_dir):
    for file_names in files:
        if file_names == file_name:
            full_path = os.path.join(root, file_names)
            find_path.append(full_path)
if find_path:
    print("Найдены следующие пути:")
    for path in find_path:
        print(path)
else:
    print("Файлы не найдены.")

# def find_file(cur_path, file_name):
#     print("Запуск поиска в папке", os.path.join(os.path.abspath(cur_path)))
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print("Проверяется путь", path)
#         if file_name == i_elem:
#             print(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#     return result
# find_file('..', 'Lesson 1.py')
