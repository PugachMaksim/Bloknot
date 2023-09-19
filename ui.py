import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n"
          "1 - вывод всех заметок из файла\n"
          "2 - добавление заметки\n"
          "3 - удаление заметки\n"
          "4 - редактирование заметки\n"
          "5 - выборка заметок по дате\n"
          "6 - показать заметку по id\n"
          "7 - выход\n"
          "\n"
          "Введите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbuy():
    print("До новых встреч!")