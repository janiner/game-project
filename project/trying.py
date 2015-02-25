import pygame, sys, random, glob
import load
import slidemenu

pygame.init()
moveX=0
moveY=0
screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("EM'S RUSH")
FPS = 20
BLUE = (0, 0, 255)
lovely_BLUE = (47, 164, 245)
RED = (255, 0, 0)
white = (255,255,255)
    
def scroll(xx, direction):
    xx = xx + 3
    return (xx)


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
        self.rect.left -= 8
        
def nextLevel():
    RED= (255, 0, 0)
    lev_font = pygame.font.Font("basefont.ttf", 38)
    congrats = lev_font.render("Moving to", True, RED)
    level_surface = lev_font.render("Next Level", True, RED)
    surface = pygame.Surface((640, 400))
    surface.fill((0,0,0))
    surface.blit(congrats, (50, 50))
    surface.blit(level_surface, (50, 200))
    return (surface)
        
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
def gameover():
    RED = (255, 0, 0)
    go = pygame.image.load("others/gameover.png")
    backsurf = pygame.Surface((640, 400))
    #backsurf.blit(go, (0,0))            
    #screen.blit(backsurf, (0,0))
    ouch_font = pygame.font.Font("font/Dk Pundak.otf", 76)
    ouch_surf = ouch_font.render("OUCH!!!", True, RED)
    #nextScreen = nextLevel()
    #backsurf.blit(nextScreen, (0, 0))
    #backsurf.blit(ouch_surf, (0, 0))
    screen.blit(go, (0,0))
    
        

class innerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.image = pygame.Surface((64, 110))
        self.rect = self.image.get_rect()

def jump_update(y, jump, number):
    jump_speed = 15
    if number == 1:
        if jump == "up" and y < 10:
            jump = "down"
    elif number == 2:
        if jump == "up" and y < -10:
            jump = "down"
    if jump == "down" and y >= 120:
        jump = "stop"
        y = 200
        number = 0
    if jump == "up":
        y = y - jump_speed
    elif jump == "down":
        y = y + jump_speed
    return(y, jump, number)

def load_pavement(pavement):
    pavement.empty()
    for x in range(0, 645, 32):
        ground = Ground()
        ground.rect.left = x
        pavement.add(ground)
    return(pavement)

def main():
    moveX=0
    moveY=0
    class Player(pygame.sprite.Sprite):
    
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
        
            self.img_position = 2
            self.x=x
            self.y=y
            self.width=50
            self.height=50
            self.i0 = pygame.image.load("m2.png")
            self.i1 = pygame.image.load("m0.png")
            self.i2 = pygame.image.load("m1.png")
            
            self.currentImage = 1
            #self.image = self.frame_set[self.currentImage]
            #self.rect = self.image.get_rect(
            #self.rect.top = 200
            #self.rect.left = 120
            self.jump = "stop"
            self.jump_number = 0
            self.timeTarget=10
            self.timeNum= 0
            self.walking = False
            self.jumping = False
            
        
        def update(self):
            self.timeNum+=1
            
            if (self.timeNum==self.timeTarget):

                if (self.currentImage==0):
                    self.currentImage+=1
            #elif (self.currentImage==1):
             #   self.currentImage+=2
                else:
                    self.currentImage=0
                self.timeNum=0

            self.render()
    

        def render(self):
            self.x=moveX
            if(moveX<0 & moveY==0 and self.walking == False):
                screen.blit(self.i0,(self.x,self.y))
            if(moveX>0 or self.walking == True ):
                
                if (self.currentImage==0):
                    screen.blit(self.i1, (self.x,self.y))
                else:
                    screen.blit(self.i2, (self.x,self.y))
            #if(self.jumping==True):
                
            

    
    screen = pygame.display.set_mode((640, 400))
    clock = pygame.time.Clock()
    pygame.display.set_caption("EM'S RUSH")
    FPS = 20
    BLUE = (0, 0, 255)
    lovely_BLUE = (47, 164, 245)
    RED = (255, 0, 0)
    white = (255,255,255)

   

#load.Credits(screen)
    gameLoop= True
    gameOver = False
    background = pygame.image.load("background/2bg.jpg")
    back_rect = background.get_rect()
    max_x = back_rect.right - 600
    backsurf = pygame.Surface((640, 400))

    go = pygame.image.load("others/gameover.png")

#load.Load(screen)
    xx = 0

    direction = "right"

    lovely = Player(120,200)
    innerLovely = innerPlayer()

    poop = Obstacle()
    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(poop)
    obstacle_spawn_delay = 10

    pavement = pygame.sprite.Group()

    ground_counter = 32

    pavement = load_pavement(pavement)


    while gameLoop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type==pygame.QUIT):
                gameLoop=False
            if (event.type==pygame.KEYDOWN):
                
                    
                if (event.key==pygame.K_RIGHT):
                    moveX = 5
                    lovely.walking = True
                    
                if (lovely.jump != "up" or lovely.jump != "down"):
                    if (event.key == pygame.K_SPACE):
                        print "fff"
                        if (lovely.jump_number < 2):
                            lovely.jumping = True
                            lovely.jump = "up"
                            lovely.jump_number += 1
                            
                if event.key == pygame.K_p:
                    pause()
            if (event.type==pygame.KEYUP):    

                if (event.key==pygame.K_RIGHT):
                    moveX = 0
                    lovely.walking = False
                if (event.key == pygame.K_SPACE):
                    moveY=0
                    lovely.jumping = False
                
                if event.key == pygame.K_p:
                    pause()
        
        if xx > max_x:
            gameOver = True
        if gameOver:
            nextScreen = nextLevel()
            screen.blit(nextScreen, (0, 0))
        elif not gameOver and moveX>0 or lovely.jumping== True:
            #x = scroll(x, direction)
            #backsurf.blit(background, (0,0), (x, 0, 640 + x, 420))            
            #screen.blit(backsurf, (0,0))


            xx = scroll(xx, direction)
            backsurf.blit(background, (0,0), (xx, 0, 640 + xx, 420))            
            screen.blit(backsurf, (0,0))

            #xx = scroll(xx, direction)
            #backsurf.blit(background, (0,0), (xx, 0, 640 + xx, 420))            
            #screen.blit(backsurf, (0,0))
            
            if (moveX==0):
                
                lovely.update()
            if (moveX>0 ):
                lovely.x+=moveX
                lovely.y+=moveY
            
            #player.update()
            if (lovely.jump_number>0):
                lovely.y, lovely.jump, lovely.jump_number = jump_update(lovely.y, lovely.jump, lovely.jump_number)

            lovely.update()
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
                obstacle_spawn_delay = random.randrange(80, 140, 5)
            obstacle_group.update()
            obstacle_group.draw(screen)


            if pygame.sprite.spritecollideany(innerLovely, obstacle_group):
            #print("collision")
                gameover()
        
    
        

            
        
        clock.tick(FPS)
        #pygame.display.flip()
        pygame.display.update()
