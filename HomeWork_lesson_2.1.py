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


# def get_shop_list_by_dishes(dishes, person_count):
#   shop_list = {}
#   for dish in dishes:
#     for ingridient in cook_book[dish]:
#       new_shop_list_item = dict(ingridient)

#       new_shop_list_item['quantity'] *= person_count
#       if new_shop_list_item['ingridient_name'] not in shop_list:
#         shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#       else:
#         shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
#   return shop_list

# def print_shop_list(shop_list):
#   for shop_list_item in shop_list.values():
#     print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
#                             shop_list_item['measure']))

# def create_shop_list():
#   person_count = int(input('Введите количество человек: '))
#   dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#     .lower().split(', ')
#   shop_list = get_shop_list_by_dishes(dishes, person_count)
#   print_shop_list(shop_list)

# create_shop_list()

###############################################
ing_amount = [] # перечень ингридиентов и блюд
e = {} # словарь с новыми блюдами и ингридиентами
dish_menu = [] # значения из файла по блюдам
with open('test.txt') as f:  # вызыаем фаил
  for line,text in enumerate(f):    
    print(line,text)
    if text == int():
      print(text)

def zzz():# функция информацию, кидает в список, каждый элемент списка содержит информацию по одному блюду.
  qwe = 2 + int(ing_amount[1])
  dish_menu.append(ing_amount[0:qwe])
  while qwe < len(ing_amount):
    qqq = qwe
    qwe = qqq + 2 + int(ing_amount[1 + qqq])
    dish_menu.append(ing_amount[qqq:qwe])
  return dish_menu  
dish_menu = zzz()



##### дальше хотел переработать список ингридиентов в dish_menu, планировал сплитом убрать разделители, 
#затем первый элемент(название блюда) воткнуть на ключ словаря, а списки ингридиентов как список словарей с игридиентами
# Однако упорно не могу сделать так, что бы в список к попал вложенный список словарей - инридиентов
k = []
w = {}
print(dish_menu)
for z in dish_menu:
  del z[1]  # Удаляем ненужное количество игридиентов
  e[z[0]] = None # сюда будет подставлено знание списка k

  for i,n in enumerate(z):
      n = n.split(' | ')  
  w['ingridient_name'] = n[0]
  w['quantity'] = n[1]
  w['measure'] = n[2]
  k.append(w) 
print (k)


      



