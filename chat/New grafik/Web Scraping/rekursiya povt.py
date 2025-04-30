def print_text(data):
    result = []
    if isinstance(data, str):
        result.append(data)
    elif isinstance(data, dict):
        for value in data.values():
            result.extend(print_text(value))
    elif isinstance(data, list):
        for item in data:
            result.extend(print_text(item))
    else:
        print('Текст не найден!!!')
    return result

data = [
    "Привет",
    {"a": "Мир", "b": ["Как", {"c": "дела?"}]},
    ["Все", {"d": "хорошо", "e": ["спасибо", {"f": "тебе"}]}]
]

report = print_text(data)
for text in report:
    print(text)