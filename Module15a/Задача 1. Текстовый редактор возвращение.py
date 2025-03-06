# user_msg = input("Введите строку: ")
# letters = list(user_msg)
# what_replace = ":"
# for_what_replace = ";"
# i = 0
# replace_count = 0
# for letter in letters:
#     if letter == what_replace:
#         letters[i] = for_what_replace
#         replace_count += 1
#     i += 1
#
# print("Исправленная строка:", end=' ')
# for letter in letters:
#     print(letter, end='')
#
# print("\nКол-во замен:", replace_count)

user_msg = input("Введите строку: ")
letters = list(user_msg)
what_replace = ":"
for_what_replace = ";"
for index, letter in enumerate(letters):
    if letter == what_replace:
        letters[index] = for_what_replace

for letter in letters:
    print(letter, end='')




