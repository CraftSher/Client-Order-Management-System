def clean_json(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            if "удалить" in key or "delete" in key:
                continue
            cleaned_value = clean_json(value)
            if cleaned_value is not None and cleaned_value is not False and cleaned_value != [] and cleaned_value != {}:
                new_dict[key] = cleaned_value
        return new_dict if new_dict else None  # Возвращаем словарь или None, если он пуст после очистки
    elif isinstance(data, list):
        new_list = []
        for item in data:
            cleaned_item = clean_json(item)
            if cleaned_item is not None and cleaned_item is not False and cleaned_item != [] and cleaned_item != {}:
                new_list.append(cleaned_item)
        return new_list if new_list else None  # Возвращаем список или None, если он пуст
    elif data is None or data is False or data == "" or data == [] or data == {}:
        return None  # Удаляем None и False
    else:
        return data  # Возвращаем остальные типы данных без изменений




data = {
    "a": 1,
    "удалить": "это надо удалить",
    "b": {
        "delete": True,
        "c": 10,
        "d": [None, 0, {"x": "", "y": []}]
    },
    "e": False,
    "f": "",
    "g": [],
    "h": {},
    "i": {"j": "оставить", "k": False}
}

cleaned_data = clean_json(data)
print(cleaned_data)