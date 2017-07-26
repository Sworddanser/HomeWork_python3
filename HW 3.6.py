
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


class Farm:
    food = None
    food_kg = 200
    owner = 'me'
    current_population = 0
    max_population = 500 #heads
    food_need = 0

    def __init__(self, population, food_need):
        self.current_population = population
        self.food_need = food_need

    def __name__(self):
        pass

    def brekfast(self, food_need):
        self.food_kg -= food_need
        print('Поели:', food_need, ', осталось:', self.food_kg)

    def count(self,population):
        self.current_population += population
        if self.current_population > self.max_population:
            print('перебор, продавай живность')


class Cows(Farm):
    food = 'grass'


class Sheeps(Farm):
    food = 'grass'


class Goats(Farm):
    food = 'grass'


class Pigs(Farm):
    food = 'all'

# Ducks, chickens, geese

class Type(type):
    pass

Ducks = Type('Ducks', (Farm,), {})
Chickens = Type('Ducks', (Farm,), {})
Geese = Type('Ducks', (Farm,), {})

duck = Ducks(20, 100)


print(duck.food, duck.__name__(), duck.owner, duck.current_population, duck.max_population, duck.food_need)
duck.brekfast(40)
duck.count(50)
print(duck.food, duck.food_kg, duck.owner, duck.current_population, duck.max_population, duck.food_need)

cow = Cows(1000,1000)
print(cow.food, cow.food_kg, cow.owner, cow.current_population, cow.max_population, cow.food_need)

cow.brekfast(1000000)

cow.count(2000)

print(cow.food, cow.food_kg, cow.owner, cow.current_population, cow.max_population, cow.food_need)