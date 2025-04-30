# Открываем файл для записи ('w' — write)
with open('мой_файл.txt', 'w', encoding='utf-8') as file:
    file.write("Привет, это мой первый сохранённый текст!")