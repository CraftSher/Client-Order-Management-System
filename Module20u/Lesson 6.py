# names = ['Tom', 'Bob', 'Albert']
# ages = [20, 45, 70]
# people = dict(zip(names, ages))
# print(people)
# for i_person in people:
#     print(i_person)
# people2 ={i_name: i_age + 20 for i_name, i_age in zip(names, ages)}
# print(people2)

list = [1, 2, 3] # Есть неизменяемый объект (кстати, попробуйте потом повторить этот код с изменяемым объектом)
hash_value = hash(tuple) # Применим к этому объекту функцию hash
print(hash_value) # Проверим, что получилось (бессмысленный набор чисел)
hash_value_2 = hash(tuple) # Попробуем ещё раз
print(hash_value_2) # Опять набор чисел
print(hash_value == hash_value_2) # И он в точности равен первому