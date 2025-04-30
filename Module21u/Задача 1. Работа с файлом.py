
def checker(question,
            error_message="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.",
            count_of_errors=3):
    while count_of_errors:
        user_input = input(question)
        if user_input.lower() == "да":
            return 1
        elif user_input.lower() == "нет":
            return 0
        else:
            print(error_message)
        count_of_errors -= 1
        print("Осталось попыток:", count_of_errors)


checker("да?")
checker("да?", "ДА ил НЕТ?!")
checker("да?", count_of_errors=3)
