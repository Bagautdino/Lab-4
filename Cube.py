from random import randint


class Cube(object):
    suits = ["", "", "", "", "", "", "", ""]
    values = [0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.endgame_points = 0

    def fill_suits(self):
        su = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.suits[i] = su[i]

    def fill_values(self):
        for i in range(8):
            self.values[i] = randint(1, 10)

    def show_cubes(self):
        for i in range(8):
            print(f"[{self.suits[i]}]", end="")

    def show_value(self, i, name):
        print(f"{name} выявил куб [{self.suits[i]}] со значением {self.values[i]}")
        self.suits[i] = str(self.values[i])

    def update_endgame_points(self):
        self.endgame_points = self.endgame_points + 1

    def check_if_already_chosen(self, cube):
        chosen = True
        for i in range(8):
            if cube == self.suits[i] and cube != str(self.values[i]):
                chosen = False
                break
            elif cube == self.suits[i] and cube == str(self.values[i]):
                chosen = True
                break
            else:
                chosen = True

        return chosen







