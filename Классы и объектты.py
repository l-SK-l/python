class Things: #Определяем класс
    pass

class Inanimate (Things): #Потомок класса Things
    pass

class Animate (Things):
    pass

class Sidewalks (Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_uoung_with_milk(self):
        print('кормит детенышей молоком')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')
    def find_food(self):
        self.move()
        print('Я нашёл еду')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

    

reginald = Giraffes() #создать объект класса Giraffes и присвоить его переменной reginald.
harold = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold.move()
harold.dance_a_jig()



class ThisIsMySillyClass: #несколько функций, принадлежащих классу
    def this_is_a_class_function():
        print('Я – функция класса')
    def this_is_also_a_class_function():
        print('Я тоже функция класса, понятно?')

