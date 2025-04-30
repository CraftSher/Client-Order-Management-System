import datetime

palindrome_count = 0

try:
    with open('words.txt', 'r', encoding='utf-8') as words_file:
        for line in words_file:
            word = line.strip()
            try:
                # Попытка преобразовать в число
                int(word)
                # Если получилось, значит это число, вызываем ошибку
                raise ValueError(f"В строке найдено число: {word}")
            except ValueError as ve:
                # Обработка ошибки ValueError (если это число) или
                # если это слово и преобразование не удалось
                if "В строке найдено число" in str(ve):
                    # Логируем ошибку в errors.log
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open('errors.log', 'a', encoding='utf-8') as log_file:
                        log_file.write(f"[{timestamp}] - ValueError: {ve}\n")
                else:
                    # Проверка на палиндром (если это не число)
                    processed_word = word.lower()
                    if processed_word == processed_word[::-1]:
                        palindrome_count += 1
except FileNotFoundError:
    print("Файл words.txt не найден.")
except Exception as e:
    print(f"Произошла неожиданная ошибка при чтении файла: {e}")
finally:
    print(f"Найдено палиндромов: {palindrome_count}")