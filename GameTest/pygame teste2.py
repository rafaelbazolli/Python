import pygame

pygame.init()

#### Create a canvas on which to display everything ####
window = (400,400)
screen = pygame.display.set_mode(window)
#### Create a canvas on which to display everything ####

#### Create a surface with the same size as the window ####
background = pygame.Surface(window)
#### Create a surface with the same size as the window ####

#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(255,255,255),(40,20,120,120)) ## Primeiro () define cor. // Segundo (posição eixo x, posição eixo y,tamanho do objeto em x, tamanho do objeto em y)
pygame.draw.rect(background,(255,0,255),(120,120,50,50))
#### Populate the surface with objects to be displayed ####

#### Blit the surface onto the canvas ####
screen.blit(background,(0,0))  ##Coloca o background na frente(blit), e como o background está com as imagens, ele mostra os quadrados.
                                # 0,0 é a posição x,y em que a ponta superior esquerda do background vai ser colocada

#### Update the the display and wait ####
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#### Update the the display and wait ####

pygame.quit()