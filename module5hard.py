import time


class User:
    """
    Конструктор User с атрибутами nick, password, age
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return  self.nickname

class Video:
    """
    Конструктор Video с атрибутами title, duration, time_now, adult_mode
    """
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    """
    Конструктор с атрибутами users, videos, current_user
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    """
    Метод log_in для входа пользователя
    """
    def log_in(self, nickname, password):
        f = True
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f"Добрый день, {nickname}!")
                f = False
                break
            elif nickname == user.nickname:
                print("Неверный пароль")
                f = False
                break
        if f:
            print("Такой пользователь не найден")

    """
    Метод для регистрации пользователя
    """
    def register(self, nickname, password, age):
        f = False
        for user in self.users:
            if user.nickname == nickname:
                f = True
                break
        if f:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
            print("Успешная регестрация, добро пожаловать!")

    """
    Метод для выхода из профиля
    """
    def log_out(self):
        print(f"Вы вышли из профиля {self.current_user.nickname}")
        self.current_user = None

    def add(self, *args):
        for video in args:
            f = True
            for old_video in self.videos:
                if old_video.title == video.title:
                    f = False
            if f:
                print(f"Видео {video.title} успешно загружено" )
                self.videos.append(video)
            else:
                print("Видео с таким названием уже существует :(")

    """
    Метод для поиска видео
    """
    def get_videos(self, search):
        result = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                result.append(video)
        if len(result) == 0:
            print(f"Поиск {search} не выдал результатов")
        else:
            print(f"Результаты поиска {search}:")
            for video in result:
                print(video.title)
    """
    Метод просмотра видео
    """
    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        f = False
        watching_vid = None
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    f = True
                    break
                f = True
                watching_vid = video
                break
        if f and watching_vid != None:
             print("Начался просмотр видео")

             while watching_vid.duration + 1 > watching_vid.time_now :
                print(f"{watching_vid.time_now} секунда видео")
                time.sleep(1)
                watching_vid.time_now += 1
             watching_vid.time_now = 0
             print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')