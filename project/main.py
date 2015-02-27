import pygame, sys, random, glob
import load
import slidemenu
import about

from math import cos, radians
import pygame, sys, random, glob
from math import cos,radians
try: import GetEvent
except: from . import GetEvent




screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("EM'S RUSH")

BLUE = (0, 0, 255)
lovely_BLUE = (47, 164, 245)
RED = (255, 0, 0)
white = (255,255,255)
moveX=0    
def scroll(x, direction):
    if direction == "left":
        x = x - 1
    elif direction == "right":
        x = x + 1

    elif direction =="rights":
        x=x+3
    return (x)


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background/pavement.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 420
    def update(self):
        self.rect.left -= 8

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("obstacles/poop.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 390
        self.rect.left = 480

    def update(self):
        self.rect.left -= 13
class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("obstacles/poop.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 100
        self.rect.left = 480

    def update(self):
        self.rect.left -= 8
        
class Pauseb(pygame.sprite.Sprite):
    blue = (0, 0, 255)
    def __init__(self,color= blue, width=60, height=60):
        super(Pauseb, self).__init__()
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

        self.sound = pygame.mixer.Sound("sounds/game.wav")

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

class reloadb(pygame.sprite.Sprite):
    blue = (0, 0, 255)
    def __init__(self,color= blue, width=60, height=60):
        super(reloadb, self).__init__()
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


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("others/coin.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = 100
        self.rect.left = 420

    def update(self):
        self.rect.left -= 11

    #def erase(self):
     #   self

class Soundmenu(pygame.sprite.Sprite):
    blue = (0, 0, 255)
    def __init__(self,color= blue, width=60, height=60):
        super(Soundmenu, self).__init__()
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

def nextLevel():
    RED= (255, 0, 0)
    lev_font = pygame.font.Font("font/DK Pundak.otf", 38)
    congrats = lev_font.render("Moving to", True, RED)
    level_surface = lev_font.render("Next Level", True, RED)
    surface = pygame.Surface((640, 400))
    surface.fill((0,0,0))
    surface.blit(congrats, (50, 50))
    surface.blit(level_surface, (50, 200))
    return (surface)

def savescore(score):
    highscorefile=open("highscore.txt", "w")
    highscorefile.write(str(score))
    highscorefile.close()

def getscore():
    highscore=0

    highscorefile=open("highscore.txt", "r")
    highscore=int(highscorefile.read())
    #print(highscore)
    highscorefile.close()

    return highscore

    
def pause():
    
    paused = True
    pausesg=pygame.sprite.Group()
    a_pauses=Pauseb()
    a_pauses.set_image("others/resume.png")
    a_pauses.set_position(270,60)

    reloadbut=pygame.sprite.Group()
    a_reloads=reloadb()
    a_reloads.set_image("others/retry.png")
    a_reloads.set_position(270,100)

    backbut=pygame.sprite.Group()
    a_backs=back()
    a_backs.set_image("others/menu.png")
    a_backs.set_position(270,140)

    sounds=pygame.sprite.Group()
    a_sound=Sound()
    
    soundmenu=pygame.sprite.Group()
    a_soundmenu=Soundmenu()
    
    
    
    while paused:
        a_sound.stopsound()
        
        BLACK = (0, 0, 0)
        WHITE = (255,255,255)
        RED = (255, 0, 0)
        pop = pygame.image.load("others/pause_board.png")
        screen.blit(pop, (180,-1))
        
        pausesg.add(a_pauses)
        pausesg.draw(screen)

        reloadbut.add(a_reloads)
        reloadbut.draw(screen)

        backbut.add(a_backs)
        backbut.draw(screen)
        
        
        
        for event in pygame.event.get():
            #if event.type == pygame.QUIT:
             #   pygame.quit()
              #  quit()

            #if event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_c:
              #    paused = False
            
            #if (event.type==pygame.MOUSEMOTION):
             #   mouse= pygame.mouse.get_pos()
              #  print(mouse)
               # print(a_reloads.rect.y)
            if (event.type ==pygame.MOUSEBUTTONDOWN):
                if(event.pos[0] < a_pauses.rect.x+100 and event.pos[1]>a_pauses.rect.y and event.pos[0]>a_pauses.rect.x and event.pos[1]<a_pauses.rect.y+32):
                    #a_sound.playsound()
                    paused=False
                    
                if(event.pos[0] < a_reloads.rect.x+100  and event.pos[1]>a_reloads.rect.y and event.pos[0]>a_reloads.rect.x and event.pos[1]<a_reloads.rect.y+31):
                    load.Load(screen)
                    a_sound.stopsound()
                    main()
                if(event.pos[0] < a_backs.rect.x+90  and event.pos[1]>a_backs.rect.y and event.pos[0]>a_backs.rect.x+5 and event.pos[1]<a_backs.rect.y+45):
                    from os.path import dirname,join
                    here = dirname('main.py')
                    scr = pygame.display.set_mode((640,400))
                    icon = pygame.image.load('logo/icon.png')
                    pygame.display.set_icon(icon)
                    bg = pygame.image.load(join(here,'others/start.jpg'))
                    scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
                    #~ scr.fill(-1)
                    pygame.display.flip()
                    a_sound.stopsound()
                    while True:
                        a_soundmenu.playsound()
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
                            a_soundmenu.stopsound()
                            load.Load(scr)
                            main()
                        if resp[0] == "highscore":
                            load.Load(scr)
                        if resp[0] == "help":
                            about.about(scr)
                        #if resp[0]=="quit":
                         #   quit()
            #display.update()
                        if resp[0] != "re-show": break
                    print(resp)
                    quit()
                    
        pygame.display.update()
        clock.tick(5)
    
    
def gameover():
    retry=pygame.sprite.Group()
    a_retry=reloadb()
    a_retry.set_image("others/retry.png")
    a_retry.set_position(207,150)

    menu=pygame.sprite.Group()
    a_menu=back()
    a_menu.set_image("others/menu.png")
    a_menu.set_position(340,150)
    
    RED = (255, 0, 0)
    WHITE = (255,255,255)
    go = pygame.image.load("others/gameover.png")

    
    
    
    #backsurf = pygame.Surface((640, 400))
    #backsurf.blit(go, (0,0))            
    #screen.blit(backsurf, (0,0))
    #ouch_font = pygame.font.Font("font/Dk Pundak.otf", 76)
    #ouch_surf = ouch_font.render("OUCH!!!", True, RED)
    #nextScreen = nextLevel()
    #backsurf.blit(nextScreen, (0, 0))
    #backsurf.blit(ouch_surf, (0, 0))
    #text=pygame.font.Font("font/Dk Pundak.otf",30)
    #text_appear=text.render("Game Over" , True, RED)
    #block = {'rect':pygame.Rect(200, 80, 230, 250),'color':WHITE}
    #pygame.draw.rect(screen, block['color'], block['rect'])
    #screen.blit(text_appear,(230,100))
    screen.blit(go, (150,10))

    
    menu.add(a_menu)
    menu.draw(screen)

    retry.add(a_retry)
    retry.draw(screen)

    sounds=pygame.sprite.Group()
    a_sound=Sound()
    a_sound.stopsound()

    font = pygame.font.Font("font/DK Pundak.otf", 30)
    highscore= getscore()
    text = font.render("your score: %s" %(highscore), 1, (10,15,30))
    screen.blit(text, (230,100))
    
    for event in pygame.event.get():
        if (event.type ==pygame.MOUSEBUTTONDOWN):
            if(event.pos[0] < a_retry.rect.x+88 and event.pos[1]>a_retry.rect.y and event.pos[0]>a_retry.rect.x and event.pos[1]<a_retry.rect.y+195):
                a_sound.stopsound()
                main()
            if(event.pos[0] < a_menu.rect.x+100 and event.pos[1]>a_menu.rect.y and event.pos[0]>a_menu.rect.x and event.pos[1]<a_menu.rect.y+33):
                from os.path import dirname,join
                here = dirname('main.py')
                scr = pygame.display.set_mode((640,400))
                icon = pygame.image.load('logo/icon.png')
                pygame.display.set_icon(icon)
                bg = pygame.image.load(join(here,'others/start.jpg'))
                scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
                    #~ scr.fill(-1)
                pygame.display.flip()
                a_sound.stopsound()
                
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
                        main()
                    if resp[0] == "highscore":
                        load.Load(scr)
                    if resp[0] == "help":
                        about.about(scr)
            
            #display.update()
                    if resp[0] != "re-show": break
                print(resp)
                quit()
                        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_position = 16
        self.img_list = glob.glob("img/l*.png")
        self.image = pygame.image.load(self.img_list[self.img_position])
        self.rect = self.image.get_rect()
        self.rect.top = 191
        self.rect.left = 120
        self.jump = "stop"
        self.jump_number = 0

class Players(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_position = 2
        self.img_list = glob.glob("imgs/l*.png")
        self.image = pygame.image.load(self.img_list[self.img_position])
        self.rect = self.image.get_rect()
        self.rect.top = 191
        self.rect.left = 120
        self.jump = "stop"
        self.jump_number = 0

                        
class Playerjump(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_position = 16
        
        self.image = pygame.image.load("img/l015.png")
        self.rect = self.image.get_rect()
        self.rect.top = 191
        self.rect.left = 120
        self.jump = "stop"
        self.jump_number = 0
        
class innerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.Surface((64, 110))
        self.rect = self.image.get_rect()

class innerPlayers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.Surface((64, 110))
        self.rect = self.image.get_rect()

def jump_update(y, jump, number):
    #l=pygame.image.load("img/l011.jpg")
    #screen.blit
    jump_speed = 20
    if number == 1:
        if jump == "up" and y < 50:
            jump = "down"
    elif number == 2:
        if jump == "up" and y < -10:
            jump = "down"
    if jump == "down" and y >= 140:
        jump = "stop"
        y = 191
        number = 0
    if jump == "up":
        y = y - jump_speed
    elif jump == "down":
        y = y + jump_speed
    return(y, jump, number)
    
def load_pavement(pavement):
    pavement.empty()
    for x in range(0, 650, 32):
        ground = Ground()
        ground.rect.left = x
        pavement.add(ground)
    return(pavement)



    
#def main():
 #   x=0
  #  background = pygame.image.load("background/Background_final.png")
   # back_rect = background.get_rect()
   # max_x = back_rect.right - 600
   # backsurf = pygame.Surface((640, 400))       
    #screen.blit(backsurf, (0,0))
    #for event in pygame.event.get():
     #   if event.type == pygame.KEYDOWN:
      #          if event.key == pygame.K_RIGHT:
       #             mains()
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    clock = pygame.time.Clock()
    pygame.display.set_caption("EM'S RUSH")
    icon = pygame.image.load('logo/icon.png')
    pygame.display.set_icon(icon)
    FPS = 10
    FFPS =20
    BLUE = (0, 0, 255)
    lovely_BLUE = (47, 164, 245)
    RED = (255, 0, 0)
    white = (255,255,255)

#load.Credits(screen)

    gameOver = False
    background = pygame.image.load("background/Background_final.png")
    back_rect = background.get_rect()
    max_x = back_rect.right - 600
    backsurf = pygame.Surface((640, 400))

    background2 = pygame.image.load("background/2bg.png")
    back_rect = background.get_rect()

    go = pygame.image.load("others/gameover.png")

#load.Load(screen)
    x = 0

    direction = "right"
    lives = 1
    lovely = Player()
    love = Playerjump()
    loves=Players()
    innerLovely = innerPlayer()
    innerLoves = innerPlayers()

    poop = Obstacle()
    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(poop)
    obstacle_spawn_delay = 10

    poops = Obstacles()
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(poop)
    obstacles_spawn_delay = 10

    coin = Coin()
    coin_group = pygame.sprite.Group()
    coin_group.add(coin)
    coin_spawn_delay = 5

    font = pygame.font.Font("font/DK Pundak.otf", 27)
    coins=0
    text = font.render("Score: %s" %(coins), 1, (10,15,30))
    #screen.blit(text, (250,20))

    

    pavement = pygame.sprite.Group()

    ground_counter = 32

    pavement = load_pavement(pavement)


    sounds=pygame.sprite.Group()
    a_sound=Sound()
    a_sound.set_image("others/soundOn.png")
    a_sound.set_position(65,10)
    a_sound.playsound()
    soundss=0
    
    soundmenu=pygame.sprite.Group()
    a_soundmenu=Soundmenu()
    
    pauseg=pygame.sprite.Group()
    a_pause=Pauseb()
    a_pause.set_image("others/pause.png")
    a_pause.set_position(10,10)
    paused =False

    
    
    backb=pygame.sprite.Group()
    a_back=back()
    a_back.set_image("others/back.png")
    a_back.set_position(580,10)

    reloadbutton=pygame.sprite.Group()
    a_reload=reloadb()
    a_reload.set_image("others/reload.png")
    a_reload.set_position(525,10)
  
    while True:
        
        for event in pygame.event.get():
            if(lives==1):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = "rights"
                    
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                    if lovely.jump != "up" or lovely.jump != "down":
                        if event.key == pygame.K_SPACE:
                            screen.blit(love.image, love.rect)
                            pygame.mixer.music.load('sounds-temporary/jump.mp3')
                            pygame.mixer.music.play()
                            if lovely.jump_number < 2:
                                lovely.jump = "up"
                                lovely.jump_number += 1
                #if event.key == pygame.K_p:
                 #   pause()
            #music = pygame.mixer.Sound("sounds-temporay/jum.mp3")
            #pygame.mixer.music.load('sounds-temporary/rush.wav')
            #pygame.mixer.music.play()
            #music.play()
            #ppp=0
            #if (event.type==pygame.MOUSEMOTION):
                #if(event.pos[0] < a_pause.rect.x+40  and event.pos[1]>a_pause.rect.y and event.pos[0]>a_pause.rect.x and event.pos[1]<a_pause.rect.y+40):
                #mouse= pygame.mouse.get_pos()
                    #pb=pygame.image.load("others/pause.png")
                    #pauser=pb.get_rect()
                    #pp=pygame.transform.scale(pb,(50,50))
                    #screen.blit(pp,(10,10))
                #print(mouse)
                if (event.type ==pygame.MOUSEBUTTONDOWN):
                    if(event.pos[0] < a_pause.rect.x+40  and event.pos[1]>a_pause.rect.y and event.pos[0]>a_pause.rect.x and event.pos[1]<a_pause.rect.y+40):
                        a_sound.stopsound()
                        pause()
                        a_sound.playsound()
                    
                        #paused=False
                #else:
                  #  if(event.pos[0] < a_pause.rect.x+40  and event.pos[1]>a_pause.rect.y and event.pos[0]>a_pause.rect.x and event.pos[1]<a_pause.rect.y+40):
                 #       paused=False
                    if(event.pos[0] < a_back.rect.x+570  and event.pos[1]>a_back.rect.y and event.pos[0]>a_back.rect.x and event.pos[1]<a_back.rect.y+570):                    
                        from os.path import dirname,join
                        here = dirname('main.py')
                        scr = pygame.display.set_mode((640,400))
                        icon = pygame.image.load('logo/icon.png')
                        pygame.display.set_icon(icon)
                        bg = pygame.image.load(join(here,'others/start.jpg'))
                        scr.blit(bg,bg.get_rect(center=scr.get_rect().center))
                    #~ scr.fill(-1)
                        pygame.display.flip()
                        a_sound.stopsound()
                        while True:
                            a_soundmenu.playsound()
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
                                a_soundmenu.stopsound()
                                load.Load(scr)
                                main()
                            if resp[0] == "highscore":
                                load.Load(scr)
                            if resp[0] == "help":
                                about.about(scr)
            
            #display.update()
                            if resp[0] != "re-show": break
                        print(resp)
                        quit()
                    
                    if(event.pos[0] < a_reload.rect.x+510  and event.pos[1]>a_reload.rect.y and event.pos[0]>a_reload.rect.x and event.pos[1]<a_reload.rect.y+510):
                        a_sound.stopsound()
                        main()
                    
                    
                    if soundss==0:
                        if(event.pos[0] < a_sound.rect.x+50  and event.pos[1]>a_sound.rect.y and event.pos[0]>a_sound.rect.x and event.pos[1]<a_sound.rect.y+50):
                            a_sound.set_image("others/soundOff.png")
                            a_sound.set_position(65,10)
                            a_sound.stopsound()
                            soundss=1
                       
                    else:
                        if(event.pos[0] < a_sound.rect.x+50  and event.pos[1]>a_sound.rect.y and event.pos[0]>a_sound.rect.x and event.pos[1]<a_sound.rect.y+50):
                            a_sound.set_image("others/soundOn.png")
                            a_sound.set_position(65,10)
                            a_sound.playsound()
                            soundss=0
                    
                    #if(event.pos[0] < a_sound.rect.x+50  and event.pos[1]>a_sound.rect.y and event.pos[0]>a_sound.rect.x and event.pos[1]<a_sound.rect.y+50):
#                        a_sound.set_image("others/soundOn.png")
 #                       a_sound.set_position(65,10)
  #                      a_sound.playsound()
                #if(event.pos[0] < a_sound.rect.x+50  and event.pos[1]>a_sound.rect.y and event.pos[0]>a_sound.rect.x and event.pos[1]<a_sound.rect.y+50):
                 #   print('sound')
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        direction = "right"
                    
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                    
            #if (event.type==pygame.MOUSEMOTION):
             #   mouse= pygame.mouse.get_pos()
              #  pb=pygame.image.load("others/pause.png")
               # pauser=pb.get_rect()

                #pp=pygame.transform.scale(pb,(90,90))

                #if(event.pos[0] < a_pause.rect.x+40  and event.pos[1]>a_pause.rect.y and event.pos[0]>a_pause.rect.x and event.pos[1]<a_pause.rect.y+40):
                 #   screen.blit(pp,pauser)
                #if(event.pos[0] < a_sound.rect.x+50  and event.pos[1]>a_sound.rect.y and event.pos[0]>a_sound.rect.x and event.pos[1]<a_sound.rect.y+50):
                    
                    
                if (event.type ==pygame.MOUSEBUTTONUP):
                    mouse = pygame.mouse.get_pos()
                    if(event.pos[0] < a_pause.rect.x+40  and event.pos[1]>a_pause.rect.y and event.pos[0]>a_pause.rect.x and event.pos[1]<a_pause.rect.y+40):
                        a_sound.stopsound()
                        paused=True
        #if lives==1:
            #a_sound.playsound()
         #   print('1')
                        
                            
        if x > max_x:
            x=0
            x = scroll(x, direction)
            backsurf.blit(background, (0,0), (x, 0, 640 + x, 420))            
            screen.blit(backsurf, (0,0))
            #gameOver = True
            #lives= 0

        if gameOver:
            #nextScreen = nextLevel()
            #screen.blit(nextScreen, (0, 0))
            #coin_group.remove(coin)
            a_sound.stopsound()
            gameover()
            #print ('f')
        
        if not gameOver:

            #a_sound.playsound()
            x = scroll(x, direction)
            backsurf.blit(background, (0,0), (x, 0, 640 + x, 420))            
            screen.blit(backsurf, (0,0))
        
            x = scroll(x, direction)
            backsurf.blit(background, (0,0), (x, 0, 640 + x, 420))            
            screen.blit(backsurf, (0,0))

            x = scroll(x, direction)
            backsurf.blit(background, (0,0), (x, 0, 640 + x, 420))            
            screen.blit(backsurf, (0,0))

            pauseg.add(a_pause)
            pauseg.draw(screen)

            backb.add(a_back)
            backb.draw(screen)

            reloadbutton.add(a_reload)
            reloadbutton.draw(screen)
       
            sounds.add(a_sound)
            sounds.draw(screen)
    
            lovely.rect.top, lovely.jump, lovely.jump_number = jump_update(lovely.rect.top, lovely.jump, lovely.jump_number)
            #screen.blit(love.image, love.rect)
            screen.blit(lovely.image, lovely.rect)
            if lovely.img_position < 16:
                lovely.img_position += 1
            else:
                lovely.img_position = 0

            lovely.image = pygame.image.load(lovely.img_list[lovely.img_position])

            if ground_counter > 0:
                pavement.update()
                ground_counter -= 8
            else:
                pavement = load_pavement(pavement)
                ground_counter = 32
        
            pavement.draw(screen)

            for obstacle in obstacle_group:
                if obstacle.rect.right < 0:
                    obstacle_group.remove(obstacle)
        
            if obstacle_spawn_delay > 0:
                obstacle_spawn_delay -= 1
            else:
                obstacle_group.add(Obstacle())
                obstacle_spawn_delay = random.randrange(40, 100, 10)
            obstacle_group.update()
            obstacle_group.draw(screen)
            
            innerLovely.rect.center = lovely.rect.center
            if pygame.sprite.spritecollideany(innerLovely, obstacle_group):
                lives=lives-1
                if (lives==0):
            #print("collision")
                    print("gg")
                   #a_sound.stopsound()
                    #gameOver = True


            innerLoves.rect.center = loves.rect.center
            if pygame.sprite.spritecollideany(innerLoves, obstacle_group):
                lives=lives-1
                if (lives==0):
            #print("collision")
                   #a_sound.stopsound()
                    gameOver = True
                    
            
            for coin in coin_group:
                if coin.rect.right < 0:
                    coin_group.remove(coin)
                    
            if coin_spawn_delay > 0:
                coin_spawn_delay -= 1
            else:
                coin_group.add(Coin())
                
                coin_spawn_delay = random.randrange(50, 100, 5)
            coin_group.update()
            coin_group.draw(screen)

            innerLovely.rect.center = lovely.rect.center


            #for runrurn
            #if pygame.sprite.spritecollideany(innerLovely, coin_group):
                #coin_group.remove(coin)
                #lovely.rect.top, lovely.jump, lovely.jump_number = jump_update(lovely.rect.top, lovely.jump, lovely.jump_number)
            #screen.blit(love.image, love.rect)
                
                #if loves.img_position < 2:
                 #   loves.img_position += 1
                #else:
                 #   loves.img_position = 0

                #loves.image = pygame.image.load(loves.img_list[loves.img_position])
                #screen.blit(loves.image, loves.rect)
                #clock.tick(30)
                
            #else:
                #lovely.rect.top, lovely.jump, lovely.jump_number = jump_update(lovely.rect.top, lovely.jump, lovely.jump_number)
            #screen.blit(love.image, love.rect)
                
                #if lovely.img_position < 16:
                 #   lovely.img_position += 1
                #else:
                 #   lovely.img_position = 0

                #lovely.image = pygame.image.load(lovely.img_list[lovely.img_position])
                #screen.blit(lovely.image, lovely.rect)
                
                #clock.tick(FPS)
            if pygame.sprite.spritecollideany(innerLovely, coin_group):
                if (lives==1):
                    coin_group.remove(coin)
                    coins = coins + 1
                    lives=1
            #else:
             #   lives=lives-0
              #  if(lives==0):
               #     gameover()
                #    print('gg')
            text = font.render("Score: %s" %(coins), 1, (10,15,30))
            screen.blit(text, (250,20))
            savescore(coins)

            

            #if obstacles_spawn_delay > 0:
             #   obstacles_spawn_delay -= 1
            #else:
             #   obstacles_group.add(Obstacles())
              #  obstacles_spawn_delay = random.randrange(80, 140, 5)
            #obstacles_group.update()
            #obstacles_group.draw(screen)  
            
        clock.tick(FPS)
        pygame.display.flip()
        pygame.display.update()
