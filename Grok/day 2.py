name = input('Как тебя зовут? ')
age = int(input('Сколько тебе лет? '))
if age >= 18:
    print(name, 'ты можешь работать.')
elif age < 16:
    print(name, 'ты ещё учишься.')
else:
    print(name, 'ты ещё молод!')