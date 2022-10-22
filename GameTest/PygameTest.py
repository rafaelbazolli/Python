import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start') #Nome da janela
window_surface = pygame.display.set_mode((800, 600)) #Largura , Altura

background = pygame.Surface((800, 600)) #vai definir o tamanho da surface do display que entrará na variável background
background.fill(pygame.Color('#000223')) #Preenche a variável background pelo comando fill()


manager = pygame_gui.UIManager((800, 600))
#pygame.rect(posição eixo x, posição eixo y), (largura do botão no eixo x, tamanho do botão no eixo y)
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Diga Olá', manager=manager)

clock = pygame.time.Clock() #Tem que ser com 'C' maiúsculo, senão não funciona

is_running = True
while is_running:
    var_tempo = clock.tick(60) / 1000.0 #Uma variável para calcular o tempo passado... conta até 60, divide por 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        manager.process_events(event)
        if event.type == pygame.USEREVENT:  #se houver algum evento do usuário, entra na estrutura condicional
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED: #se o evento for do tipo: botão pressionado, ele entra no proximo condicional
                if event.ui_element == hello_button: #Se o elemento que sofreu a ação foi o botão hello, aí ele exibe no terminal uma mensagem
                    print('Olá Mundo!')
    manager.update(var_tempo) #Atualizar a variável tempo

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface) #draw = desenhar

    pygame.display.update()