import Logic
import pygame
import sys

player_A = Logic.Player(0)
print('created', player_A.name, 'with symbol ', player_A.symbol)
player_B = Logic.Player(1)
print('created', player_B.name, 'with symbol ', player_B.symbol)
field = Logic.Field()

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
font = pygame.font.SysFont('couriernew', 30)
text_0 = font.render(str('0'), True, pygame.color.THECOLORS['green'])
text_x = font.render(str('x'), True, pygame.color.THECOLORS['blue'])
#screen.blit(text, (50, 50))

pygame.display.flip()
# is_the_end=9 - Победителя нет, есть свободные клетки
# is_the_end=0 - Победитель с символом 0
# is_the_end=1 - Победитель с символом 1
# is_the_end=100 - Победителя нет, свободных клеток нет
is_the_end = 9
who_is_go = 0
while(is_the_end == 9):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            print('pressed', mouse_position)
            if(who_is_go % 2 == 0):
                #pygame.draw.circle(screen, color_red, mouse_position, 2, 2)
                print('Player_A go to ', int((mouse_position[0]-5)//100), int((mouse_position[1]-5)//100))
                if(player_A.go(field, int((mouse_position[0]-5)//100), int((mouse_position[1]-5)//100)) == 1):
                    is_the_end = field.check_the_winner()
                    who_is_go += 1
                    screen.blit(text_0, (int((mouse_position[0]-5)//100)*100+50, int((mouse_position[1]-5)//100)*100+50))
            else:
                #pygame.draw.circle(screen, color_red, mouse_position, 2, 2)
                print('Player_B go to ', int((mouse_position[0] - 5) // 100), int((mouse_position[1] - 5) // 100))
                if(player_B.go(field, int((mouse_position[0] - 5) // 100), int((mouse_position[1] - 5) // 100)) == 1):
                    is_the_end = field.check_the_winner()
                    who_is_go += 1
                    screen.blit(text_x, (
                    int((mouse_position[0] - 5) // 100) * 100 + 50, int((mouse_position[1] - 5) // 100) * 100 + 50))
        pygame.display.flip()
