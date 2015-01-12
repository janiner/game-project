import pygame, sys, random, glob

from Tkinter import *

def close():
    exit()

window = Tk()
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=close)

menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)
window.mainloop()

def scroll(x, direction):
    if direction == "left":
        x = x - 1
    elif direction == "right":
        x = x + 1
    return (x)

def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                  paused = False

                elif event.key == pyagme.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update()
        clock.tick(5)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_position = 0
        self.img_list = glob.glob("img/n*.png")
        self.image = pygame.image.load(self.img_list[self.img_position])
        self.rect = self.image.get_rect()
        self.rect.top = 130
        self.rect.left = 180
        self.jump = "stop"
        self.jump_number = 0

class innerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.Surface((64, 110))
        self.rect = self.image.get_rect()

def jump_update(y, jump, number):
    jump_speed = 20
    if number == 1:
        if jump == "up" and y < 50:
            jump = "down"
    elif number == 2:
        if jump == "up" and y < -10:
            jump = "down"
    if jump == "down" and y >= 140:
        jump = "stop"
        y = 140
        number = 0
    if jump == "up":
        y = y - jump_speed
    elif jump == "down":
        y = y + jump_speed
    return(y, jump, number)

pygame.init()
screen = pygame.display.set_mode((480, 320))
clock = pygame.time.Clock()
FPS = 20
BLUE = (0, 0, 255)
lovely_BLUE = (47, 164, 245)
RED = (255, 0, 0)
white = (255,255,255)

background = pygame.image.load("bg3.jpg")
back_rect = background.get_rect()
max_x = back_rect.right - 380
backsurf = pygame.Surface((480, 390))


x = 0

direction = "right"

lovely = Player()
innerLovely = innerPlayer()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if lovely.jump != "up" or lovely.jump != "down":
                if event.key == pygame.K_SPACE:
                    if lovely.jump_number < 2:
                        lovely.jump = "up"
                        lovely.jump_number += 1
            if event.key == pygame.K_p:
                pause()

    x = scroll(x, direction)
    backsurf.blit(background, (0,0), (x, 0, 480 + x, 390))            
    screen.blit(backsurf, (0,0))

    lovely.rect.top, lovely.jump, lovely.jump_number = jump_update(lovely.rect.top, lovely.jump, lovely.jump_number)
    screen.blit(lovely.image, lovely.rect)
    if lovely.img_position < 3:
            lovely.img_position += 1
    else:
            lovely.img_position = 0

    lovely.image = pygame.image.load(lovely.img_list[lovely.img_position])


    clock.tick(FPS)
    pygame.display.update()
game_intro()
