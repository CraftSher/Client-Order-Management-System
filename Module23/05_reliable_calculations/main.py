import math

def calculate_square_root(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Введенное значение не является числом")
    if number < 0:
        raise ValueError("Невозможно вычислить квадратный корень отрицательного числа")
    else:
        return math.sqrt(number)

def process_numbers(numbers):
    results = []
    for number in numbers:
        try:
            sqrt_result = calculate_square_root(number)
            results.append(f"Квадратный корень из {number}: {sqrt_result}")
        except (ValueError, TypeError) as e:
            results.append(f"Ошибка для {number}: {e}")
        except Exception as exc:
            results.append(f"Непредвиденная ошибка для {number}: {exc}")
    return results

numbers = [16, 25, -9, 0, 4.5, "abc"]
results = process_numbers(numbers)
for result in results:
    print(result)