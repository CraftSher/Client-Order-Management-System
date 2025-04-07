# TODO здесь писать код
def str_tpl(line, num_tuple):
    return ((sym, num) for sym, num in zip(line, num_tuple))

def my_zip(*iterables):
    return (item for item in zip(*iterables))

line = 'abcd'
num_tuple = (10, 20, 30, 40)
result = str_tpl(line, num_tuple)
for item in result:
    print(item)

list1 = [1, 2, 3]
str1 = 'abc'
tuple1 = (10, 20, 30)
set1 = {100, 200, 300}
result1 = my_zip(list1, str1, tuple1, set1)
for item in result1:
    print(item)

