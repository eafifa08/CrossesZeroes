import Logic
import pygame
import sys

def who_is_winner(x):
    if x == 0:
        return 'Player A'
    elif x == 1:
        return 'Player B'
    elif x == 100:
        return 'Friendship'
    else:
        return 'whoiswinner_error'

player_A = Logic.Player(0)
print('created', player_A.name, 'with symbol ', player_A.symbol)
player_B = Logic.Player(1)
print('created', player_B.name, 'with symbol ', player_B.symbol)
field = Logic.Field()

pygame.init()
pygame.display.set_caption('Crosses & NuLLs')
color_grey = (100, 100, 100)
color_red = (250, 0, 0)

screen = pygame.display.set_mode((300, 300))
image_field = pygame.image.load('crosses_nulls_field.jpg')
image_rect = image_field.get_rect()
screen.fill(pygame.color.THECOLORS['black'])
screen.blit(image_field, image_rect)

#screen = pygame.display.set_mode((310, 310))
#r = pygame.Rect(5, 5, 300, 300)
#pygame.draw.rect(screen, color_grey, r, 0)
#line = pygame.draw.line(screen, color_red, [105, 5], [105, 305])
#line = pygame.draw.line(screen, color_red, [205, 5], [205, 305])
#line = pygame.draw.line(screen, color_red, [5, 105], [305, 105])
#line = pygame.draw.line(screen, color_red, [5, 205], [305, 205])
font = pygame.font.SysFont('couriernew', 20)
text_0 = font.render(str('0'), True, pygame.color.THECOLORS['green'])
text_x = font.render(str('x'), True, pygame.color.THECOLORS['blue'])

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
                print('Player_A go to ', int((mouse_position[0])//100), int((mouse_position[1])//100))
                if(player_A.go(field, int((mouse_position[0])//100), int((mouse_position[1])//100)) == 1):
                    is_the_end = field.check_the_winner()[0]
                    who_is_go += 1
                    screen.blit(text_0, (int((mouse_position[0])//100)*100+50, int((mouse_position[1])//100)*100+50))
            else:
                #pygame.draw.circle(screen, color_red, mouse_position, 2, 2)
                print('Player_B go to ', int((mouse_position[0]) // 100), int((mouse_position[1]) // 100))
                if(player_B.go(field, int((mouse_position[0]) // 100), int((mouse_position[1]) // 100)) == 1):
                    is_the_end = field.check_the_winner()[0]
                    who_is_go += 1
                    screen.blit(text_x, (
                    int((mouse_position[0]) // 100) * 100 + 50, int((mouse_position[1]) // 100) * 100 + 50))
        pygame.display.flip()
pygame.display.flip()

if is_the_end != 100:
    line_to_draw_winner = [[field.check_the_winner()[1][0]*100+50, field.check_the_winner()[1][1]*100+50],
                           [field.check_the_winner()[2][0]*100+50, field.check_the_winner()[2][1]*100+50],
                           [field.check_the_winner()[3][0]*100+50, field.check_the_winner()[3][1]*100+50]]
    pygame.draw.lines(screen, pygame.color.THECOLORS['orange'], False, line_to_draw_winner)
    pygame.display.flip()
nextStep = False
while not nextStep:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            nextStep = True

screen.fill(pygame.color.THECOLORS['green'], (0, 0, 300, 300), 0)
who_is_winner ='Winner is ' + str(who_is_winner(is_the_end))
text_winner = font.render(who_is_winner, True, pygame.color.THECOLORS['blue'])
screen.blit(text_winner, (5, 5))
pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



