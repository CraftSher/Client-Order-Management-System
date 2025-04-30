class SmallNumberError(Exception):
    pass

try:
    with open('numbers.txt', 'r', encoding='utf-8') as numbers:
        for line in numbers:
            # Удаляем лишние пробелы в начале и конце строки и разделяем по пробелу (или другому разделителю в твоем файле)
            parts = line.strip().split()
            if len(parts) == 2:
                try:
                    num1 = float(parts[0])
                    num2 = float(parts[1])
                    if num1 < num2:
                        raise SmallNumberError('Первое число меньше чем второе!!!')
                    else:
                        result = num1 / num2
                        print(f'{num1} / {num2} = {result}')
                except ValueError:
                    print(f'Ошибка: Некорректный формат чисел в строке: {line.strip()}')
                except SmallNumberError as e:
                    print(f'Ошибка: {e}')
            else:
                print(f'Ошибка: Некорректный формат строки с числами: {line.strip()}')
except FileNotFoundError:
    print('Ошибка: Файл numbers.txt не найден.')
except Exception as e:
    print(f'Произошла непредвиденная ошибка: {e}')
