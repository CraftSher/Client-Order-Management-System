import re

# Ввод текста
text = input('Введите текст: ')

# Приводим текст к нижнему регистру и удаляем все, кроме букв
cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())

# Переворачиваем строку
reverse_text = cleaned_text[::-1]

# Проверка на палиндром
if cleaned_text == reverse_text:
    print('Это палиндром!')
else:
    print('Это не палиндром.')

# Вывод оригинального и перевёрнутого текста для проверки
print(f'Оригинальный текст: {text}')
print(f'Перевернутый текст: {reverse_text}')