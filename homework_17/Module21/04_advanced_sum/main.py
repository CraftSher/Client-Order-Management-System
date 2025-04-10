# TODO здесь писать кoд
def sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += sum(*arg)
        elif isinstance(arg, (int, float)):
            total += arg

    return total

num = ([[1, 2, [3]], [1], 3])
result = sum(*num)
print('Ответ в консоли:', result)