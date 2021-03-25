import random


class Player:
    def __init__(self, symbol):
        self.name = 'Player' + str(random.randint(1, 100))
        self.symbol = symbol

    def go(self, field, x, y):
        try:
            if(field.cells[x][y] == '*'):
                print('Symbol ', self.symbol, ' is write to ', x, y)
                field.cells[x][y] = self.symbol
                return 1
            else:
                print('Cell is not empty')
                return 0
        except IndexError:
            print('bad index')
            return 0


class Field:
    size = width, height = 3, 3
    def __init__(self):
        # '9' - is empty cell
        self.cells = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        print('Field is created')

    def check_the_winner(self):
        if(self.cells[0][0] == self.cells[0][1] == self.cells[0][2] ):
            if(self.cells[0][0] == 0):
                print('Player with symbol 0 win')
                return [0, [0, 0], [0, 1], [0, 2]]
            elif(self.cells[0][0] == 1):
                print('Player with symbol 1 win')
                return [1, [0, 0], [0, 1], [0, 2]]
            else:
                return [9]
        if (self.cells[1][0] == self.cells[1][1] == self.cells[1][2]):
            if (self.cells[1][0] == 0):
                print('Player with symbol 0 win')
                return [0, [1, 0], [1, 1], [1, 2]]
            elif (self.cells[1][0] == 1):
                print('Player with symbol 1 win')
                return [1, [1, 0], [1, 1], [1, 2]]
            else:
                return [9]
        if (self.cells[2][0] == self.cells[2][1] == self.cells[2][2]):
            if (self.cells[2][0] == 0):
                print('Player with symbol 0 win')
                return [0, [2, 0], [2, 1], [2, 2]]
            elif (self.cells[2][0] == 1):
                print('Player with symbol 1 win')
                return [1, [2, 0], [2, 1], [2, 2]]
            else:
                return [9]
        if (self.cells[0][0] == self.cells[1][0] == self.cells[2][0]):
            if (self.cells[0][0] == 0):
                print('Player with symbol 0 win')
                return [0, [0, 0], [1, 0], [2, 0]]
            elif (self.cells[0][0] == 1):
                print('Player with symbol 1 win')
                return [1, [0, 0], [1, 0], [2, 0]]
            else:
                return [9]
        if (self.cells[0][1] == self.cells[1][1] == self.cells[2][1]):
            if (self.cells[0][1] == 0):
                print('Player with symbol 0 win')
                return [0, [0, 1], [1, 1], [2, 1]]
            elif (self.cells[0][1] == 1):
                print('Player with symbol 1 win')
                return [1, [0, 1], [1, 1], [2, 1]]
            else:
                return [9]
        if (self.cells[0][2] == self.cells[1][2] == self.cells[2][2]):
            if (self.cells[0][2] == 0):
                print('Player with symbol 0 win')
                return [0, [0, 2], [1, 2], [2, 2]]
            elif (self.cells[0][2] == 1):
                print('Player with symbol 1 win')
                return [1, [0, 2], [1, 2], [2, 2]]
            else:
                return [9]
        if (self.cells[0][0] == self.cells[1][1] == self.cells[2][2]):
            if (self.cells[0][0] == 0):
                print('Player with symbol 0 win')
                return [0, [0, 0], [1, 1], [2, 2]]
            elif (self.cells[0][0] == 1):
                print('Player with symbol 1 win')
                return [1, [0, 0], [1, 1], [2, 2]]
            else:
                return [9]
        if (self.cells[2][0] == self.cells[1][1] == self.cells[0][2]):
            if (self.cells[1][1] == 0):
                print('Player with symbol 0 win')
                return [0, [2, 0], [1, 1], [0, 2]]
            elif (self.cells[1][1] == 1):
                print('Player with symbol 1 win')
                return [1, [2, 0], [1, 1], [0, 2]]
            else:
                return [9]
        is_field_full = True
        for row in self.cells:
            for elem in row:
                if(elem == '*'):
                    is_field_full = False
        if is_field_full:
            print('Friendship win')
            return [100]

        return [9]


class GameProcess:
    def __init__(self):
        self.playerA = Player()
        self.playerB = Player()
        self.field = Field()

    def start(self):
        pass
