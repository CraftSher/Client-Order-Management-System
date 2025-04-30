server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

# for key1, value1 in server_data.items():
#     print(key1)
#     if isinstance(value1, dict):
#         for key2, value2 in value1.items():
#             print('      ', key2, ':', value2)

for key, value in server_data.items():
    print(key)
    for j_key, j_value in value.items():
        print('      ',j_key, ':', j_value)