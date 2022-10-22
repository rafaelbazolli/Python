import pygame
import pygame_gui
from pygame_gui.elements import UIButton

pygame.init()

pygame.display.set_caption('Quick Start') #Nome da janela
ui_window = pygame.display.set_mode((800, 600)) #Largura , Altura

background = pygame.Surface((800, 600)) #vai definir o tamanho da surface do display que entrará na variável background
background.fill(pygame.Color('#000223')) #Preenche a variável background pelo comando fill()
manager = pygame_gui.UIManager((800, 600))

button_layout_rect = pygame.Rect(30, 20, 100, 20)
UIButton(relative_rect=button_layout_rect, text='Hello', manager=manager, container=ui_window)



clock = pygame.time.Clock() #Tem que ser com 'C' maiúsculo, senão não funciona

is_running = True
while is_running:
    var_tempo = clock.tick(60) / 1000.0 #Uma variável para calcular o tempo passado... conta até 60, divide por 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        manager.process_events(event)
    manager.update(var_tempo) #Atualizar a variável tempo

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface) #draw = desenhar

    pygame.display.update()