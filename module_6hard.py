import math

class Figure:
    def __init__(self, color, sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        f = True
        for i in args:
            if i < 0 or not(isinstance(int)):
                f = False
        return f and len(args) == len(self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_slides):
        if len(new_slides) == self.sides_count:
            self.__sides = list(new_slides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides[:1])
        self.__radius = super().get_sides()[0] / (math.pi * 2)

    def get_square(self):
        return self.__radius ** 2 * math.pi

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)
    def get_square(self):
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        p = (self.__len__())/2
        return p * (p - a) * (p - b) * (p - c)

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, sides * 12 )

    def get_volume(self):
        return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((111, 12, 123), 12,  21, 41)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())