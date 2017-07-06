# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_132_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import glob
import os.path

def file_glob():

	migrations = 'Migrations'
	file_path = os.path.abspath(os.path.dirname(__file__))
	files = glob.glob(os.path.join(file_path, migrations, "*.sql"))
	return files

def serch_fun(files,serch_item):
	files_next = []
	for file in files:
		with open (file) as file_for_read:
			obj_for_serch_item = file_for_read.read()
		if serch_item in obj_for_serch_item:
			files_next.append(file)
			print(file)
	return files_next 

def main_input(files):
	serch_item = input('Введите слово для поиска, Владыка: ')
	files_next = serch_fun(files,serch_item)
	print('Всего: ', len(files_next))
	return files_next 

def main():
	while True:
		files = file_glob()
		files = main_input(files)
		one = len(files)
		if one <= 1:
			print('Мы достигли дна, Владыка!')
			choise = str(input('Повторить поиск сначала?(Y , N): '))
			if choise != 'N':
				files = file_glob()
			else:
				break

main()