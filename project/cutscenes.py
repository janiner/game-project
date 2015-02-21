import pygame, sys
from pygame.locals import *


def cutscene(screen, text):
    font = pygame.font.Font("font/Dk Pundak.otf", 34)
    black = pygame.Surface((640, 400))
    black.fill((0, 0, 0))
    alpha = 255
    intro = True
    outro = False
    height = len(text)*(font.get_height()+3)
    image = pygame.Surface((640, height))
    y = 0
    for line in text:
        ren = font.render(line, 1, (255, 255, 255))
        image.blit(ren, (320-ren.get_width()/2, y*(font.get_height()+3)))
        y += 1
    while 1:
        pygame.time.wait(10)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == K_c:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return
                if e.key in (K_SPACE, K_RETURN):
                    intro = False
                    outro = True
        if intro:
            if alpha > 0:
                alpha -= 5
        if outro:
            if alpha < 255:
                alpha += 5
            else:
                return
        black.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 240-image.get_height()/2))
        screen.blit(black, (0, 0))
        ren = font.render("Press Enter to continue", 1, (255, 255, 255))
        screen.blit(ren, (320-ren.get_width()/2, 400))
        pygame.display.flip()
