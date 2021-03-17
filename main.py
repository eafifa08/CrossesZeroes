import Logic
player_A = Logic.Player(0)
print('created', player_A.name, 'with symbol ', player_A.symbol)
player_B = Logic.Player(1)
print('created', player_B.name, 'with symbol ', player_B.symbol)
field = Logic.Field()

is_the_end = False
while(not is_the_end):
    is_the_end = field.check_the_end()
    player_A.go(field, int(input('Player_A input x=')), int(input('Player_A input y=')))
    print(field.cells[0])
    print(field.cells[1])
    print(field.cells[2])
    player_B.go(field, int(input('Player_B input x=')), int(input('Player_B input y=')))
    print(field.cells[0])
    print(field.cells[1])
    print(field.cells[2])
