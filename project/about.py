import pygame, sys, random, glob
from cutscenes import *

def about(screen):
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("EM'S RUSH")
    RED= (255, 0, 0)
    about = pygame.image.load('obstacles/poop.png')
    screen.blit(about, (0,0))
    
    
   # pygame.display.flip()
    
def help(screen):
    cutscene(screen, ["EM's RUSH",
    "",
    "Move: Arrow Keys",
    "Jump: Space bar"])          
