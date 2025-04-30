# import requests
# # Отправляем GET-запрос на сайт
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
#
# # Проверяем, успешен ли запрос
# if response.status_code == 200:
#     print("Запрос успешен!")
#     # Выводим данные (в формате JSON)
#     print(response.json())
# else:
#     print(f"Ошибка: {response.status_code}")


import requests
# Данные, которые мы хотим отправить на сервер
new_post = {
    'title': 'New Post Title',
    'body': 'This is the body of the new post.',
    'userId': 1
}

# Отправляем POST-запрос на сайт с данными
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

# Проверяем, успешен ли запрос
if response.status_code == 201:
    print("Пост успешно создан!")
    # Выводим данные (в формате JSON)
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")