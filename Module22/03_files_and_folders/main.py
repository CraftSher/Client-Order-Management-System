import os
def count_item(folder):
    catalog_weight = 0
    folder_count = 0
    file_count = 0
    for i_elem in os.listdir(folder):
        path = os.path.join(folder, i_elem)
        if os.path.isfile(path):
            file_count += 1
            catalog_weight += os.path.getsize(path)
        elif os.path.isdir(path):
            sub_weight, sub_folder_count, sub_file_count = count_item(path)
            catalog_weight += sub_weight
            folder_count += 1 + sub_folder_count
            file_count += sub_file_count
    return catalog_weight, folder_count, file_count

folder_path = input('Введите путь: ')
result = count_item(folder_path)
weight, fcount, ficount =result
weight_kb = round(weight / 1024,2)
print(f'Размер каталога (в Кб): {weight_kb} \nКоличество подкаталогов: {fcount} \nКоличество файлов: {ficount}')

