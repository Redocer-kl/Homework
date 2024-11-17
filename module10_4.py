import threading
import random
import time
import queue
class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe():
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            got_table = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"Гость {guest.name} занял столик {table.number}")
                    got_table = True
                    break
            if not got_table:
                self.queue.put(guest)
                print(f"Гость {guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал и ушел")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                     next_guest = self.queue.get()
                     table.guest = next_guest
                     next_guest.start()
                     print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
