import pygame

pygame.init()

window = pygame.display.set_mode((100,100))

pygame.display.set_caption("Girl Running")

black = (0,0,0)

white = (255,255,255)

clock = pygame.time.Clock()


image1 = pygame.image.load('m1.jpg')
image2 = pygame.image.load('m2.jpg')

image11 = 1

gameloop=True
while gameloop:

    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            gameloop=False

    window.fill(white)

    if (image11==1):
        window.blit(image1, (10,10))

    if (image11==2):
        window.blit(image2, (10,10))

    if (image11==2):
        image11=1

    else:
        image11+=1;

    pygame.display.flip()

    clock.tick(4)

pygame.quit()
