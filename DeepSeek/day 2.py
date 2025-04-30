import os
from datetime import datetime

while True:
    try:
        num1 = input("Введите первое число (или 'выход' для завершения): ")
        if num1.lower() == 'выход':
            break

        num1 = float(num1)
        num2 = float(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, *, /, **) или команду (очистить/статистика/последняя): ")

        # Обработка команд
        if operation.lower() == "очистить":
            if os.path.exists('история.txt'):
                os.remove('история.txt')
                print("История очищена!")
            else:
                print("Файл истории не найден.")
            continue

        if operation.lower() == "статистика":
            if os.path.exists('история.txt'):
                with open('история.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    print(f"Всего операций: {len(lines)}")
            else:
                print("История пуста.")
            continue

        if operation.lower() == 'последняя':
            if os.path.exists('история.txt'):
                with open('история.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    if lines:
                        print(f"Последняя операция: {lines[-1].strip()}")
                    else:
                        print("История пуста.")
            else:
                print("История пуста.")
            continue

        # Вычисления
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if operation == "+":
            result = num1 + num2
            formula = f"[{timestamp}] {num1} + {num2} = {result}"
        elif operation == "-":
            result = num1 - num2
            formula = f"[{timestamp}] {num1} - {num2} = {result}"
        elif operation == "*":
            result = num1 * num2
            formula = f"[{timestamp}] {num1} * {num2} = {result}"
        elif operation == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = round(num1 / num2, 2)
            formula = f"[{timestamp}] {num1} / {num2} = {result}"
        elif operation == '**':
            try:
                result = round(num1 ** num2, 3)
                formula = f'[{timestamp}] {num1} ^ {num2} = {result}'
            except OverflowError:
                print("Ошибка: слишком большой результат!")
                continue
        else:
            print("Ошибка: неизвестная операция!")
            continue

        print(formula.split('] ')[1])  # Выводим без временной метки
        with open('история.txt', 'a', encoding='utf-8') as file:
            file.write(formula + "\n")

    except ValueError:
        print("Ошибка: введите число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Показываем историю при завершении
if os.path.exists('история.txt'):
    print("\nФинальная история операций:")
    with open('история.txt', 'r', encoding='utf-8') as file:
        print(file.read())