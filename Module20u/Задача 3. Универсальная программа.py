import ast
def get_even_indexed_elements(iterable):
    if isinstance(iterable, dict):
        iterable = iterable.values()
    results = []
    for index, element in enumerate(iterable):
        if index % 2 == 0:
            results.append(element)
    return results

print(get_even_indexed_elements('О Дивный Новый мир!'))
print(get_even_indexed_elements([100, 200, 300, 'буква', 0, 2, 'а']))
print(get_even_indexed_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))