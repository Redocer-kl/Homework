class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        else:
            raise TypeError("Нельзя сравнить")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        else:
            raise TypeError("Нельзя сравнить")

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        else:
            raise TypeError("Нельзя сравнить")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        else:
            raise TypeError("Нельзя сравнить")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        else:
            raise TypeError("Нельзя сравнить")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        else:
            raise TypeError("Нельзя сравнить")

    def __add__(self, value):
        self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__