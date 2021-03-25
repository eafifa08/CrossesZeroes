import Logic
import pygame
import sys

pygame.init()
pygame.display.set_caption('my test')
screen = pygame.display.set_mode((300, 300))
image_field = pygame.image.load('crosses_nulls_field.jpg')
image_rect = image_field.get_rect()
while True:
    screen.fill(pygame.color.THECOLORS['black'])
    screen.blit(image_field, image_rect)
    pygame.display.flip()

pygame.display.flip()