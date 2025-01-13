class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                 print(f'{self.name} съел {food.name}')
                 self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{self.name} не  растение,{food.name} не  съедобно.')
            



class Plant:
    def __init__(self, name, edible= False):
        self.edible = edible
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, False)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим имя хищника
print(a1.name)
# Выводим название цветка
print(p1.name)
# Выводим живой ли хищник
print(a1.alive)
# Выводим сытый ли млекопитающее
print(a2.fed)
# Хищник пробует съесть цветок
a1.eat(p1)
# Млекопитающее пробует съесть фрукт
a2.eat(p2)
# Выводим живой ли хищник после поедания не съедобного растения
print(a1.alive)
# Выводим сытое ли млекопитающее после фрукта
print(a2.fed)