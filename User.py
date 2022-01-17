from Cube import Cube


class User(object):
    def __init__(self):
        self.name = "Компьютер"
        self.score = 0

    def update_score(self, i):
        self.score = self.score + Cube.values[i]

    def show_score(self):
        print(f"{self.name} Ваш счёт равен: {self.score} ")

    def choose_cube(self):
        print("Пожалуйста, введите букву вашего куба: ")
        cube = input().upper()
        chosen = Cube.check_if_already_chosen(Cube(), cube)
        while chosen is True:
            print("Этот куб уже был выбран. Пожалуйста, выберите другой вариант:")
            cube = input().upper()
            chosen = Cube.check_if_already_chosen(Cube(), cube)
        for i in range(8):
            if cube == Cube().suits[i]:
                self.update_score(i)
                Cube.show_value(Cube(), i, self.name)
                self.show_score()

    def check_winner(self, other_score):
        if self.score > other_score:
            print(f"\nПОЗДРАВЛЯЮ {self.name} вы победили!")
        elif self.score < other_score:
            print(f"\nИзвините, {self.name} вы проиграли. Удачи в следующий раз!")
        else:
            print(f"\nЕсть ничья. Вы оба выиграли!")