documents = [
        {"type": "passport", 
         "number": "2207 876234", 
         "name": "Василий Гупкин"},

        {"type": "invoice", 
         "number": "11-2", 
         "name": "Геннадий Покемонов"},

        {"type": "insurance", 
         "number": "10006", 
         "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

    # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    # m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

def del_numb_input():
 del_number = str(input('Введите команду номер документа для удаления:'))
 return del_number

def new_shelf_add(directories):
  new_shelf_enter = str(input('Введите № новой полки :'))

  other = [new_shelf_enter, None]
  if other[0] in directories.keys():
   print('Такой номер полки существует')
  if other[0] not in directories.keys():
   directories.update([other])
   print (directories)
  return directories

def transport (directories):
  numb_new_shelf = str(input('Введите номер документа :'))
  shelf_new = str(input('Введите № полки :'))

  for i,n in directories.items():
    if numb_new_shelf in n:
     n.remove(numb_new_shelf)
    if shelf_new == i:
     n.append(numb_new_shelf)
    if shelf_new != i:
     print('Нет нужной полки, создайте ее')
  return directories

def doc_del(del_number3):
 del_number2 = del_number3
 for i,n in enumerate(documents):
   if del_number2 in n['number']:
    documents.pop(i)
 return documents

def shelf_num_del(del_number3):
 del_number2 = del_number3
 for i,n in directories.items():
  if del_number2 in n:
   n.remove(del_number2)
 return directories

def get_name(documents):
 num_doc = str(input('Введите номер документа:'))
 peop_name = []
 for inv in documents:
  for key,eim in inv.items():
   if num_doc in eim:
    peop_name.append(inv["name"])
 return peop_name

def get_all(documents):
 all_data = []
 for inv in documents:
  for key,eim in inv.items():
   all_data.append(str(eim))
 return all_data

def get_shelf(directories):
 num_doc_shelf = str(input('Введите номер документа, чтобы найти полку:'))
 shelf_numb = []
 for key_sh,eim_sh in directories.items():
  if num_doc_shelf in eim_sh:
   shelf_numb.append(key_sh)
 return shelf_numb

def new_count(documents):
  tnn_new = {
           "type": 1,
           "number":2, 
           "name": 3
           }
  type_new = str(input('Введите тип докуммента:'))
  tnn_new['type'] = type_new
  num_new = str(input('Введите номер документа:'))
  tnn_new['number'] = num_new
  name_new = str(input('Введитеде имя:'))
  tnn_new['name'] = name_new
  documents.append(tnn_new)
  return documents

def new_shelf(directories):
  num_last = documents[-1]['number']
  num_self_new = str(input('Введите номер полки:'))
  for i, o in directories.items():
   if i == num_self_new:
    o.append(num_last)
    directories[i] = o
  return directories

def main_input():
 comm = str(input('Введите команду(p,l,s,a,d,m,as):'))
 return comm

def main_low():
 
 while True:
  chek_list = ['p','l','s','a','d','m','as']
  c = main_input()
  c in chek_list == True
  if c == chek_list[0]:
   human_name = get_name(documents)
   print('Имя человека по данному документу:', human_name)
  elif c == chek_list[1]:
   all_data2 = get_all(documents)
   print(all_data2)
  elif c == chek_list[2]:
   shelf = get_shelf(directories)
   print (str(shelf))
  elif c == chek_list[3]:
   new_count(documents)
   print(documents)
   new_shelf(directories)
   print(directories)
  elif c == chek_list[4]:
   del_number3 = del_numb_input()
   doc_del(del_number3)
   shelf_num_del(del_number3)
   print(documents)
   print(directories)
  elif c == chek_list[5]:
   transport(directories)
   print(directories)
  elif c == chek_list[6]:
   new_shelf_add(directories)
   print(directories)
  else:
   exit()

main_low()





#  