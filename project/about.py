import pygame, sys, random, glob
import slidemenu
import load
import main
import highscorepy

from math import cos, radians
import pygame, sys, random, glob
from math import cos,radians

try: import GetEvent
except: from . import GetEvent

class back(pygame.sprite.Sprite):
    blue = (0, 0, 255)
    def __init__(self,color= blue, width=60, height=60):
        super(back, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()

    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y

    def set_image(self,filename=None):
        if (filename!=None):
            self.image=pygame.image.load(filename)
            self.rect=self.image.get_rect()

class Sound(pygame.sprite.Sprite):
    blue = (0, 0, 255)
    def __init__(self,color= blue, width=60, height=60):
        super(Sound, self).__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect=self.image.get_rect()

        self.sound = pygame.mixer.Sound("sounds/[Background.wav")

    def playsound(self):
        self.sound.play(-1)

    def set_position(self,x,y):
        self.rect.x=x
        self.rect.y=y

    def set_image(self,filename=None):
        if (filename!=None):
            self.image=pygame.image.load(filename)
            self.rect=self.image.get_rect()

    def stopsound(self):
        self.sound.stop()
        
def about(screen):
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("EM'S RUSH")
    RED= (255, 0, 0)
    about = pygame.image.load('others/help_.png')
    
    backb=pygame.sprite.Group()
    a_back=back()
    a_back.set_image("others/back.png")
    a_back.set_position(60,35)
    
    a_soundabout=Sound()
    
    icon = pygame.image.load('logo/icon.png')
    pygame.display.set_icon(icon)
    
    screen.blit(about, (0,0))
    backb.add(a_back)
    backb.draw(screen)
    a_soundabout.playsound()    
    while True:
       # pygame.time.wait(10)
        
        for event in pygame.event.get():
            
            if (event.type ==pygame.MOUSEBUTTONDOWN):
                if(event.pos[0] < a_back.rect.x+35  and event.pos[1]>a_back.rect.y and event.pos[0]>a_back.rect.x and event.pos[1]<a_back.rect.y+35):                    
                    from os.path import dirname,join
                    here = dirname('main.py')
                    scr = pygame.display.set_mode((640,400))
                    icon = pygame.image.load('logo/icon.png')
                    pygame.display.set_icon(icon)
                    bg = pygame.image.load(join(here,'others/start.jpg'))
                    scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
                    #~ scr.fill(-1)
                    pygame.display.flip()
                   
               
                    while True:
                        
                        resp= slidemenu.menu(['play',
                                         'highscore',
                                        'help',
                                         'quit::good bye'],
                                         font1      = pygame.font.Font(join(here,'font/DK Pundak.otf'),25),
                                        font2      = pygame.font.Font(join(here,'font/DK Pundak.otf'),30),
                                         tooltipfont= pygame.font.Font(join(here,'font/DK Pundak.otf'),12),
                                         color1     = (255,0,40),
                                         light      = 9,
                                         tooltiptime= 1000,
                                         cursor_img = pygame.image.load('others/mouse.png'),
                                         hotspot    = (38,15))
                        if resp[0] == "play":
                            load.Load(scr)
                            a_soundabout.stopsound()
                            main.main()
                        if resp[0] == "highscore":
                            a_soundabout.stopsound()
                            highscorepy.score(scr)
                        if resp[0] == "help":
                            a_soundabout.stopsound()
                            about(screen)
            
            #display.update()
                        if resp[0] != "re-show": break
                    print(resp)
                    quit()
            

        
        
        
        pygame.display.flip()
           
