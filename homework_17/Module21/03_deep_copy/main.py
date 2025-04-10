site = {
    'html': {
       'head': {
          'title': 'Куплю/продам телефон недорого'
       },
       'body': {
          'h2': 'У нас самая низкая цена на iPhone',
          'div': 'Купить',
          'p': 'Продать'
       }
    }
}
def deep_copy(data):
    new_dict={}
    for key, value in data.items():
        if isinstance(value, dict):
            new_dict[key] = deep_copy(value)
        else:
            new_dict[key] = value
    return new_dict

def replace_product_name(new_dict, product_name):
    for key, value in new_dict.items():
        if isinstance(key, str):
            if 'телефон'.lower() in key.lower() or 'iphone'.lower() in key.lower():
                new_key = key.lower().replace('телефон'.lower(), product_name).replace('iphone'.lower(), product_name)
                new_dict[new_key] = new_dict.pop(key)
                key = new_key
        if isinstance(value, str):
            if 'телефон'.lower() in value.lower() or 'iphone'.lower() in value.lower():
                new_dict[key] = value.lower().replace('телефон'.lower(), product_name).replace('iphone'.lower(), product_name)
        elif isinstance(value, dict):
            replace_product_name(value, product_name)

user_answer = int(input('Сколько сайтов: '))
site_list = []

for i in range(user_answer):
    user_product_name = input('Введите название продукта для нового сайта: ')
    copied_site = deep_copy(site)
    replace_product_name(copied_site, user_product_name)
    site_list.append(copied_site)
    print(f'Сайт для {user_product_name}:')
    print(site_list)

