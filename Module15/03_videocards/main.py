# TODO здесь писать код


qua_video_cards = int(input('Количество видеокарт: '))
old_num_vc = []
new_num_vc = []


for i in range(qua_video_cards):
    card_number = int(input(f'Видеокарта {i + 1}: '))
    old_num_vc.append(card_number)
# print(old_num_vc)

max_value = max(old_num_vc)
for index in old_num_vc:
    if index < max_value:
        new_num_vc.append(index)
print('Старый список видеокарт:', old_num_vc)
print('Новый список видеокарт:', new_num_vc)

