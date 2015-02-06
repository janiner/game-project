import pygame, sys, time
from pygame.locals import *

pygame.init()

def Load(screen):
    WHITE = (255, 255, 255)
    ORANGE = (255, 103, 1)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    
    screen.fill(WHITE)
    comicFont = pygame.font.Font('font/DK Pundak.otf', 20)
    text = comicFont.render('PLEASE WAIT...', True, RED, WHITE)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery 
    screen.blit(text, textRect)
    pygame.display.update()

def Credits(screen):
    num = 0
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    screen.fill(WHITE)
    icon = pygame.image.load('logo/logo.png')
    rect = icon.get_rect()
    logo = pygame.transform.scale(icon, (300, 340))
    rect.centerx = screen.get_rect().centerx + 50
    rect.centery = screen.get_rect().centery + 70
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        comicFont = pygame.font.Font('font/DK Pundak.otf', 40)
        text = comicFont.render('CREATED BY LOVELY JAM', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 150
        screen.blit(text, textRect)
        screen.blit(logo, rect)
        pygame.display.update()
        num += 1
        if num > 1000:
            break

