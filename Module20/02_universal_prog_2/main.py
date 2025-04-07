# TODO здесь писать код
object = ('О Дивный Новый мир!')

def is_prime(item):
    if item < 2:
        return False
    elif item == 2:
        return True
    for i in range(2, int(item ** 0.5) + 1):
        if item % i == 0:
            return False
    return True

def crypto(object):
    if isinstance(object, (list, str, tuple, set)):
        new_list = [element for index, element in enumerate(object) if is_prime(index)]
        return new_list
    elif isinstance(object, dict):
        new_list = [value for index, value in enumerate(object.values()) if is_prime(index)]
        return new_list
    else:
        print('Введите корректные данные!!!')

new_list = crypto(object)


print(f'Ответ в консоли: {new_list}')