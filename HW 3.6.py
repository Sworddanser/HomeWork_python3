
# Добрый день.
#
# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи
# Утки, куры, гуси
# Условия:
#
# 1. Должен быть один базовый класс, который наследуют все остальные животные.
#
# 2. Базовый класс должен определять общие характеристики и интерфейс.

class Farm_animals:
    owner = 'me'
    food = None
    current_population = 0
    max_population = 500 #heads

    def __init__(self, population, food):
        self.current_population = population
        self.food = food

    def count(self):
        if self.current_population > self.max_population:
            print('перебор, продавай живность')
        else:
            print('Влезаем')


class Cows(Farm_animals):
    food = 'grass'


class Sheeps(Farm_animals):
    food = 'grass'


class Goats(Farm_animals):
    food = 'grass'


class Pigs(Farm_animals):
    food = 'all'

# Ducks, chickens, geese


Ducks = type('Ducks', (Farm_animals,), {'food': 'Sunflower seeds'})
Chickens = type('Chickens', (Farm_animals,), {'food': 'Sunflower seeds'})
Geese = type('Geese', (Farm_animals,), {'food': 'Oats'})

pupa = Cows(100, 'Grass')
print(pupa.count())# не совсем понимаю откуда взялся None, вродебы он сидит в самом count, но не вижу его

tom = Geese(501,'Oats')
print(tom.count())
print(tom.food)

print('Тут мы видим, что для Йорика, неободимо задать количество голов и еду, т.е. наследование работает')
yorik = Ducks()

