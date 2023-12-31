import os
import time
import logging
from prettytable import PrettyTable
from modPick import pick

os.system('color 2')
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


def clear():
    os.system('cls')


data = [
    "блокнот", "C:/Windows/System32/notepad.exe",
    "stalker", "C:/Users/AIS/Desktop/Anomaly Launcher.lnk",
    "hunter", "D:/Games/Silent Hunter 5/sh5.exe",
    "mo2", "F:/Games/MO2/ModOrganizer.exe",
    "total", "D:/totalcmd/TOTALCMD64.EXE",
    "шахматы", "D:/Games/LucasChessR/bin/LucasR.exe",
    "браузер", "C:/Program Files/Mozilla Firefox/firefox.exe",
    "таблица", "no path"
]


def show_table():
    # ТАБЛИЦА
    columns = ["Команда", "Путь"]
    count_col = len(columns)
    table = PrettyTable(columns)
    table.align = "l"
    table.sortby = "Команда"

    td_data = data[:]

    while td_data:
        table.add_row(td_data[:count_col])
        td_data = td_data[count_col:]
    print(table)


title = 'Запуск:'

logging.info("Запуск цикла")
while True:
    clear()
    option, index = pick(data[::2], title, indicator='>', default_index=0)
    userInput = option
    execDone = False

    # ОБРАБОТКА ИНПУТА ОТ ПОЛЬЗОВАТЕЛЯ
    if userInput == "таблица":
        show_table()
        time.sleep(5)
        continue

    for ind, elem in enumerate(data):
        if userInput == elem:
            command = data[ind + 1]
            try:
                os.startfile(command)
                execDone = True
                logging.info("Запуск  " + command)
            except FileNotFoundError:
                logging.info("Ошибка запуска  " + command)
            break

    if execDone:
        print(userInput + " >>> выполнено")
    else:
        print(userInput + " - программа не обнаружена")
    time.sleep(2)
