# OrganizerAndStarter
# Для работы через IDE (PyCharm) необходимо включить эмуляцию терминала в конфиге проекта

from modPick import pick
import datetime
import os
import csv
import time

os.system('color 6')

clear = lambda: os.system('cls')


def show_pick(title, options, index):
    return pick(options, title, indicator='>', default_index=index)


fileName = 'YourTasks.csv'
mine_title = 'Главное меню:'
tasks_str = "Задачи"
idea_str = "Идеи"
notes_str = "Заметки"
back_str = "Назад"
create_str = "Создать"
remove_str = "Удалить"
save_str = "Сохранить"
cancel_str = "Отмена"
exit_str = "Выход"

mine_options = [tasks_str, idea_str, notes_str, save_str, exit_str]  # пункты - Главное меню
base_second_menu = [remove_str, create_str, back_str]  # пункты - Второстепенное меню

dict_type = {tasks_str: [], idea_str: [], notes_str: []}


def fnc_exit():
    print("Завершение работы")
    time.sleep(1)
    exit()


def fnc_back():
    _index = mine_options.index(title)
    _title = mine_title
    _options = mine_options
    return _title, _options, _index


def fnc_tasks():
    _title = tasks_str
    _options = dict_type[_title]
    _index = 0
    return _title, _options, _index


def fnc_idea():
    _title = idea_str
    _options = dict_type[_title]
    _index = 0
    return _title, _options, _index


def fnc_notes():
    _title = notes_str
    _options = dict_type[_title]
    _index = 0
    return _title, _options, _index


def fnc_create():
    _title = title
    _options = dict_type[_title]
    _index = base_second_menu.index(option)
    user_input = input("создание " + _title + "\n>>> ")
    if user_input != "":
        current_date = datetime.datetime.now()
        _options.append(current_date.strftime("%Y-%m-%d %H:%M") + " - " + user_input)
    return _title, _options, _index


def fnc_remove():
    _title = title
    _options = dict_type[_title]
    _index = base_second_menu[::-1].index(remove_str)
    try:
        #  Отмена удаляет сама себя, затем добавляется снова
        selected, ind = pick([cancel_str] + dict_type[title][3:], remove_str, indicator='->', default_index=0)
        dict_type[title].remove(selected)
    except:
        print("error")
    return _title, _options, _index


def fnc_save():
    _title = mine_title
    _options = mine_options
    _index = mine_options.index(save_str)

    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([
            [tasks_str] + dict_type[tasks_str][3:],
            [idea_str] + dict_type[idea_str][3:],
            [notes_str] + dict_type[notes_str][3:]
        ])
    print("Сохранено успешно!")
    time.sleep(1)
    return _title, _options, _index


#  Создание и обработка файла базы данных
file = open(fileName, 'a')
file.close()
with open(fileName, 'r') as f:
    for row in csv.reader(f):
        dict_type[row[0]] = row[1:]

#  Добавление пунктов Второстепенного меню к спискам
for list in [dict_type[tasks_str], dict_type[idea_str], dict_type[notes_str]]:
    for item in base_second_menu:
        list.insert(0, item)

# активация Стартовое меню
title = mine_title
options = mine_options

index = 0
while 1:
    clear()
    option, currentInd = show_pick(title, options, index)  # Вывод меню на экран

    title, options, index = {
        exit_str: fnc_exit,
        tasks_str: fnc_tasks,
        idea_str: fnc_idea,
        notes_str: fnc_notes,
        back_str: fnc_back,
        create_str: fnc_create,
        remove_str: fnc_remove,
        save_str: fnc_save
    }.get(option)()
