# from pick import pick
from modPick import pick
import datetime
import os
from os.path import abspath
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

mine_options = [tasks_str, idea_str, notes_str, save_str] #  пункты - Главное меню
base_second_menu = [remove_str, create_str, back_str] #  пункты - Второстепенное меню

dict_type = {}
dict_type[tasks_str] = []
dict_type[idea_str] = []
dict_type[notes_str] = []


#  Создание и обработка файла базы данных
file = open(fileName,'a')
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
	option, index = show_pick(title, options, index) #  Вывод меню на экран
	
	#  Обработка событий
	if option == tasks_str:
		title = tasks_str
		options = dict_type[tasks_str]
		index = 0
		continue

	elif option == idea_str:
		title = idea_str
		options = dict_type[idea_str]
		index = 0
		continue

	elif option == notes_str:
		title = notes_str
		options = dict_type[notes_str]
		index = 0
		continue

	elif option == back_str:
		index = mine_options.index(title)
		title = mine_title
		options = mine_options
		continue
		
	elif option == create_str:
		user_input = input("создание " + title + "\n>>> ")
		if user_input == "":
			continue
		current_date = datetime.datetime.now()
		dict_type[title].append(current_date.strftime("%Y-%m-%d %H:%M") + " - " + user_input)
		continue
		
	elif option == remove_str:
		try:
			#  Отмена удаляет сама себя, затем добавляется снова
			selected, ind = pick([cancel_str] + dict_type[title][3:], remove_str, indicator='->', default_index=0)
			dict_type[title].remove(selected)
		except:
			print("error")
		continue
	
	elif option == save_str:
		with open(fileName, 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerows([
				[tasks_str] + dict_type[tasks_str][3:],
				[idea_str] + dict_type[idea_str][3:],
				[notes_str] + dict_type[notes_str][3:]
			])
		print("Сохранено успешно!")
		time.sleep(1)
	
	time.sleep(1)























