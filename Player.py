from User import User


class Player(User):
    def __init__(self):
        super(User).__init__()
        self.set_name()
        self.score = 0

    def set_name(self):
        print("\nТвоё имя? ")
        self.name = input()


def menu():
    print("\n\t1) Игрок Vs. Компьютера"
          "\n\t2) Мультиплеер"
          "\n\t0) Выход")
    print("\n\nВыберите режим: ")
    option = input()

    return option
