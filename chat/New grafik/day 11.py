from tabulate import tabulate

def analyze_json(data, counts=None, depth=0, seen_strings=None):
    if counts is None:
        counts = {'num': 0, 'str': 0, 'lst': 0, 'dct': 0, 'max_depth': 0, 'null': 0, 'bool': 0}
    if seen_strings is None:
        seen_strings = set()

    counts['max_depth'] = max(counts['max_depth'], depth)
    if isinstance(data, dict):
        counts['dct'] += 1
        for value in data.values():
            analyze_json(value, counts, depth + 1, seen_strings)
    elif isinstance(data,list):
        counts['lst'] += 1
        for item in data:
            analyze_json(item, counts, depth + 1, seen_strings)
    elif isinstance(data, str):
        counts['str'] += 1
        if data not in seen_strings:
            seen_strings.add(data)
    elif isinstance(data, (int, float)):
        counts['num'] += 1
    elif data is None:
        counts['null'] += 1
    elif isinstance(data, bool):
        counts['bool'] += 1
    return counts

data = {
    "a": 1,
    "b": {
        "c": "hello",
        "d": [None, 3, {"x": "world", "y": [4, 5]}]
    },
    "e": [False, 10],
    "f": None
}
result = analyze_json(data)
print(tabulate(result.items(), headers=['ТИП','КОЛИЧЕСТВО']))







