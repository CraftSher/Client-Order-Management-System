# TODO переписать программу OK

violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56],
    ['Halo', 4.9], ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29], ['Clean', 5.83]]
time_total = 0

quantity = int(input('Сколько песен выбрать? '))

for i in range(quantity):
    print(f'Название {i + 1}-й песни: ')
    song = input('')
    for track in violator_songs:
        if song == track[0]:
            time_total += track[1]
print('Общее время звучания песен:', round(time_total, 2), 'минут')
