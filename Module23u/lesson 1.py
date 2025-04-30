import collections
import zipfile

def unzip(archive):
    try:
        zfile = zipfile.ZipFile(archive, 'r')
        for i_file_name in zfile.namelist():
            zfile.extract(i_file_name)
    except zipfile.BadZipFile:
        print(f"Ошибка: Файл '{archive}' не является корректным zip-архивом.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{archive}' не найден.")
    finally:
        if 'zfile' in locals() and zfile:
            zfile.close()

def collect_stats(file_name):
    result = {}
    extracted_file_name = 'voyna_i_mir.txt'  # Предполагаемое имя текстового файла после распаковки
    if file_name.endswith('.zip'):
        unzip(file_name)
    try:
        with open(extracted_file_name, 'r', encoding='utf-8') as text_file:
            for i_line in text_file:
                for j_chair in i_line:
                    if j_chair.isalpha():
                        if j_chair not in result:
                            result[j_chair] = 0
                        result[j_chair] += 1
    except FileNotFoundError:
        print(f"Ошибка: Не найден файл '{extracted_file_name}' после распаковки.")
        return {}
    return result
def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))

def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse= True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict

file_name = 'voyna_i_mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)