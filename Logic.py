import random


class Player:
    def __init__(self, symbol):
        self.name = 'Player' + str(random.randint(1, 100))
        self.symbol = symbol


class Field:
    size = width, height = 3, 3
    def __init__(self):
        # '9' - is empty cell
        cells = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]


class GameProcess:
    def __init__(self):
        self.playerA = Player()
        self.playerB = Player()
        self.field = Field()


    def start(self):
        pass



