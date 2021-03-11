import random


class Field:
    size = width, height = 3, 3
    def __init__(self):
        # '9' - is empty cell
        # second comment
        # toghe comment
        cells = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]



class Player:
    def __init__(self, symbol):
        self.name = 'Player' + str(random.randint(1, 100))
        self.symbol = symbol


class GameProcess:
    pass
