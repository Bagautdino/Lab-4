from Player import Player
from Player import menu
import time
from Cube import Cube
from Cpu import Cpu


class Main(object):
    @staticmethod
    def run():
        opt = ""
        while opt != "0":
            cubes1 = Cube()
            opt = menu()
            if opt == "1":
                print("\n\n[  Игрок    V S.   Компьютера  ]")
                cubes1.fill_suits()
                cubes1.fill_values()
                player = Player()
                cpu = Cpu()
                while cubes1.endgame_points < 8:
                    time.sleep(2)
                    cubes1.show_cubes()
                    print(f"\n\n{player.name} теперь твоя очередь...")
                    player.choose_cube()
                    cubes1.update_endgame_points()

                    time.sleep(4)
                    cubes1.show_cubes()
                    print("\n\nТеперь очередь Компьютера...")
                    cpu.choose_cube()
                    cubes1.update_endgame_points()

                print("\nОкончательный счет: "
                      f"\n{player.name}: {player.score}"
                      f"\n{cpu.name}: {cpu.score}")
                player.check_winner(cpu.score)
                input()
            elif opt == "2":
                print("\n\n[  Мультиплеер  ]")
                cubes1.fill_suits()
                cubes1.fill_values()
                player1 = Player()
                player2 = Player()
                while cubes1.endgame_points < 8:
                    time.sleep(2)
                    cubes1.show_cubes()
                    print(f"\n\n{player1.name} теперь твоя очередь...")
                    player1.choose_cube()
                    cubes1.update_endgame_points()

                    time.sleep(2)
                    cubes1.show_cubes()
                    print(f"\n\n{player2.name} теперь твоя очередь...")
                    player2.choose_cube()
                    cubes1.update_endgame_points()

                print("\nОкончательный счет: "
                      f"\n{player1.name}: {player1.score}"
                      f"\n{player2.name}: {player2.score}")
                player1.check_winner(player2.score)
                player2.check_winner(player1.score)
                input()


if __name__ == '__main__':
    Main().run()
