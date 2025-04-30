def shift_detection(first_text, second_text):
    first_text *= 2
    index = first_text.find(second_text)

    if index != -1:
        result = f"Первая строка получается из второй со сдвигом {index}"
    else:
        result = "Первую строку нельзя получить из второй с помощью циклического сдвига."
    return result
first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
print(shift_detection(first_text, second_text))
