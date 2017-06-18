# следующие характеристики: имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале. 
 

student = [{
		 'Имя': 'Саша',
		 'Фамилия':'Иванов',
		 'Пол':'М',
		 'Опыт(да, нет)':'да',
		 'ДЗ':[2,3,2,6,9],
		 'ЭКЗАМЕН': 10
},
{
		 'Имя': 'Петя',
		 'Фамилия':'Петров',
		 'Пол':'М',
		 'Опыт(да, нет)':'нет',
		 'ДЗ':[2,3,2,6,1],
		 'ЭКЗАМЕН': 5
},
{
		 'Имя': 'Миша',
		 'Фамилия':'Сидоров',
		 'Пол':'М',
		 'Опыт(да, нет)':'да',
		 'ДЗ':[5,6,7,6,1],
		 'ЭКЗАМЕН': 8
},
{
		 'Имя': 'Соня',
		 'Фамилия':'Домова',
		 'Пол':'Ж',
		 'Опыт(да, нет)':'нет',
		 'ДЗ':[1,1,7,1,1],
		 'ЭКЗАМЕН': 3
},
{
		 'Имя': 'Юля',
		 'Фамилия':'Дворова',
		 'Пол':'Ж',
		 'Опыт(да, нет)':'да',
		 'ДЗ':[10,10,10,1,1],
		 'ЭКЗАМЕН': 8
},
{
		 'Имя': 'Оксана',
		 'Фамилия':'Районова',
		 'Пол':'Ж',
		 'Опыт(да, нет)':'нет',
		 'ДЗ':[10,9,10,1,1],
		 'ЭКЗАМЕН': 8
}]


# среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:

#         Средняя оценка за домашние задания по группе: X
#         Средняя оценка за экзамен: Y

# где X и Y - вычисляемые значения;

# среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта в виде:

#         Средняя оценка за домашние задания у мужчин: A
#         Средняя оценка за экзамен у мужчин: B
#         Средняя оценка за домашние задания у женщин: C
#         Средняя оценка за экзамен у женщин: D
        
#         Средняя оценка за домашние задания у студентов с опытом: E
#         Средняя оценка за экзамен у студентов с опытом: F        
#         Средняя оценка за домашние задания у студентов без опыта: G
#         Средняя оценка за экзамен у студентов без опыта: H

# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:

# Лучший студент: S с интегральной оценкой Z

# если студент один или:

# Лучшие студенты: S... с интегральной оценкой Z

# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение. 



def mark_int(student):
	mark_int_list=[]
	for i, n in enumerate(student,start=1):
	 hw_ave = sum(n['ДЗ'])/len(n['ДЗ'])
	 ex = n['ЭКЗАМЕН']
	 b = 0.6*hw_ave+0.4*ex
	 n['Оценка'] = b
	return student
def max_grade (a):
	f = []
	for i, n in enumerate(student,start=1):
	 f.append(n['Оценка'])
	g = max(f)
	return g
def name_l (g):
	name = []
	for n in student:
	 if g == n['Оценка']:
	  name.append(n['Имя']+' '+n['Фамилия'])
	return name

def exp_r():
	exp = []
	for each_student in student:
	 for q in each_student['Опыт(да, нет)']:
	 	if q not in exp:
	 		exp.append(q)
	return exp
def hw_exp_y (exp):
	homework_mark_list =[]
	for each_student in student:
		if exp[0] in each_student['Опыт(да, нет)']:
		 for hw_mark in each_student['ДЗ']:
		  homework_mark_list.append(hw_mark)
	return homework_mark_list
def ex_exp_y (exp):
	exam_mark_list =[]
	for each_student in student:
	 if exp[0] in each_student['Опыт(да, нет)']:
	 	exam_mark_list.append(each_student['ЭКЗАМЕН'])
	return exam_mark_list
