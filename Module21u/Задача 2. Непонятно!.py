data_input = {"a": 10, "b": 20}


if type(data_input) in (str, tuple, int, float, bool):
    print("Неизменяемый (immutable)")
elif type(data_input) in (list, dict, set):
    print("Изменяемый (mutable)")
else:
    print("Тип данных не определён")

print(f'Тип данных: {type(data_input)} (строка)')
print(f'id объекта: {id(data_input)}')