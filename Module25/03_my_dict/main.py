class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, key, default=0):
        # Вызываем метод get() родительского класса (dict)
        value = super().get(key, default)
        # Проверяем, вернул ли родительский get() значение по умолчанию (None, если не был передан default)
        # TODO данная конструкция лишняя, возвращайте сразу value
        if value is None and default == 0:
            return 0
        else:
            return value


my_dict = MyDict({'a': 1, 'b': 2})

print(my_dict.get('a'))      # Выведет: 1
print(my_dict.get('c'))      # Выведет: 0 (вместо None)
print(my_dict.get('c', 5))   # Выведет: 5 (пользователь передал значение default)
print(my_dict.get('b', 0))   # Выведет: 2 (ключ найден, значение default игнорируется)
print(my_dict['a'])          # Работает как обычный словарь: 1

empty_dict = MyDict()
print(empty_dict.get('key')) # Выведет: 0