def hw_exp_n (exp):
	homework_mark_list =[]
	for each_student in student:
		if exp[1] in each_student['Опыт(да, нет)']:
		 for hw_mark in each_student['ДЗ']:
		  homework_mark_list.append(hw_mark)
	return homework_mark_list
def ex_exp_n (exp):
	exam_mark_list =[]
	for each_student in student:
	 if exp[1] in each_student['Опыт(да, нет)']:
	 	exam_mark_list.append(each_student['ЭКЗАМЕН'])
	return exam_mark_list

def male_hw_list():
	homework_mark_list =[]
	sex = 'М'
	for each_student in student:
	 if sex in each_student['Пол']:
	  for hw_mark in each_student['ДЗ']:
	   homework_mark_list.append(hw_mark)
	return homework_mark_list
def male_ex_list():
	exam_mark_list =[]
	sex = 'М'
	for each_student in student:
	 	if sex in each_student['Пол']:
	 	 exam_mark_list.append(each_student['ЭКЗАМЕН'])
	return exam_mark_list
def female_hw_list():
	homework_mark_list =[]
	sex = 'Ж'
	for each_student in student:
	 if sex in each_student['Пол']:
	  for hw_mark in each_student['ДЗ']:
	   homework_mark_list.append(hw_mark)
	return homework_mark_list
def female_ex_list():
	exam_mark_list =[]
	sex = 'Ж'
	for each_student in student:
	 	if sex in each_student['Пол']:
	 	 exam_mark_list.append(each_student['ЭКЗАМЕН'])
	return exam_mark_list

def hm_list():
	homework_mark_list =[]
	for each_student in student:
		for hw_mark in each_student['ДЗ']:
		  homework_mark_list.append(hw_mark)
	return homework_mark_list
def ex_list():
 exam_mark_list = list()
 for each_student in student:
  exam_mark_list.append(each_student['ЭКЗАМЕН'])
 return exam_mark_list

def average(smth):
	b = len(smth)
	a = sum(smth)
	c = a/b
	return c

def main_input ():
 comm = input('Введете команду (q,w,e,r):')
 return comm
def main ():
	while True:
		c = main_input()
		check_list = ['q','w','e','r']
		if c in check_list:
			if c == 'q':
				smth = ex_list()
				c = average(smth)
				print('Средняя оценка за домашние задания по группе:', round(c,1))
				smth = hm_list()
				c = average(smth)
				print('Средняя оценка за экзамен:', round(c,1))
				c = main_input()
			elif c == 'w':
				smth = male_hw_list()
				c = average(smth)
				print('Средняя оценка за домашние задания у мужчин:', round(c,1))
				smth = male_ex_list()
				c = average(smth)
				print('Средняя оценка за экзамен у мужчин:', round(c,1))
				smth = female_hw_list()
				c = average(smth)
				print('Средняя оценка за домашние задания у женщин:', round(c,1))
				smth = female_ex_list()
				c = average(smth)
				print('Средняя оценка за экзамен у женщин:', round(c,1))
			elif c == 'e':
				exp = exp_r()
				smth = hw_exp_y(exp)
				c = average(smth)
				print('Средняя оценка за домашние задания у студентов с опытом:', round(c,1))
				smth = ex_exp_y(exp)
				c = average(smth)
				print('Средняя оценка за экзамен у студентов с опытом:', round(c,1))
				smth = hw_exp_n(exp)
				c = average(smth)
				print('Средняя оценка за домашние задания у студентов без опыта:', round(c,1))
				smth = ex_exp_n(exp)
				c = average(smth)
				print('Средняя оценка за экзамен у студентов без опыта:', round(c,1))
			elif c == 'r':
				mark_int(student)
				g = max_grade(student)
				name = name_l(g)
				if len(name) == 1:
					print('Лучший студент: {} с интегральной оценкой {}'.format(' '.join(name),g))
				else:
					print('Лучшие студенты: {} с интегральной оценкой {}'.format(', '.join(name) ,g))
		else:
			break
main()
