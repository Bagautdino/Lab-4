from User import User
from Cube import Cube
from random import randint


class Cpu(User):
    def __init__(self):
        super(User).__init__()
        self.__name = "Компьютер"
        self.score = 0

    def show_score(self):
        print(f"Счёт компьютера равен: {self.score}")

    def choose_cube(self):
        cube = Cube().suits[randint(0, 7)]
        chosen = Cube.check_if_already_chosen(Cube(), cube)
        while chosen is True:
            cube = Cube.suits[randint(0, 7)]
            chosen = Cube.check_if_already_chosen(Cube(), cube)
        for i in range(8):
            if cube == Cube().suits[i]:
                self.update_score(i)
                Cube.show_value(Cube(), i, self.__name)
                self.show_score()