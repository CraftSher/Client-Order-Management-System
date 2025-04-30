alphabet = 'abcdefghijklmnopqrstuvwxyz'
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
try:
    with open('ages.txt', 'r', encoding='utf-8') as file_ages:
        data = file_ages.readlines()
        ages = []
        for line in data:
            line = int(line.strip())
            ages.append(line)
    with open('result.txt', 'x', encoding='utf-8') as file_result:
        for name, age in zip(names, ages):
            file_result.write(f"{name} - {age}\n")

except (ValueError, IsADirectoryError):
    print("Ошибка: неверный тип данных.")
except FileExistsError:
    print("Ошибка: файл уже существует.")




