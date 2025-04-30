path = input("Путь к файлу: ")
disk = input("На каком диске должен лежать файл: ")
extension = input("Требуемое расширение файла: ")

if path.startswith(disk) and path.endswith(extension):
    print("Путь корректен!")
else:
    print("Путь некорректен!")