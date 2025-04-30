phonebook_dict = {
    ('Петров', 'Ваня'): 88006663636,
    ('Егоров', 'Ваня'): 88003333333,
    ('Ульянов', 'Петя'): 88005553535,
    ('Сидорова', 'Лена'): 88007773737
}
phonebook_dict[('Сидорова', 'Алёна')] = 1877680097
for i_person in phonebook_dict:
    if 'Сидорова' in i_person:
        print(i_person[1], phonebook_dict[i_person])

print(phonebook_dict)