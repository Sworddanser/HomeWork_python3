def get_default_cook_book():
  cook_book = {
      'яйчница': [
        {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
      'стейк': [
        {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
      'салат': [
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        ]
      }
  return cook_book

def upload_cook_book():
  cook_book = {}
  with open('test.txt') as f:  # вызыаем фаил
    for line in f: 
      dish_name = line.strip()    
      cook_book[dish_name] = []
      ing_amount = int(f.readline())
      for line in range(ing_amount):
        ingridient = f.readline().strip()
        ingridient = ingridient.split(' | ')
        ing_list = {}
        ing_list['ingridient_name'] = ingridient[0]
        ing_list['quantity'] = int(ingridient[1])
        ing_list['measure'] = ingridient[2]
        cook_book[dish_name].append(ing_list)  
  return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  ans = input('Загрузить книгу рецептов(да,нет):')
  if ans == 'да':    
    cook_book = upload_cook_book()
  elif ans == 'нет':
    cook_book = get_default_cook_book()
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)

create_shop_list()

###############################################
# w={}
# k=[]
# ing_list = []
# v = []
# ing_amount = [] # перечень ингридиентов и блюд
# e = {} # словарь с новыми блюдами и ингридиентами
# dish_menu = [] # значения из файла по блюдам
# with open('test.txt') as f:  # вызыаем фаил
#   for number,line in enumerate(f): 

#    dish = line.split()
#    for i in dish:
#     cook_book[i] = None
#    print(line)
#    sec_line = int(f.readline())


#    for line in range(sec_line):
#       ingridient = f.readline()
#       ingridient = ingridient.split(' | ')
#    # for 
#       w['ingridient_name'] = ingridient[0]
#       w['quantity'] = int(ingridient[1])
#       w['measure'] = ingridient[2]
      
#       v.append(w) 
#       print(line,ingridient)
# # print(v)
#   # print(w)
#     # ing_list.append(ingridient.split(' | '))

#   # cook_book[dish] = None
# for ingridient2 in cook_book.values():
#   print(type(ingridient2))

#    for i in dish:
#     ing_amount.append(i)
# print(ing_amount)
# for i in ing_amount:
#   if '|' in i:
#     ing_amount.remove('|')
# print(ing_amount)


# def zzz():# функция информацию, кидает в список, каждый элемент списка содержит информацию по одному блюду.
#   qwe = 2 + int(ing_amount[1])*3
#   dish_menu.append(ing_amount[0:qwe])
#   while qwe < len(ing_amount):
#     qqq = qwe
#     qwe = qqq + 2 + int(ing_amount[1 + qqq])*3
#     dish_menu.append(ing_amount[qqq:qwe])
#     print(dish_menu)
#   return dish_menu  
# dish_menu = zzz()




# ##### дальше хотел переработать список ингридиентов в dish_menu, планировал сплитом убрать разделители, 
# #затем первый элемент(название блюда) воткнуть на ключ словаря, а списки ингридиентов как список словарей с игридиентами
# # Однако упорно не могу сделать так, что бы в список к попал вложенный список словарей - инридиентов
# k = []
# # w = {}
# print(dish_menu)
# for z in dish_menu:
#   del z[1]  # Удаляем ненужное количество игридиентов
#   e[z[0]] = None # сюда будет подставлено знание списка k


# print (k)
















# ##### дальше хотел переработать список ингридиентов в dish_menu, планировал сплитом убрать разделители, 
# #затем первый элемент(название блюда) воткнуть на ключ словаря, а списки ингридиентов как список словарей с игридиентами
# # Однако упорно не могу сделать так, что бы в список к попал вложенный список словарей - инридиентов
# k = []
# w = {}
# print(dish_menu)
# for z in dish_menu:
#   del z[1]  # Удаляем ненужное количество игридиентов
#   e[z[0]] = None # сюда будет подставлено знание списка k

#   for i,n in enumerate(z):
#       n = n.split(' | ')  
#   w['ingridient_name'] = n[0]
#   w['quantity'] = n[1]
#   w['measure'] = n[2]
#   k.append(w) 
# print (k)


      



