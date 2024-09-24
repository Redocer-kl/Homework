class _Vehicle():
    __color_variants = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, power, color):
        self.owner = owner
        self.__model = model
        self.__enjine_power = power
        self.__color = color

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Модель: {self.__enjine_power}")

    def get_color(self):
        print(f"Модель: {self.__color}")

    def print_info(self):
        print(f"Владелец: {self.owner}")
        self.get_model()
        self.get_horsepower()
        self.get_color()

    def set_color(self, new_color):
        if  self.__color_variants.count(new_color.lower()):
            print(f"Цвет поменян на {new_color}")
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(_Vehicle):
    pass

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
