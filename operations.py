import Note
import file_RW
import ui

number = 10 #Длина заметки


def add():
    note = ui.create_note(number)
    array = file_RW.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_RW.write_fie(array, 'a')
    print('Заметка добавлена!!!')

def show(text):
    flag = True
    array = file_RW.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            flag = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            flag = False
            print("ID: " + Note.Note.get_id(notes))
        if text == 'date':
            flag = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if flag == True:
        print('Заметок нет')

def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = file_RW.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if flag == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')

    file_RW.write_fie(array, 'a')