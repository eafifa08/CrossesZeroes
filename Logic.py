import random


class Player:
    def __init__(self, symbol):
        self.name = 'Player' + str(random.randint(1, 100))
        self.symbol = symbol

    def go(self, field, x, y):
        try:
            if(field.cells[x][y] == 9):
                print('Empty cell')
                return 1
        except IndexError:
            print('bad index')
            return 0


class Field:
    size = width, height = 3, 3
    def __init__(self):
        # '9' - is empty cell
        self.cells = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        print('Field is created')

    def check_the_end(self):
        return False



class GameProcess:
    def __init__(self):
        self.playerA = Player()
        self.playerB = Player()
        self.field = Field()

    def start(self):
        pass