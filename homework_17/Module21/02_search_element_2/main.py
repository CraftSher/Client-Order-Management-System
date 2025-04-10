# TODO здесь писать код
def find_key(data, key, depth=None):
    if isinstance(data, dict):
        for current_key, value in data.items():
            if current_key == key:
                return value
            if isinstance(value, dict):
                if depth is None or depth > 1:
                    result = find_key(value, key, depth - 1 if depth is not None else None)
                    if result is not None:
                        return result
        return None
    return None

site = {
    'html': {
       'head': {
          'title': 'Мой сайт'
       },
       'body': {
          'h2': 'Здесь будет мой заголовок',
          'div': 'Тут, наверное, какой-то блок',
          'p': 'А вот здесь новый абзац'
       }
    }
}

search_key = input('Введите искомый ключ: ').lower()
max_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if max_depth == 'y':
    max_depth_value = int(input('Введите максимальную глубину: '))
    depth = max_depth_value
else:
    depth = None

value = find_key(site, search_key, depth)
if value:
    print(value)
else:
    print(None)