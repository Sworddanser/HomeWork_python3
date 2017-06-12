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


def get_name(documents):
 num_doc = str(input('Введите номер документа:'))
 peop_name = []
 for inv in documents:
  for key,eim in inv.items():
   if num_doc in eim:
    peop_name.append(inv['name'])
 return peop_name

def get_all(documents):
 all_data = []
 for inv in documents:
  for key,eim in inv.items():
   all_data.append(eim)
 return all_data

def main_input():
 comm = str(input('Введите команду(p,l,s,a):'))
 return comm

def main_low():
 
 while True:
  chek_list = ['p','l','s','a']
  c = main_input()
  c in chek_list == True
  
  if c == 'p':
   first_resp_name = get_name(documents)
   print('Имя человека поданному документу:', first_resp_name)
  elif c =='l':
   all_data2 = get_all(documents)
   print (str(all_data2))
  else:
  	exit()

main_low()

#  