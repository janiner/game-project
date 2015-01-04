import pygame
import pygame.sprite as sprite

pygame.init()

pygame.display.set_caption("Girl Running")

window = pygame.display.set_mode((900,480))

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

background = pygame.image.load('bg.jpg').convert()

image1 = pygame.image.load('n1.png')
image2 = pygame.image.load('n2.png')
image3 = pygame.image.load('n3.png')
image4 = pygame.image.load('n4.png')

image11 = 1

background_size = background.get_size()
background_rect = background.get_rect()
window = pygame.display.set_mode(background_size)
window.fill(white)

w, h = background_size
x = 0
y = 0

x1 = -w
y1 = 0

x2 = 0


gameloop=True
while gameloop:
    
    window.blit(background, background_rect)
    
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            gameloop=False

    if x2 <= (w/2)-200:                 #move to center
        x2 += 20
    else:                               #move background
        x1 -= 20
        x -= 20

        window.blit(background, (x,y))
        window.blit(background, (x1,y1))

        if x < -w:
            x = w-10
        if x1 < -w:
            x1 = w-10
                
                
    if (image11==1):
        window.blit(image1, (x2,h-180))   
            
    if (image11==2):
        window.blit(image2, (x2,h-180))

    if (image11==3):
        window.blit(image3, (x2,h-180))

    if (image11==4):
        window.blit(image4, (x2,h-180))

    if (image11==2):
        image11=1

    else:
        image11+=1;
    
    pygame.display.flip()
    
    clock.tick(20)
    
pygame.quit()
