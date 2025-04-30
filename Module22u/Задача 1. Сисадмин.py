import os

file_name = 'admin.bat'
folder_name = 'sher'
real_path = os.path.join('docs', folder_name, file_name)
abs_path = os.path.abspath(file_name)
print('Абсолютный путь до файла:', abs_path)
print('Относительный путь до файла:', real_path)