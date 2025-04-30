# def format_menu(menu_string):
#     """Форматирует строку меню в список блюд с заглавными буквами."""
#
#     dishes = menu_string.split(';')
#     formatted_dishes = [dish.strip().capitalize() for dish in dishes]
#     return ', '.join(formatted_dishes)
#
# # Пример использования
# menu_input = input('')  # Получаем строку меню от пользователя
# formatted_menu = format_menu(menu_input)
# print(formatted_menu)

# def nice_view(text):
#     text = ", ".join(text.split(';'))
#     return text.title()
# site_menu = input('Введите доступное меню: ')
# print('Доступное меню:', site_menu)
# print('На данный момент в меню есть:', nice_view(site_menu))



def nice_view(text):
    text = ', '.join(text.split(';'))
    return text.title()


dish = input('Введите доступное меню: ')
print('Доступное меню:', dish)
print('На данный момент в меню есть:', nice_view(dish))