# def factorial(num):
#     if num == 1:
#         return 1
#     fact_n_minus_1 = factorial(num - 1)
#     return num * fact_n_minus_1
#
#
#
#
# num_fact = factorial(5)
# print(num_fact)

site = {
    'html':{
        'head':{
            'tittle': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def find_key(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Какой ключ ищем? ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа в структуре сайта нет.')
