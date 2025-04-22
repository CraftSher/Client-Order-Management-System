def validate_data(line):
    cleaned_line = line.strip()
    parts = cleaned_line.split(' ')
    if len(parts) != 3:
        raise IndexError
    if not parts[0].isalpha():
        raise NameError
    if '@' not in parts[1] or '.' not in parts[1]:
        raise SyntaxError
    try:
        age = int(parts[2])
        if not 10 <= age <= 99:
            raise ValueError("Поле «Возраст» не является числом от 10 до 99")
    except ValueError:
        raise ValueError("Поле «Возраст» не является числом")

def main():
    good_log_filename = "registrations_good.log"
    bad_log_filename = "registrations_bad.log"
    input_filename = "registrations.txt"

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(good_log_filename, 'w', encoding='utf-8') as outfile_good, \
             open(bad_log_filename, 'w', encoding='utf-8') as outfile_bad:
            for line in infile:
                line = line.strip()
                try:
                    validate_data(line)
                    outfile_good.write(line + '\n')
                except IndexError:
                    outfile_bad.write(f"{line}\tНЕ присутствуют все три поля\n")
                except NameError:
                    outfile_bad.write(f"{line}\tПоле «Имя» содержит НЕ только буквы\n")
                except SyntaxError:
                    outfile_bad.write(f"{line}\tПоле «Имейл» НЕ содержит @ и . (точку)\n")
                except ValueError as e:
                    if "invalid literal for int()" in str(e):
                        outfile_bad.write(f"{line}\tПоле «Возраст» НЕ является числом\n")
                    else:
                        outfile_bad.write(f"{line}\tПоле «Возраст» НЕ является числом от 10 до 99\n")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
