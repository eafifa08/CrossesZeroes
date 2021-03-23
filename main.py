import Logic
import pygame
import sys

pygame.init()
pygame.display.set_caption('Crosses & NuLLs')

color_grey = (100, 100, 100)
color_red = (250, 0, 0)

screen = pygame.display.set_mode((310, 310))

r = pygame.Rect(5, 5, 300, 300)
pygame.draw.rect(screen, color_grey, r, 0)
line = pygame.draw.line(screen, color_red, [105, 5], [105, 305])
line = pygame.draw.line(screen, color_red, [205, 5], [205, 305])
line = pygame.draw.line(screen, color_red, [5, 105], [305, 105])
line = pygame.draw.line(screen, color_red, [5, 205], [305, 205])
font = pygame.font.SysFont('couriernew', 20)
text = font.render(str('HELLO'), True, pygame.color.THECOLORS['green'])
screen.blit(text, (50, 50))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('pressed', pygame.mouse.get_pos())
            pygame.draw.circle(screen, color_red, pygame.mouse.get_pos(), 2, 2)

            pygame.display.flip()


player_A = Logic.Player(0)
print('created', player_A.name, 'with symbol ', player_A.symbol)
player_B = Logic.Player(1)
print('created', player_B.name, 'with symbol ', player_B.symbol)
field = Logic.Field()
# is_the_end=9 - Победителя нет, есть свободные клетки
# is_the_end=0 - Победитель с символом 0
# is_the_end=1 - Победитель с символом 1
# is_the_end=100 - Победителя нет, свободных клеток нет
is_the_end = 9
while(is_the_end == 9):
    player_A.go(field, int(input('Player_A input x=')), int(input('Player_A input y=')))
    print(field.cells[0])
    print(field.cells[1])
    print(field.cells[2])
    is_the_end = field.check_the_winner()
    if(is_the_end == 9):
        player_B.go(field, int(input('Player_B input x=')), int(input('Player_B input y=')))
        print(field.cells[0])
        print(field.cells[1])
        print(field.cells[2])
    is_the_end = field.check_the_winner()

