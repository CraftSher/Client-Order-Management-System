guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
len(guests)


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    question = input('Гость пришёл или ушёл? ')
    if question == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print('Привет', name, '!')
            print()
        else:
            print('Прости,', name, 'но мест нет.')
            print()
    elif question == 'ушёл':
        name = input('Имя гостя: ')
        if name in guests:
            print('Пока', name, '!')
            guests.remove(name)
        else:
            print('Гостя по имени', name, 'здесь нет')
        print()
    elif question == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        print()
        break
