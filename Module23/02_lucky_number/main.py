import random

def main():
    total_sum = 0
    output_filename = "out_file.txt"
    unlucky_number = 6
    while True:
        try:
            num = int(input('Введите число: '))
            random_number = random.randint(1, 13)
            if random_number == unlucky_number:
                raise Exception("Вас постигла неудача!")
                break
            else:
                with open('out_file.txt', 'a', encoding='utf-8') as out_file:
                    out_file.write(str(num)+ '\n')
                    total_sum += num
                    if total_sum >= 777:
                        print("Вы успешно выполнили условие для выхода из порочного цикла!")
                        break
        except ValueError as e:
            print("Ошибка: Введите целое число.")
        except Exception as e:
            print(e)  # Вывод сообщения о неудаче
            break

if __name__ == "__main__":
    main()





