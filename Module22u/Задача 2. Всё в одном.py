import os

def print_dirs_and_copy_code(folder):
    # Открываем файл для записи
    with open('scripts.txt', 'w', encoding='utf-8') as output_file:
        print('\nСодержимое папки:', folder)
        for i_elem in os.listdir(folder):
            path = os.path.join(folder, i_elem)
            if os.path.isfile(path):
                if i_elem.endswith('.py'):
                    # Открываем файл .py для чтения
                    with open(path, 'r', encoding='utf-8') as file:
                        code = file.read()
                        # Записываем содержимое в 'scripts.txt'
                        output_file.write(code + '\n')
                        output_file.write('*' * 40 + '\n')  # Разделитель

folder_path = r'/Module22u'  # Путь к твоей папке
print_dirs_and_copy_code(folder_path)