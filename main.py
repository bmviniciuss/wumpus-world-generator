from Game import Game


def main():
    size  = int(input("Board size: "))
    game = Game(size)
    game.printBoard()


if __name__ == '__main__':
    main()
