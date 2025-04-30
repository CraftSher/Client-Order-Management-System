def filter_data(data):
    new_data = []

    # Фильтруем IP-адреса
    for item in data:
        ip_address = item[0]
        ip_parts = ip_address.split('.')
        if len(ip_parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
            new_data.append([ip_address, []])  # Добавляем IP с пустым списком файлов

    symbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')

    # Фильтруем файлы
    for item in data:
        ip_address = item[0]
        file_list = item[1][0].split(' ')  # Разделяем строку файлов по пробелу

        for file in file_list:
            if not file.startswith(symbols) and (file.endswith('.txt') or file.endswith('.docx')):
                for entry in new_data:
                    if entry[0] == ip_address:
                        entry[1].append(file)

    return new_data


# Исходные данные
data = [
    ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
    ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
    ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
    ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
    ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
    ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
    ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
]

# Вызов функции и вывод результата
filtered_data = filter_data(data)
print('Новая структура данных:', filtered_data)